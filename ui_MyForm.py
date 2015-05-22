# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Fri May 22 04:04:59 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(713, 572)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.radioButton = QtGui.QRadioButton(self.centralwidget)
        self.radioButton.setCheckable(True)
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.verticalLayout.addWidget(self.radioButton_2)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalSlider = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setProperty("value", 50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(0)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.verticalLayout.addWidget(self.horizontalSlider)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 713, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        self.dockWidget.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textEdit_2 = QtGui.QTextEdit(self.dockWidgetContents)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.gridLayout.addWidget(self.textEdit_2, 0, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget)
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName(_fromUtf8("action"))
        self.action_2 = QtGui.QAction(MainWindow)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.action_3 = QtGui.QAction(MainWindow)
        self.action_3.setObjectName(_fromUtf8("action_3"))
        self.action_4 = QtGui.QAction(MainWindow)
        self.action_4.setObjectName(_fromUtf8("action_4"))
        self.action_8 = QtGui.QAction(MainWindow)
        self.action_8.setObjectName(_fromUtf8("action_8"))
        self.action_9 = QtGui.QAction(MainWindow)
        self.action_9.setObjectName(_fromUtf8("action_9"))
        self.action_12 = QtGui.QAction(MainWindow)
        self.action_12.setObjectName(_fromUtf8("action_12"))
        self.actionTextRank = QtGui.QAction(MainWindow)
        self.actionTextRank.setObjectName(_fromUtf8("actionTextRank"))
        self.action_13 = QtGui.QAction(MainWindow)
        self.action_13.setObjectName(_fromUtf8("action_13"))
        self.action_14 = QtGui.QAction(MainWindow)
        self.action_14.setObjectName(_fromUtf8("action_14"))
        self.action_15 = QtGui.QAction(MainWindow)
        self.action_15.setObjectName(_fromUtf8("action_15"))
        self.action_16 = QtGui.QAction(MainWindow)
        self.action_16.setObjectName(_fromUtf8("action_16"))
        self.action_17 = QtGui.QAction(MainWindow)
        self.action_17.setObjectName(_fromUtf8("action_17"))
        self.action_18 = QtGui.QAction(MainWindow)
        self.action_18.setObjectName(_fromUtf8("action_18"))
        self.action_19 = QtGui.QAction(MainWindow)
        self.action_19.setObjectName(_fromUtf8("action_19"))
        self.action_20 = QtGui.QAction(MainWindow)
        self.action_20.setObjectName(_fromUtf8("action_20"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Автоматическое реферирование", None))
        self.radioButton.setText(_translate("MainWindow", "FrequencySummarizer", None))
        self.radioButton_2.setText(_translate("MainWindow", "TextRank", None))
        self.action.setText(_translate("MainWindow", "Новый проект", None))
        self.action_2.setText(_translate("MainWindow", "Открыть", None))
        self.action_3.setText(_translate("MainWindow", "Сохранить", None))
        self.action_4.setText(_translate("MainWindow", "Сохранить как", None))
        self.action_8.setText(_translate("MainWindow", "Текст", None))
        self.action_9.setText(_translate("MainWindow", "Отчет", None))
        self.action_12.setText(_translate("MainWindow", "Статистический", None))
        self.actionTextRank.setText(_translate("MainWindow", "TextRank", None))
        self.action_13.setText(_translate("MainWindow", "Машинное обучение", None))
        self.action_14.setText(_translate("MainWindow", "Нечеткая логика", None))
        self.action_15.setText(_translate("MainWindow", "Параметры автореферата", None))
        self.action_16.setText(_translate("MainWindow", "Статистика", None))
        self.action_17.setText(_translate("MainWindow", "Графы", None))
        self.action_18.setText(_translate("MainWindow", "Нечеткая логика", None))
        self.action_19.setText(_translate("MainWindow", "Машинное обучение", None))
        self.action_20.setText(_translate("MainWindow", "Новый проект", None))

