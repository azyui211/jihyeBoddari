# encoding:utf-8
# !/usr/bin/env python
# sw_shakerM.py
# author : SeokWon Choi

import maya.cmds as cmds
import random
import os
from PySide2 import QtCore, QtWidgets, QtGui

currentpath = os.path.abspath(__file__)

class undoCheck(object):
    def __enter__(self):
        cmds.undoInfo(openChunk=True)

    def __exit__(self, *exc):
        cmds.undoInfo(closeChunk=True)

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        # UI
        self.setWindowTitle("Shaker")
        self.resize(264, 328)
        self.setStyleSheet("background-color:rgb(210,210,210)")
        fontA = QtGui.QFont()
        fontA.setPointSize(10)
        fontA.setBold(True)
        fontB = QtGui.QFont()
        fontB.setPointSize(9)
        fontB.setBold(True)
        fontC = QtGui.QFont()
        fontC.setPointSize(14)
        fontC.setBold(True)
        lbColA = "QLabel{color:white;background-color:rgb(75,140,200)}"
        buttonColA = "QPushButton{color: white; background-color: rgb(75,140,200); border-radius:5px} QPushButton:hover{color: black; background-color: lightblue; border-radius:5px}"
        rangeLb = QtWidgets.QLabel(self)
        rangeLb.setGeometry(QtCore.QRect(0, 12, 264, 18))
        rangeLb.setText("  :+:   Input Range ( - / + )")
        rangeLb.setFont(fontB)
        rangeLb.setStyleSheet(lbColA)
        trxLb = QtWidgets.QLabel(self)
        trxLb.setGeometry(QtCore.QRect(7, 40, 80, 30))
        trxLb.setText("TranslateX :")
        trxLb.setFont(fontA)
        trxLb.setStyleSheet("QLabel{color:black}")
        self.trxLe = QtWidgets.QLineEdit(self)
        self.trxLe.setGeometry(QtCore.QRect(90, 42, 40, 26))
        self.trxLe.setAlignment(QtCore.Qt.AlignCenter)
        self.trxLe.setStyleSheet("QLineEdit{color:black}")
        self.trxLe.setText("0")
        rtxLb = QtWidgets.QLabel(self)
        rtxLb.setGeometry(QtCore.QRect(144, 40, 60, 30))
        rtxLb.setText("RotateX :")
        rtxLb.setFont(fontA)
        rtxLb.setStyleSheet("QLabel{color:black}")
        self.rtxLe = QtWidgets.QLineEdit(self)
        self.rtxLe.setGeometry(QtCore.QRect(207, 42, 40, 26))
        self.rtxLe.setAlignment(QtCore.Qt.AlignCenter)
        self.rtxLe.setStyleSheet("QLineEdit{color:black}")
        self.rtxLe.setText("0")
        tryLb = QtWidgets.QLabel(self)
        tryLb.setGeometry(QtCore.QRect(7, 75, 80, 30))
        tryLb.setText("TranslateY :")
        tryLb.setFont(fontA)
        tryLb.setStyleSheet("QLabel{color:black}")
        self.tryLe = QtWidgets.QLineEdit(self)
        self.tryLe.setGeometry(QtCore.QRect(90, 77, 40, 26))
        self.tryLe.setAlignment(QtCore.Qt.AlignCenter)
        self.tryLe.setStyleSheet("QLineEdit{color:black}")
        self.tryLe.setText("0")
        rtyLb = QtWidgets.QLabel(self)
        rtyLb.setGeometry(QtCore.QRect(144, 75, 60, 30))
        rtyLb.setText("RotateY :")
        rtyLb.setFont(fontA)
        rtyLb.setStyleSheet("QLabel{color:black}")
        self.rtyLe = QtWidgets.QLineEdit(self)
        self.rtyLe.setGeometry(QtCore.QRect(207, 77, 40, 26))
        self.rtyLe.setAlignment(QtCore.Qt.AlignCenter)
        self.rtyLe.setStyleSheet("QLineEdit{color:black}")
        self.rtyLe.setText("0")
        trzLb = QtWidgets.QLabel(self)
        trzLb.setGeometry(QtCore.QRect(7, 110, 80, 30))
        trzLb.setText("TranslateZ :")
        trzLb.setFont(fontA)
        trzLb.setStyleSheet("QLabel{color:black}")
        self.trzLe = QtWidgets.QLineEdit(self)
        self.trzLe.setGeometry(QtCore.QRect(90, 112, 40, 26))
        self.trzLe.setAlignment(QtCore.Qt.AlignCenter)
        self.trzLe.setStyleSheet("QLineEdit{color:black}")
        self.trzLe.setText("0")
        rtzLb = QtWidgets.QLabel(self)
        rtzLb.setGeometry(QtCore.QRect(144, 110, 60, 30))
        rtzLb.setText("RotateZ :")
        rtzLb.setFont(fontA)
        rtzLb.setStyleSheet("QLabel{color:black}")
        self.rtzLe = QtWidgets.QLineEdit(self)
        self.rtzLe.setGeometry(QtCore.QRect(207, 112, 40, 26))
        self.rtzLe.setAlignment(QtCore.Qt.AlignCenter)
        self.rtzLe.setStyleSheet("QLineEdit{color:black}")
        self.rtzLe.setText("0")
        shakeLb = QtWidgets.QLabel(self)
        shakeLb.setGeometry(QtCore.QRect(0, 154, 264, 18))
        shakeLb.setText("  :+:   Shaking Range            /      Frame Step")
        shakeLb.setFont(fontB)
        shakeLb.setStyleSheet(lbColA)
        self.stLe = QtWidgets.QLineEdit(self)
        self.stLe.setGeometry(QtCore.QRect(7, 184, 60, 26))
        self.stLe.setAlignment(QtCore.Qt.AlignCenter)
        self.stLe.setStyleSheet("QLineEdit{color:black}")
        minT = cmds.playbackOptions(q=True, min=True)
        self.stLe.setText(str(int(minT)))
        self.edLe = QtWidgets.QLineEdit(self)
        self.edLe.setGeometry(QtCore.QRect(80, 184, 60, 26))
        self.edLe.setAlignment(QtCore.Qt.AlignCenter)
        self.edLe.setStyleSheet("QLineEdit{color:black}")
        maxT = cmds.playbackOptions(q=True, max=True)
        self.edLe.setText(str(int(maxT)))
        slaLb = QtWidgets.QLabel(self)
        slaLb.setGeometry(QtCore.QRect(147, 184, 10, 30))
        slaLb.setText(" / ")
        slaLb.setFont(fontB)
        slaLb.setStyleSheet("QLabel{color:white}")
        self.spLe = QtWidgets.QLineEdit(self)
        self.spLe.setGeometry(QtCore.QRect(180, 184, 40, 26))
        self.spLe.setAlignment(QtCore.Qt.AlignCenter)
        self.spLe.setStyleSheet("QLineEdit{color:black}")
        self.spLe.setText("1")
        typeLb = QtWidgets.QLabel(self)
        typeLb.setGeometry(QtCore.QRect(7, 225, 110, 30))
        typeLb.setText("Shake Type :")
        typeLb.setFont(fontA)
        typeLb.setStyleSheet("QLabel{color:black}")
        wid = QtWidgets.QWidget(self)
        wid.setGeometry(QtCore.QRect(105,225,170,30))
        rdGrp = QtWidgets.QHBoxLayout(wid)
        self.normalRbtn = QtWidgets.QRadioButton(self)
        self.normalRbtn.setText("Random")
        self.normalRbtn.setStyleSheet("QRadioButton{color:black}")
        self.normalRbtn.setChecked(True)
        self.zigRbtn = QtWidgets.QRadioButton(self)
        self.zigRbtn.setText("Zigzag")
        self.zigRbtn.setStyleSheet("QRadioButton{color:black}")
        rdGrp.addWidget(self.normalRbtn)
        rdGrp.addWidget(self.zigRbtn)
        shakeBtn = QtWidgets.QPushButton(self)
        shakeBtn.setGeometry(QtCore.QRect(7, 275, 250, 40))
        shakeBtn.setText("Shake")
        shakeBtn.setFont(fontC)
        shakeBtn.setStyleSheet(buttonColA)
        shakeBtn.clicked.connect(self.exc)

    def getdigit(self):
        self.digitTest = [self.spLe.text(), self.edLe.text(), self.stLe.text(), self.trxLe.text(), self.tryLe.text(), self.trzLe.text(), self.rtxLe.text(), self.rtyLe.text(), self.rtzLe.text()]

    def exc(self):
        self.getdigit()
        if self.normalRbtn.isChecked() == True:
            self.shake()
        else:
            self.zig()

    def upd(self, digitTest):
        trList = list()
        rtList = list()
        for n, i in enumerate(digitTest[3:]):
            if float(i) == 0:
                pass
            else:
                if n == 0:
                    trList.append("translateX")
                elif n == 1:
                    trList.append("translateY")
                elif n == 2:
                    trList.append("translateZ")
                elif n == 3:
                    rtList.append("rotateX")
                elif n == 4:
                    rtList.append("rotateY")
                else:
                    rtList.append("rotateZ")
        return trList, rtList

    def shake(self):
        with undoCheck():
            trList, rtList = self.upd(self.digitTest)
            rangeDur = [float(self.stLe.text()), float(self.edLe.text())]
            spBy = int(self.spLe.text())
            inpDict = {"translateX":float(self.trxLe.text()), "translateY":float(self.tryLe.text()), "translateZ":float(self.trzLe.text()), "rotateX":float(self.rtxLe.text()), "rotateY":float(self.rtyLe.text()), "rotateZ":float(self.rtzLe.text())}
            trInd = {"translateX":0, "translateY":1, "translateZ":2, "rotateX":0, "rotateY":1, "rotateZ":2}
            sel = cmds.ls(sl=True)
            for i in sel:
                tr = cmds.xform(str(i), q=True, t=True)
                rt = cmds.xform(str(i), q=True, ro=True)
                for j in range(int(rangeDur[0]), int(rangeDur[1]+1), spBy):
                    if trList:
                        for k in trList:
                            if j == int(rangeDur[0]):
                                ranv = tr[trInd[k]]
                            else:
                                ranv = random.uniform(tr[trInd[k]]-inpDict[k], tr[trInd[k]]+inpDict[k])
                            cmds.setKeyframe(str(i), at=k, t=(j, j), v=ranv)
                    if rtList:
                        for r in rtList:
                            if j == int(rangeDur[0]):
                                ranv = rt[trInd[r]]
                            else:
                                ranv = random.uniform(rt[trInd[r]]-inpDict[r], rt[trInd[r]]+inpDict[r])
                            cmds.setKeyframe(str(i), at=r, t=(j, j), v=ranv)

    def zig(self):
        with undoCheck():
            trList, rtList = self.upd(self.digitTest)
            rangeDur = [float(self.stLe.text()), float(self.edLe.text())]
            spBy = int(self.spLe.text())
            inpDict = {"translateX":float(self.trxLe.text()), "translateY":float(self.tryLe.text()), "translateZ":float(self.trzLe.text()), "rotateX":float(self.rtxLe.text()), "rotateY":float(self.rtyLe.text()), "rotateZ":float(self.rtzLe.text())}
            trInd = {"translateX": 0, "translateY": 1, "translateZ": 2, "rotateX": 0, "rotateY": 1, "rotateZ": 2}
            sel = cmds.ls(sl=True)
            for i in sel:
                tr = cmds.xform(str(i), q=True, t=True)
                rt = cmds.xform(str(i), q=True, ro=True)
                dp = random.choice([-1,1])
                for j in range(int(rangeDur[0]), int(rangeDur[1]+1), spBy):
                    dp = -1*dp
                    if trList:
                        for k in trList:
                            if j == int(rangeDur[0]):
                                ranv = tr[trInd[k]]
                            else:
                                ranv = random.uniform(tr[trInd[k]], tr[trInd[k]]+(dp*inpDict[k]))
                            cmds.setKeyframe(str(i), at=k, t=(j, j), v=ranv)
                    if rtList:
                        for r in rtList:
                            if j == int(rangeDur[0]):
                                ranv = rt[trInd[r]]
                            else:
                                ranv = random.uniform(rt[trInd[r]], rt[trInd[r]]+(dp*inpDict[r]))
                            cmds.setKeyframe(str(i), at=r, t=(j, j), v=ranv)

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