# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zenTracer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ZenTracerDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(963, 527)
        self.gridLayout_5 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_5 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)
        self.cmbPackage = QtWidgets.QComboBox(self.groupBox_5)
        self.cmbPackage.setObjectName("cmbPackage")
        self.cmbPackage.addItem("")
        self.gridLayout_4.addWidget(self.cmbPackage, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.btnClassFileAdd = QtWidgets.QPushButton(self.groupBox_4)
        self.btnClassFileAdd.setMaximumSize(QtCore.QSize(120, 16777215))
        self.btnClassFileAdd.setObjectName("btnClassFileAdd")
        self.gridLayout_6.addWidget(self.btnClassFileAdd, 0, 0, 1, 1)
        self.btnClassStringAdd = QtWidgets.QPushButton(self.groupBox_4)
        self.btnClassStringAdd.setMaximumSize(QtCore.QSize(120, 16777215))
        self.btnClassStringAdd.setObjectName("btnClassStringAdd")
        self.gridLayout_6.addWidget(self.btnClassStringAdd, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_4, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txtClass = QtWidgets.QLineEdit(self.groupBox)
        self.txtClass.setObjectName("txtClass")
        self.horizontalLayout.addWidget(self.txtClass)
        self.btnClassAdd = QtWidgets.QPushButton(self.groupBox)
        self.btnClassAdd.setObjectName("btnClassAdd")
        self.horizontalLayout.addWidget(self.btnClassAdd)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.listClasses1 = QtWidgets.QListWidget(self.groupBox)
        self.listClasses1.setObjectName("listClasses1")
        self.gridLayout.addWidget(self.listClasses1, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.txtClassBreak = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtClassBreak.setObjectName("txtClassBreak")
        self.horizontalLayout_3.addWidget(self.txtClassBreak)
        self.btnClassBreakAdd = QtWidgets.QPushButton(self.groupBox_2)
        self.btnClassBreakAdd.setObjectName("btnClassBreakAdd")
        self.horizontalLayout_3.addWidget(self.btnClassBreakAdd)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.listClasses2 = QtWidgets.QListWidget(self.groupBox_2)
        self.listClasses2.setObjectName("listClasses2")
        self.gridLayout_2.addWidget(self.listClasses2, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabTracer = QtWidgets.QTableWidget(self.groupBox_3)
        self.tabTracer.setObjectName("tabTracer")
        self.tabTracer.setColumnCount(0)
        self.tabTracer.setRowCount(0)
        self.gridLayout_3.addWidget(self.tabTracer, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_3, 2, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ZenTracer"))
        self.groupBox_5.setTitle(_translate("Dialog", "进程缓存数据选择"))
        self.label_5.setText(_translate("Dialog", "进程："))
        self.cmbPackage.setItemText(0, _translate("Dialog", "选择缓存数据"))
        self.groupBox_4.setTitle(_translate("Dialog", "快捷操作"))
        self.btnClassFileAdd.setText(_translate("Dialog", "JavaFile"))
        self.btnClassStringAdd.setText(_translate("Dialog", "JavaString"))
        self.groupBox.setTitle(_translate("Dialog", "trace"))
        self.label.setText(_translate("Dialog", "类名："))
        self.btnClassAdd.setText(_translate("Dialog", "添加"))
        self.groupBox_2.setTitle(_translate("Dialog", "break"))
        self.label_3.setText(_translate("Dialog", "类名："))
        self.btnClassBreakAdd.setText(_translate("Dialog", "添加"))
        self.groupBox_3.setTitle(_translate("Dialog", "结果"))

