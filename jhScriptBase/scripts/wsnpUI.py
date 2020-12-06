import maya.cmds as cmds
from PySide2 import QtCore, QtWidgets, QtGui

'''
@Jesse

Snap the selected controller to the world for the selected amount of frames 

1) Get on the frame where the controller should start to be snaped
2) click on start
3) Get to the frame where the controller should stop to be snapped 
4) click on end 
5) Select controller, click on Snap

@Seokwon - 2019.12.05 Update
- Add parent / point / orient selection mode.
- Add Reverse

'''

class undoCheck(object):
	def __enter__(self):
		cmds.undoInfo(openChunk=True)

	def __exit__(self, *exc):
		cmds.undoInfo(closeChunk=True)

class Window(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)
		# UI
		self.setWindowTitle("World Snap")
		self.resize(220, 137)
		self.setStyleSheet("background-color:rgb(210,210,210)")
		fontA = QtGui.QFont()
		fontA.setPointSize(11)
		fontA.setBold(True)
		buttonColA = "QPushButton{color: white; background-color: gray} QPushButton:hover{color: black; background-color: lightblue}"
		self.dirChk = QtWidgets.QCheckBox(self)
		self.dirChk.setGeometry(QtCore.QRect(10, 7, 76, 20))
		self.dirChk.setText("Reverse")
		self.dirChk.setStyleSheet("QCheckBox{color:black;}")
		self.conCmb = QtWidgets.QComboBox(self)
		self.conCmb.setGeometry(QtCore.QRect(130, 7, 90, 20))
		self.conCmb.addItems(["Translate", "Rotate", "Both"])
		self.conCmb.setStyleSheet("QComboBox{color:black; background-color:lightblue; selection-color: black; selection-background-color: lightblue;} QComboBox QAbstractItemView{color:black;background:lightblue}")
		self.stBtn = QtWidgets.QPushButton(self)
		self.stBtn.setGeometry(QtCore.QRect(0, 32, 108, 50))
		self.stBtn.setStyleSheet(buttonColA)
		self.stBtn.setFont(fontA)
		self.stBtn.setText("Start : ")
		self.endBtn = QtWidgets.QPushButton(self)
		self.endBtn.setGeometry(QtCore.QRect(112, 32, 108, 50))
		self.endBtn.setStyleSheet(buttonColA)
		self.endBtn.setFont(fontA)
		self.endBtn.setText("End : ")
		snapBtn = QtWidgets.QPushButton(self)
		snapBtn.setGeometry(QtCore.QRect(0, 86, 220, 50))
		snapBtn.setStyleSheet(buttonColA)
		snapBtn.setFont(fontA)
		snapBtn.setText("Snap")
		self.minValue = cmds.playbackOptions(q=1, min=1)
		self.maxValue = cmds.playbackOptions(q=1, max=1)
		self.stBtn.clicked.connect(self.getSt)
		self.endBtn.clicked.connect(self.getEnd)
		snapBtn.clicked.connect(self.exct)

	def getSt(self):
		self.minValue = cmds.currentTime(q=True)
		self.stBtn.setText("Start : " + str(int(self.minValue)))

	def getEnd(self):
		self.maxValue = cmds.currentTime(q=True)
		self.endBtn.setText("End : " + str(int(self.maxValue)))

	def exct(self):
		self.snapCtrlToWorld(self.minValue, self.maxValue)

	def snapToObj(self, myObj):
		myLoc = cmds.spaceLocator()
		cmds.setAttr(myLoc[0]+'.localScaleX',10)
		cmds.setAttr(myLoc[0]+'.localScaleY',10)
		cmds.setAttr(myLoc[0]+'.localScaleZ',10)
		if self.conCmb.currentText() == "Translate":
			parConst = cmds.pointConstraint(myObj, myLoc, mo=False)
		elif self.conCmb.currentText() == "Rotate":
			parConst = cmds.orientConstraint(myObj, myLoc, mo=False)
		else:
			parConst = cmds.parentConstraint(myObj, myLoc, mo=False)
		cmds.delete(parConst)
		return myLoc

	def snapSelection(self, myMast, mySlave):
		if self.conCmb.currentText() == "Translate":
			parConst = cmds.pointConstraint(myMast, mySlave, mo=False)
		elif self.conCmb.currentText() == "Rotate":
			parConst = cmds.orientConstraint(myMast, mySlave, mo=False)
		else:
			parConst = cmds.parentConstraint(myMast, mySlave, mo=False)
		cmds.setKeyframe(mySlave)
		cmds.delete(parConst)

	def snapCtrlToWorld(self, minValue, maxValue):
		with undoCheck():
			myCtrl = cmds.ls(sl=True)
			if (minValue<maxValue):
				if self.dirChk.isChecked() == False:
					currentT = minValue
					cmds.currentTime(currentT)
					myLoc = self.snapToObj(myCtrl)
					nextFrame = currentT + 1
					cmds.refresh(suspend=1)
					while (nextFrame <= maxValue):
						cmds.currentTime(nextFrame)
						self.snapSelection(myLoc, myCtrl)
						currentT = cmds.currentTime(q=True)
						nextFrame = currentT + 1
					cmds.refresh(suspend=0)
					cmds.delete(myLoc)
					cmds.select(myCtrl)
				else:
					currentT = maxValue
					cmds.currentTime(currentT)
					myLoc = self.snapToObj(myCtrl)
					nextFrame = currentT - 1
					cmds.refresh(suspend=1)
					while (nextFrame >= minValue):
						cmds.currentTime(nextFrame)
						self.snapSelection(myLoc, myCtrl)
						currentT = cmds.currentTime(q=True)
						nextFrame = currentT - 1
					cmds.refresh(suspend=0)
					cmds.delete(myLoc)
					cmds.select(myCtrl)
			else:
				cmds.confirmDialog(t="Notice", m="Range Error")

def app():
	global myWindow
	try:
		myWindow.close()
	except:
		pass
	myWindow = Window()
	myWindow.show()
	return myWindow

if __name__ == '__main__':
	app()