# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainWindow.ui'
#
# Created: Tue Dec 26 22:57:29 2017
#      by: pyside-uic 0.2.13 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(766, 565)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ModeSwitcher = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ModeSwitcher.sizePolicy().hasHeightForWidth())
        self.ModeSwitcher.setSizePolicy(sizePolicy)
        self.ModeSwitcher.setObjectName("ModeSwitcher")
        self.StoryMode = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StoryMode.sizePolicy().hasHeightForWidth())
        self.StoryMode.setSizePolicy(sizePolicy)
        self.StoryMode.setObjectName("StoryMode")
        self.verticalLayout = QtGui.QVBoxLayout(self.StoryMode)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.StoryMode_Text = QtGui.QTextBrowser(self.StoryMode)
        self.StoryMode_Text.setObjectName("StoryMode_Text")
        self.verticalLayout.addWidget(self.StoryMode_Text)
        self.StoryMode_Input = QtGui.QPlainTextEdit(self.StoryMode)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StoryMode_Input.sizePolicy().hasHeightForWidth())
        self.StoryMode_Input.setSizePolicy(sizePolicy)
        self.StoryMode_Input.setMinimumSize(QtCore.QSize(0, 100))
        self.StoryMode_Input.setMaximumSize(QtCore.QSize(16777215, 50))
        self.StoryMode_Input.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.StoryMode_Input.setAcceptDrops(False)
        self.StoryMode_Input.setUndoRedoEnabled(False)
        self.StoryMode_Input.setTextInteractionFlags(QtCore.Qt.TextEditable)
        self.StoryMode_Input.setObjectName("StoryMode_Input")
        self.verticalLayout.addWidget(self.StoryMode_Input)
        self.ModeSwitcher.addTab(self.StoryMode, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.ModeSwitcher.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.ModeSwitcher, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 766, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.ModeSwitcher.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.ModeSwitcher.setTabText(self.ModeSwitcher.indexOf(self.StoryMode), QtGui.QApplication.translate("MainWindow", "Story", None, QtGui.QApplication.UnicodeUTF8))
        self.ModeSwitcher.setTabText(self.ModeSwitcher.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))

