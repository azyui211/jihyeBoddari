"""
PolyImagePlane

Creates a polygon plane that mimics the position of an camera image plane.

To use, simply select the camera image plane and run the script.

import polyImagePlane
polyImagePlane.main()

Or if you know the name of the camera, camera shape and image plane directly,
you can call the function directly.

import polyImagePlane
polyImagePlane.createPolyImagePlane('cameraName', 'cameraShapeName', 'imagePlaneName')
"""

import maya.cmds as cmds
import math

def getLongName(name):
    if cmds.objExists(name):
        return str(cmds.ls(name, long=True)[0])
    return None

def getShortName(name):
    if cmds.objExists(name):
        return str(cmds.ls(name)[0])
    return None

def createPolyImagePlane(camera, cameraShape, imagePlane):
    # Create Nodes
    implane, polyPlane = cmds.polyPlane(n="projectionCam_PLY", sx=1, sy=1, cuv=2, ch=1, ax=(0,1,0), w=1, h=1)
    planeShape = str(cmds.listRelatives(implane, c=True, type="mesh")[0])
    cmds.parent(implane, camera)
    # Add expression
    exp = ''
    exp += 'float $f = %s.focalLength;\n' % cameraShape
    exp += 'float $fbw = %s.horizontalFilmAperture;\n' % cameraShape
    exp += 'float $fbh = %s.verticalFilmAperture;\n' % cameraShape
    exp += 'float $fov = rad_to_deg(2 * atan( ($fbw*25.4) / (2 * $f) ));\n'
    exp += 'float $planeScale = 2*(%s.depth)*(tand($fov/2.0));\n\n' % imagePlane
    exp += '%s.width = 1.0;\n' % polyPlane
    exp += '%s.height = $fbh/$fbw;\n\n' % polyPlane
    exp += 'translateX = $planeScale*0.5*((%s.offsetX/2.54)/(($fbw/2.54)*0.5));\n' % imagePlane
    exp += 'translateY = $planeScale*0.5*((%s.offsetY/2.54)/(($fbw/2.54)*0.5));\n' % imagePlane
    exp += 'translateZ = -1*%s.depth;\n' % imagePlane
    exp += 'rotateX = 90.0;\n'
    exp += 'rotateY = rotateZ = 0.0;\n\n'
    exp += 'scaleX = scaleY = scaleZ = $planeScale;\n\n'
    cmds.expression(string=exp, object=implane, alwaysEvaluate=True, unitConversion='all')
    return (implane, planeShape, polyPlane)

def polyImagePlane():
    camera = None
    cameraShape = None
    imagePlane = []
    tmp = cmds.ls(sl=True, dag=True, type='imagePlane')
    if len(tmp) > 0:
        imagePlane.append(tmp[0])
    camList = cmds.ls(sl=True, dag=True, type="camera")
    for camName in camList:
        camIP = cmds.listConnections("%s.imagePlane"%camName, sh=True, d=True)
        if camIP:
            imagePlane.append(camIP[0])
    imagePlaneList = list(set(imagePlane))
    if len(imagePlaneList) == 0:
        return False
    for imagePlane in imagePlaneList:
        conn = [str(m) for m in cmds.listConnections(imagePlane, type="camera", shapes=True) if str(m) == imagePlane.split("->")[0]]
        if len(conn) > 0:
            cameraShape = getLongName(conn[0])
            camera = cmds.listRelatives(cameraShape, parent=True)[0]
            camera = getLongName(camera)
        else:
            return False
        implane, planeShape, polyPlane = createPolyImagePlane(camera, cameraShape, imagePlane)
        cmds.select(implane, replace=True)
        cmds.setAttr("%s.overrideLevelOfDetail"%planeShape, 1)
    seldp = str(cmds.duplicate(implane, rr=True)[0])
    cmds.parent(seldp, w=True)
    temp = str(cmds.parentConstraint(implane, seldp, mo=False, w=True)[0])
    minT = cmds.playbackOptions(q=True, min=True)
    maxT = cmds.playbackOptions(q=True, max=True)
    cmds.bakeResults(seldp, sm=False, t=(minT, maxT), mr=True, pok=True)
    cmds.delete(temp)
    scaleList = ["scaleX", "scaleY", "scaleZ"]
    scl = [float(cmds.getAttr(implane + "." + i)) for i in scaleList]
    cmds.delete(implane)
    if cmds.objExists("|aniGeom"):
        cmds.parent(seldp, "|aniGeom")
    for sca in scaleList:
        cmds.setAttr(seldp + "." + sca, scl[scaleList.index(sca)])
    try:
        cmds.rename(seldp, "projectionCard")
    except:
        pass
    cmds.selectKey(k=True)
    cmds.filterCurve(f="euler")
    return True