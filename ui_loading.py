# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'loadingJXBlOA.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc


class Ui_LoadingWindow(object):
    def setupUi(self, LoadingWindow):
        if not LoadingWindow.objectName():
            LoadingWindow.setObjectName(u"LoadingWindow")
        LoadingWindow.resize(800, 600)
        LoadingWindow.setStyleSheet(u"*{\n"
                                    "border:none;\n"
                                    "background-color:#16191d;\n"
                                    "padding:0;\n"
                                    "margin:0;\n"
                                    "color:#fff;\n"
                                    "font-family:Trebuchet MS  \n"
                                    "}\n"
                                    "\n"
                                    "QProgressBar{\n"
                                    "border: 2px solid grey; border-radius: 5px; text-align: center;\n"
                                    "}\n"
                                    "\n"
                                    "QProgressBar::chunk{\n"
                                    "\n"
                                    "}")
        self.centralwidget = QWidget(LoadingWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LoadingContainer = QWidget(self.centralwidget)
        self.LoadingContainer.setObjectName(u"LoadingContainer")
        self.verticalLayout_2 = QVBoxLayout(self.LoadingContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.LoadingSubContainerOne = QWidget(self.LoadingContainer)
        self.LoadingSubContainerOne.setObjectName(u"LoadingSubContainerOne")
        self.horizontalLayout = QHBoxLayout(self.LoadingSubContainerOne)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.progressBar = QProgressBar(self.LoadingSubContainerOne)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(500, 16777215))
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(24)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout.addWidget(self.progressBar, 0, Qt.AlignBottom)

        self.verticalLayout_2.addWidget(self.LoadingSubContainerOne)

        self.LoadingSubContainerTwo = QWidget(self.LoadingContainer)
        self.LoadingSubContainerTwo.setObjectName(u"LoadingSubContainerTwo")
        self.horizontalLayout_2 = QHBoxLayout(self.LoadingSubContainerTwo)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.loadingLabel = QLabel(self.LoadingSubContainerTwo)
        self.loadingLabel.setObjectName(u"loadingLabel")
        self.loadingLabel.setMinimumSize(QSize(400, 0))

        self.horizontalLayout_2.addWidget(
            self.loadingLabel, 0, Qt.AlignRight | Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.LoadingSubContainerTwo)

        self.verticalLayout.addWidget(self.LoadingContainer)

        LoadingWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoadingWindow)

        QMetaObject.connectSlotsByName(LoadingWindow)
    # setupUi

    def retranslateUi(self, LoadingWindow):
        LoadingWindow.setWindowTitle(QCoreApplication.translate(
            "LoadingWindow", u"MainWindow", None))
        self.loadingLabel.setText(QCoreApplication.translate(
            "LoadingWindow", u"Loading...", None))
    # retranslateUi
