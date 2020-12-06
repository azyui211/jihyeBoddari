# _*_ coding: utf-8 _*_
# author : HyeYeon Kim

import os
import maya.cmds as cmds
import maya.mel
import maya.OpenMayaAnim as animAPI

class hyClass():
    def __init__(self): 
        self.win = 'hyClass_locator&constrain'
        self.targetObj_world = []
        self.aniLoc_world = []
    

    def ui(self):

        if cmds.window(self.win, exists = 1) == True: 
            cmds.deleteUI(self.win)
        
        window = cmds.window(self.win,title="locator&constrain", iconName='locator&constrain', widthHeight=(250, 210) )
        cmds.columnLayout( adjustableColumn=True )
        cmds.button( label='makelocator(0,0,0)',command = lambda *x:self.makelocator_zero())
        cmds.button( label='makelocator_snap',command = lambda *x:self.makelocator())
        cmds.button( label='bakeSimulation_locator',command = lambda *x:self.bsloc())
        cmds.button( label='sameKey_locator', command = lambda *x:self.sameloc())
        cmds.button( label='constrainParents_locator', command = lambda *x:self.conloc())
        cmds.button( label='bakeSimulation', command = lambda *x:self.bs())
        cmds.button( label='maintain=1_constrainParents', command = lambda *x:self.maintainconsParent())
        cmds.button( label='maintain=0_constrainParents', command = lambda *x:self.consParent())
        cmds.button( label='setInfinity', command = lambda *x:self.setInfinit())
        cmds.setParent( '..' )
        cmds.showWindow(window)
        
 
    def makelocator_zero(self):
        cmds.spaceLocator ( p = [0,0,0])    
    
    
    def makelocator(self):
        
        sel = cmds.ls(sl=1)
        locator_list = [] 
        pac = []
        
        for x in sel :
            loc = cmds.spaceLocator ( p = [0,0,0], n = x+'_Loc' )[0] 
            pc = cmds.parentConstraint ( x , loc , weight = 1 )
            locator_list.append ( loc ) 
            pac.append ( pc[0] ) 
        
        
        cmds.delete ( pac ) 
        
        cmds.select (locator_list)
    
    

    
    def bsloc(self):
        sel = cmds.ls(sl=1)
        locator_list = [] 
        pac = []
        
        for x in sel :
            loc = cmds.spaceLocator ( p = [0,0,0], n = x+'_Loc' )[0] 
            pc = cmds.parentConstraint ( x , loc , weight = 1 )
            locator_list.append ( loc )
            pac.append ( pc[0] )
        
        
        min = cmds.playbackOptions(q=1,min=1)
        max = cmds.playbackOptions(q=1,max=1)
        cmds.select ( locator_list , r=1 )
        
        cmds.refresh(suspend=1) 
        cmds.bakeSimulation(t = (min, max), sb=1 )
        cmds.refresh(suspend=0) 
        cmds.delete ( pac )
        

        if len ( sel ) == len ( locator_list ) :
            for i in range ( len ( locator_list ) ):
                cmds.parentConstraint ( locator_list[i] , sel[i] , weight =1 )   
        cmds.select ( sel, r=1 )
        
        
    
    
    def sameloc(self):
        sel = cmds.ls(sl=1)
        locator_list = [] 
        pac = []
        
        for x in sel :
            loc = cmds.spaceLocator ( p = [0,0,0], n = x+'_loc' )[0] 
            cmds.setKeyframe(loc)
            pc = cmds.parentConstraint ( x , loc , weight = 1 )
            locator_list.append ( loc )
            pac.append ( pc[0] ) 
            
        cmds.select ( sel,locator_list, r=1 )
        
        minValue = animAPI.MAnimControl.minTime().value()
        
        maxValue = animAPI.MAnimControl.maxTime().value()
        
        
        
        keyNumbers = len(list(set(cmds.keyframe(cmds.ls(sl=True), query=True, timeChange=True, time=(minValue,maxValue)))))
        
        
        print keyNumbers
        
        for i in range(0,keyNumbers):
            cmds.refresh(suspend=1)
        
            cmds.setKeyframe()
            
            cmds.currentTime(cmds.findKeyframe( timeSlider=True, which="next" ))
            cmds.refresh(suspend=0)
            
        cmds.delete ( pac )

        if len ( sel ) == len ( locator_list ) :
            for i in range ( len ( locator_list ) ):
                cmds.parentConstraint ( locator_list[i] , sel[i] , weight =1 )
    
    def conloc(self):
        sel = cmds.ls(sl=1)
        locator_list = [] # 빈 리스트를 만들어 놓습니다!
        pac = []
        
        for x in sel :
            loc = cmds.spaceLocator ( p = [0,0,0], n = x+'_Loc' )[0]  # 만든거의 첫번째꺼를 쓰겠다!!!
            pc = cmds.parentConstraint ( x , loc , weight = 1 )
            locator_list.append ( loc ) # .append 포 구문에서 나온 loc를 리스트에 넣어주는 기능입니다!!!
            pac.append ( pc[0] ) # .append 포 구문에서 나온 loc를 리스트에 넣어주는 기능입니다!!!
            
            
    #5
    
    def bs(self):
        sel = cmds.ls(sl=1)
        
        
        min = cmds.playbackOptions(q=1,min=1)
        max = cmds.playbackOptions(q=1,max=1)
        cmds.select ( sel , r=1 )
        
        cmds.refresh(suspend=1) #화면 끄는 스크립트 입니다!! 속도 빠르게 하기 위해
        cmds.bakeSimulation(t = (min, max), sb=1 )
        cmds.refresh(suspend=0) #화면 켜는 스크립트 입니다!!
        
    #6
    
    def maintainconsParent(self):
        
        sel = cmds.ls(sl=1)
        pc = cmds.parentConstraint ( sel[0] , sel[1] ,mo=1, weight = 1 )
   
    
    
    #7
    def consParent(self):
        
        sel = cmds.ls(sl=1)
        pc = cmds.parentConstraint ( sel[0] , sel[1] ,mo=0, weight = 1 )
        
        
        
    def setInfinit(self):
        first=cmds.findKeyframe(w="first")
        last=cmds.findKeyframe(w="last")
        cmds.keyTangent(cmds.ls(sl=True), edit=True, inTangentType='plateau', time =(first,first))
        cmds.keyTangent(cmds.ls(sl=True), edit=True, outTangentType='plateau', time =(last,last))
        cmds.setInfinity( pri='linear', poi='linear' )
        cmds.animCurveEditor( 'graphEditor1GraphEd', edit=True, displayInfinities='on')


def self_loc():
	if not os.path.isdir(os.path.dirname(__file__)):
		return 
	runScript = hyClass()
	runScript.ui()

