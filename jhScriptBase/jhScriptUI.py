# encoding:utf-8
# !/usr/bin/env python
# jhScriptUI.py
# author : SeokWon Choi

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from PySide2 import QtCore, QtGui, QtWidgets
import maya.cmds as cmds
import maya.mel as mel
import platform
import json
import os
import re

if platform.system() == "Windows":
    SCRIPTS_PATH =  "/".join(os.path.dirname(os.path.abspath(__file__)).split("\\")) + "/scripts/"
else:
    CURRENTPATH = os.path.abspath(__file__)
    SCRIPTS_PATH = os.path.join(os.path.dirname(CURRENTPATH), "scripts/")
if not SCRIPTS_PATH in sys.path:
    sys.path.append(SCRIPTS_PATH)

class undoCheck(object):
    def __enter__(self):
        cmds.undoInfo(openChunk=True)

    def __exit__(self, *exc):
        cmds.undoInfo(closeChunk=True)

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle("Jihye    B O D D A R I")
        self.resize(321, 241)
        self.setStyleSheet("QMainWindow{background-color:#2A2A2A}")
        ftA = QtGui.QFont("Helvetica", 11, QtGui.QFont.DemiBold)
        btA = "QPushButton{color: qradialgradient(cx:0.5, cy:0.5, radius:5, fx:0.5, fy: 1, stop:0 rgba(223,223,223,255), stop:0.2 rgba(223,223,223,180), stop:0.4 rgba(223,223,223,60));" \
              " background-color: qradialgradient(cx:0.5, cy:0.5, radius:2, fx:0.5, fy: 1, stop:0 rgba(93,202,184,210), stop:0.2 rgba(93,202,184,144), stop:0.4 rgba(93,202,184,32));" \
              " border-radius:35px} " \
              "QPushButton:hover{color: qradialgradient(cx:0.5, cy:0.5, radius:5, fx:0.5, fy: 1, stop:0 rgba(223,223,223,255), stop:0.2 rgba(223,223,223,180), stop:0.4 rgba(223,223,223,60));" \
              " background-color: qradialgradient(cx:0.5, cy:0.5, radius:2, fx:0.5, fy: 1, stop:0 rgba(235,50,50,210), stop:0.2 rgba(235,50,50,144), stop:0.4 rgba(255,20,20,32));" \
              " border-radius:35px}"
        self.paieBtn = QtWidgets.QPushButton(self)
        self.paieBtn.setGeometry(10,10,70,70)
        self.paieBtn.setText("Pose-L")
        self.paieBtn.setStyleSheet(btA)
        self.paieBtn.setFont(ftA)

        self.snapBtn = QtWidgets.QPushButton(self)
        self.snapBtn.setGeometry(87, 10, 70, 70)
        self.snapBtn.setText("Snap")
        self.snapBtn.setStyleSheet(btA)
        self.snapBtn.setFont(ftA)

        self.kkCtrlBtn = QtWidgets.QPushButton(self)
        self.kkCtrlBtn.setGeometry(164, 10, 70, 70)
        self.kkCtrlBtn.setText("kkCtrl")
        self.kkCtrlBtn.setStyleSheet(btA)
        self.kkCtrlBtn.setFont(ftA)

        self.tweenBtn = QtWidgets.QPushButton(self)
        self.tweenBtn.setGeometry(241, 10, 70, 70)
        self.tweenBtn.setText("tween-M")
        self.tweenBtn.setStyleSheet(btA)
        self.tweenBtn.setFont(ftA)

        self.camRigBtn = QtWidgets.QPushButton(self)
        self.camRigBtn.setGeometry(10, 87, 70, 70)
        self.camRigBtn.setText("camRig")
        self.camRigBtn.setStyleSheet(btA)
        self.camRigBtn.setFont(ftA)

        self.worldSnapBtn = QtWidgets.QPushButton(self)
        self.worldSnapBtn.setGeometry(87, 87, 70, 70)
        self.worldSnapBtn.setText("W-Snap")
        self.worldSnapBtn.setStyleSheet(btA)
        self.worldSnapBtn.setFont(ftA)

        self.polyPlateBtn = QtWidgets.QPushButton(self)
        self.polyPlateBtn.setGeometry(164, 87, 70, 70)
        self.polyPlateBtn.setText("Img-P")
        self.polyPlateBtn.setStyleSheet(btA)
        self.polyPlateBtn.setFont(ftA)

        self.followCamBtn = QtWidgets.QPushButton(self)
        self.followCamBtn.setGeometry(241, 87, 70, 70)
        self.followCamBtn.setText("F-Cam")
        self.followCamBtn.setStyleSheet(btA)
        self.followCamBtn.setFont(ftA)

        self.cppvBtn = QtWidgets.QPushButton(self)
        self.cppvBtn.setGeometry(10, 164, 70, 70)
        self.cppvBtn.setText("Pivot_CP")
        self.cppvBtn.setStyleSheet(btA)
        self.cppvBtn.setFont(ftA)

        self.shakerBtn = QtWidgets.QPushButton(self)
        self.shakerBtn.setGeometry(87, 164, 70, 70)
        self.shakerBtn.setText("Shaker")
        self.shakerBtn.setStyleSheet(btA)
        self.shakerBtn.setFont(ftA)

        self.addFrBtn = QtWidgets.QPushButton(self)
        self.addFrBtn.setGeometry(164, 164, 70, 70)
        self.addFrBtn.setText("Add Fr")
        self.addFrBtn.setStyleSheet(btA)
        self.addFrBtn.setFont(ftA)

        self.locsBtn = QtWidgets.QPushButton(self)
        self.locsBtn.setGeometry(241, 164, 70, 70)
        self.locsBtn.setText("locs")
        self.locsBtn.setStyleSheet(btA)
        self.locsBtn.setFont(ftA)

        self.paieBtn.clicked.connect(self.paieExc)
        self.snapBtn.clicked.connect(self.snapExc)
        self.kkCtrlBtn.clicked.connect(self.kkCtrlExc)
        self.tweenBtn.clicked.connect(self.tweenExc)
        self.camRigBtn.clicked.connect(self.camRigExc)
        self.worldSnapBtn.clicked.connect(self.wsnapExc)
        self.polyPlateBtn.clicked.connect(self.plateExc)
        self.followCamBtn.clicked.connect(self.followCam)
        self.cppvBtn.clicked.connect(self.cppv)
        self.shakerBtn.clicked.connect(self.shaker)
        self.addFrBtn.clicked.connect(self.addFr)
        self.locsBtn.clicked.connect(self.locs)

    def paieExc(self):
        global paieUI
        try:
            paieUI.close()
        except:
            pass
        import paieMD
        reload(paieMD)
        paieUI = paieMD.paie()

    def snapExc(self):
        selList = cmds.ls(sl=True)
        master = selList[0]
        slave = selList[1]
        cmds.parentConstraint(master, slave, w=1, mo=False)
        cmds.delete(hierarchy=True, cn=True)

    def kkCtrlExc(self):
        mel.eval('source "{path}kk_controllersMD.mel";kk_controllers;'.format(path=SCRIPTS_PATH))

    def tweenExc(self):
        global tweenUI
        try:
            tweenUI.close()
        except:
            pass
        import tween_machineMD
        reload(tween_machineMD)
        tweenUI = tween_machineMD.start()

    def camRigExc(self):
        mel.eval('source "{path}mmRigBuilderMD.mel";mmRigBuilder'.format(path=SCRIPTS_PATH))

    def wsnapExc(self):
        global wsnapUI
        try:
            wsnapUI.close()
        except:
            pass
        import wsnpUI
        reload(wsnpUI)
        wsnapUI = wsnpUI.app()

    def plateExc(self):
        global plateUI
        try:
            plateUI.close()
        except:
            pass
        import polyImagePlaneMD
        reload(polyImagePlaneMD)
        plateUI = polyImagePlaneMD.polyImagePlane()

    def followCam(self):
        sel = str(cmds.ls(sl=True)[0])
        cam = cmds.camera(coi=5, cs=1, fl=35, ff="Fill", lsr=1, hfo=0, hfa=1.4173, vfa=0.9449, vfo=0, ovr=1, mb=False, sa=144, ncp=1, fcp=1000000, o=False, ow=30, pze=False, hpn=0, vpn=0, zom=1)
        camTr = cmds.createNode("transform", n=str(cam[0] + "_FollowCam"))
        cmds.parent(cam[0], camTr)
        tr = cmds.xform(sel, q=True, ws=True, t=True)
        cmds.xform(camTr, ws=True, t=tr)
        cmds.parentConstraint(sel, camTr, mo=True)

    def cppv(self):
        sel = cmds.ls(sl=True)
        pvPoint = cmds.xform(sel[0], q=True, ws=True, t=True)
        cmds.move(pvPoint[0], pvPoint[1], pvPoint[2], sel[1] + ".scalePivot", sel[1] + ".rotatePivot", a=True)

    def shaker(self):
        global shakerUI
        try:
            shakerUI.close()
        except:
            pass
        import sw_shakerM
        reload(sw_shakerM)
        shakerUI = sw_shakerM.main()

    def addFr(self):
        with undoCheck():
            minT = cmds.playbackOptions(q=True, min=True)
            maxT = cmds.playbackOptions(q=True, max=True)
            getN = 10
            sel = cmds.ls(sl=True)
            for i in sel:
                for j in cmds.listAttr(str(i), k=True):
                    hd = cmds.keyframe(str(i), q=True, at=str(j))
                    if hd != None:
                        cmds.setKeyframe(str(i), at=str(j), t=(minT, maxT), i=True)
                        if not minT - 1 in cmds.keyframe(str(i), q=True, at=str(j)):
                            subA = cmds.getAttr(str(i) + "." + str(j), t=minT) - cmds.getAttr(str(i) + "." + str(j),t=minT + 1)
                            cmds.setKeyframe(str(i), at=str(j), t=minT - getN, v=cmds.getAttr(str(i) + "." + str(j), t=minT) + getN * subA)
                            cmds.keyTangent(str(i), at=str(j), t=(minT - getN, minT - getN), itt="linear", ott="linear")
                        if not maxT + 1 in cmds.keyframe(str(i), q=True, at=str(j)):
                            subB = cmds.getAttr(str(i) + "." + str(j), t=maxT) - cmds.getAttr(str(i) + "." + str(j),t=maxT - 1)
                            cmds.setKeyframe(str(i), at=str(j), t=maxT + getN, v=cmds.getAttr(str(i) + "." + str(j), t=maxT) + getN * subB)
                            cmds.keyTangent(str(i), at=str(j), t=(maxT + getN, maxT + getN), itt="linear", ott="linear")

    def locs(self):
        global locUI
        try:
            locUI.close()
        except:
            pass
        import locs
        reload(locs)
        locUI = locs.self_loc()


def main():
    global myWindow
    try:
        myWindow.close()
    except:
        pass
    myWindow = Window()
    myWindow.show()
    return myWindow

if __name__ == '__main__':
    main()