# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceSbxfby.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(964, 816)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"background-color:transparent;\n"
"background:transparent;\n"
"padding:0;\n"
"margin:0;\n"
"color:#fff;\n"
"font-family:Trebuchet MS  \n"
"}\n"
"\n"
"\n"
"QComboBox{\n"
"   position: relative;\n"
"  line-height: 2;\n"
"\n"
"  border-radius: 4px;\n"
"\n"
"  letter-spacing: 1px;\n"
"  background-color: #1f232a;\n"
" color: white;\n"
"\n"
"padding-left: 5px;\n"
"padding-bottom:3px;\n"
"\n"
"\n"
"}\n"
"\n"
"QScrollBar\n"
"{\n"
"background:white;\n"
"width:10px;\n"
"border: 1px solid white;\n"
"\n"
"}\n"
"QScrollBar::handle\n"
"{\n"
"background : #1f232a;\n"
"\n"
"\n"
"}\n"
"QScrollBar::handle::pressed\n"
"{\n"
"background : #16191d;\n"
"border: 1px solid #DFCFBE;\n"
"}\n"
"\n"
"QTableWidget::item{\n"
"border: 0px;\n"
"padding-left: 2px; \n"
"}\n"
"\n"
"QLineEdit, QTextEdit {\n"
"color: rgba(255, 255, 255,1);\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"padding-top: 5px;\n"
"padding-left: 5px;\n"
"background-color: #16191d\n"
"}\n"
"\n"
"\n"
"::section{\n"
"Background-color:#16191d;\n"
""
                        "padding-left:4px\n"
"}\n"
"\n"
"#centralWidget{\n"
"background-color:#1f232a;\n"
"}\n"
"#leftMenuSubContainer{\n"
"background-color:#16191d;\n"
"}\n"
"\n"
"#leftMenuSubContainer QPushButton{\n"
"text-align:left;\n"
"padding:5px 10px;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"\n"
"#centerMenuSubContainer, #rightMenuSubContainer{\n"
"	background-color:#2c313c;\n"
"}\n"
"#frame_4, #frame_8, #popupNotificationSubContainer{\n"
"background-color:#16191d;\n"
"border-radius:10px;\n"
"}\n"
"#headerContainer, #footerContainer{\n"
"background-color:#1f232a;\n"
"}\n"
"")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.horizontalLayout = QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QWidget(self.centralWidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/white/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"margin-top:2px")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.dashboardBtn = QPushButton(self.frame_2)
        self.dashboardBtn.setObjectName(u"dashboardBtn")
        self.dashboardBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.dashboardBtn.setStyleSheet(u"background-color:#1f232a")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/white/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboardBtn.setIcon(icon1)
        self.dashboardBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.dashboardBtn)

        self.personnelBtn = QPushButton(self.frame_2)
        self.personnelBtn.setObjectName(u"personnelBtn")
        self.personnelBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/white/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.personnelBtn.setIcon(icon2)
        self.personnelBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.personnelBtn)

        self.hireBtn = QPushButton(self.frame_2)
        self.hireBtn.setObjectName(u"hireBtn")
        self.hireBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/white/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.hireBtn.setIcon(icon3)
        self.hireBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.hireBtn)

        self.reportBtn = QPushButton(self.frame_2)
        self.reportBtn.setObjectName(u"reportBtn")
        self.reportBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.reportBtn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/white/clipboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.reportBtn.setIcon(icon4)
        self.reportBtn.setIconSize(QSize(20, 24))
        self.reportBtn.setAutoRepeat(False)
        self.reportBtn.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.reportBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.settingsBtn = QPushButton(self.frame_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/white/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon5)
        self.settingsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.settingsBtn)

        self.newsBtn = QPushButton(self.frame_3)
        self.newsBtn.setObjectName(u"newsBtn")
        self.newsBtn.setMinimumSize(QSize(0, 0))
        self.newsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/white/rss.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.newsBtn.setIcon(icon6)
        self.newsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.newsBtn)

        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/white/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon7)
        self.helpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.helpBtn)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.mainBodyContainer = QWidget(self.centralWidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy1)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_12 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.headerContainer.setMaximumSize(QSize(16777215, 16777215))
        self.headerContainer.setStyleSheet(u"background-color: #16191d\n"
"\n"
"")
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(30, 30))
        self.label_5.setPixmap(QPixmap(u":/images/images/logo.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setFamily(u"Trebuchet MS")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_6.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_6)


        self.horizontalLayout_5.addWidget(self.frame_5)

        self.searchBox = QLineEdit(self.headerContainer)
        self.searchBox.setObjectName(u"searchBox")
        self.searchBox.setMaximumSize(QSize(200, 16777215))
        self.searchBox.setStyleSheet(u"border-radius: 10px;\n"
"background-color: #1f232a;\n"
"padding-bottom:5px;\n"
"")
        self.searchBox.setCursorPosition(0)
        self.searchBox.setClearButtonEnabled(False)

        self.horizontalLayout_5.addWidget(self.searchBox)

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.notificationBtn = QPushButton(self.frame_6)
        self.notificationBtn.setObjectName(u"notificationBtn")
        self.notificationBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/white/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon8)
        self.notificationBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_6.addWidget(self.notificationBtn)

        self.profileBtn = QPushButton(self.frame_6)
        self.profileBtn.setObjectName(u"profileBtn")
        self.profileBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/white/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileBtn.setIcon(icon9)
        self.profileBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.profileBtn)


        self.horizontalLayout_5.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_7)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/white/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon10)
        self.minimizeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.minimizeBtn)

        self.maximizeBtn = QPushButton(self.frame_7)
        self.maximizeBtn.setObjectName(u"maximizeBtn")
        self.maximizeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/white/maximize.svg", QSize(), QIcon.Normal, QIcon.On)
        self.maximizeBtn.setIcon(icon11)
        self.maximizeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.maximizeBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/white/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon12)
        self.closeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.closeBtn)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.headerContainer)

        self.popupNotificationContainer = QWidget(self.mainBodyContainer)
        self.popupNotificationContainer.setObjectName(u"popupNotificationContainer")
        self.popupNotificationContainer.setMaximumSize(QSize(16777215, 0))
        self.popupNotificationContainer.setStyleSheet(u"background-color: rgba(22, 25, 29, 1);\n"
" border-radius: 25px;\n"
"opacity:0.5;\n"
"margin:10px")
        self.verticalLayout_37 = QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(-1, 9, -1, -1)
        self.popupNotificationSubContainer = QWidget(self.popupNotificationContainer)
        self.popupNotificationSubContainer.setObjectName(u"popupNotificationSubContainer")
        self.popupNotificationSubContainer.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_38 = QVBoxLayout(self.popupNotificationSubContainer)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.popupNotificationLabel = QLabel(self.popupNotificationSubContainer)
        self.popupNotificationLabel.setObjectName(u"popupNotificationLabel")

        self.verticalLayout_38.addWidget(self.popupNotificationLabel, 0, Qt.AlignHCenter)


        self.verticalLayout_37.addWidget(self.popupNotificationSubContainer)


        self.verticalLayout_12.addWidget(self.popupNotificationContainer)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy2)
        self.mainBodyContent.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_9 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.mainContentContainer = QWidget(self.mainBodyContent)
        self.mainContentContainer.setObjectName(u"mainContentContainer")
        sizePolicy1.setHeightForWidth(self.mainContentContainer.sizePolicy().hasHeightForWidth())
        self.mainContentContainer.setSizePolicy(sizePolicy1)
        self.mainContentContainer.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.mainContentContainer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.centerMenuContainer = QWidget(self.mainContentContainer)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        sizePolicy.setHeightForWidth(self.centerMenuContainer.sizePolicy().hasHeightForWidth())
        self.centerMenuContainer.setSizePolicy(sizePolicy)
        self.centerMenuContainer.setMinimumSize(QSize(0, 0))
        self.centerMenuContainer.setMaximumSize(QSize(0, 16777215))
        self.formLayout = QFormLayout(self.centerMenuContainer)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(230, 0))
        self.verticalLayout_7 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.frame_4 = QFrame(self.centerMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(240, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.centerMenuLabel = QLabel(self.frame_4)
        self.centerMenuLabel.setObjectName(u"centerMenuLabel")
        self.centerMenuLabel.setStyleSheet(u"font-size: 14px;")

        self.horizontalLayout_10.addWidget(self.centerMenuLabel, 0, Qt.AlignHCenter)

        self.closeCenterMenuBtn = QPushButton(self.frame_4)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        self.closeCenterMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/white/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenuBtn.setIcon(icon13)
        self.closeCenterMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.closeCenterMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.stackedWidget = QStackedWidget(self.centerMenuSubContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_34 = QVBoxLayout(self.page_4)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.widget_13 = QWidget(self.page_4)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_33 = QVBoxLayout(self.widget_13)
        self.verticalLayout_33.setSpacing(12)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label = QLabel(self.widget_13)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Trebuchet MS")
        font1.setPointSize(10)
        self.label.setFont(font1)

        self.verticalLayout_33.addWidget(self.label, 0, Qt.AlignHCenter)

        self.githubBtn = QPushButton(self.widget_13)
        self.githubBtn.setObjectName(u"githubBtn")
        self.githubBtn.setMinimumSize(QSize(50, 50))
        self.githubBtn.setMaximumSize(QSize(50, 50))
        self.githubBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.githubBtn.setStyleSheet(u"background-color:#171515 ;\n"
"border-radius: 25%;")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/white/github.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.githubBtn.setIcon(icon14)
        self.githubBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_33.addWidget(self.githubBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_34.addWidget(self.widget_13, 0, Qt.AlignTop)

        self.widget_14 = QWidget(self.page_4)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_35 = QVBoxLayout(self.widget_14)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_7 = QLabel(self.widget_14)
        self.label_7.setObjectName(u"label_7")
        font2 = QFont()
        font2.setFamily(u"Trebuchet MS")
        font2.setBold(True)
        font2.setWeight(75)
        self.label_7.setFont(font2)

        self.verticalLayout_35.addWidget(self.label_7, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_34.addWidget(self.widget_14)

        self.stackedWidget.addWidget(self.page_4)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_9 = QVBoxLayout(self.page_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.settingsContainer = QWidget(self.page_3)
        self.settingsContainer.setObjectName(u"settingsContainer")
        self.verticalLayout_36 = QVBoxLayout(self.settingsContainer)
        self.verticalLayout_36.setSpacing(12)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_3 = QLabel(self.settingsContainer)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_36.addWidget(self.label_3)

        self.settingsFontComboBox = QComboBox(self.settingsContainer)
        self.settingsFontComboBox.addItem("")
        self.settingsFontComboBox.addItem("")
        self.settingsFontComboBox.addItem("")
        self.settingsFontComboBox.addItem("")
        self.settingsFontComboBox.setObjectName(u"settingsFontComboBox")
        self.settingsFontComboBox.setMinimumSize(QSize(0, 30))
        self.settingsFontComboBox.setStyleSheet(u"QComboBox::placeholder{\n"
"\n"
"color: white\n"
"}")

        self.verticalLayout_36.addWidget(self.settingsFontComboBox)

        self.label_12 = QLabel(self.settingsContainer)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_36.addWidget(self.label_12)

        self.settingsFormatComboBox = QComboBox(self.settingsContainer)
        self.settingsFormatComboBox.addItem("")
        self.settingsFormatComboBox.addItem("")
        self.settingsFormatComboBox.addItem("")
        self.settingsFormatComboBox.setObjectName(u"settingsFormatComboBox")
        self.settingsFormatComboBox.setMinimumSize(QSize(0, 30))

        self.verticalLayout_36.addWidget(self.settingsFormatComboBox)

        self.label_18 = QLabel(self.settingsContainer)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_36.addWidget(self.label_18)

        self.dial = QDial(self.settingsContainer)
        self.dial.setObjectName(u"dial")
        self.dial.setStyleSheet(u"::handle { color: green }")
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(50)

        self.verticalLayout_36.addWidget(self.dial)

        self.label_15 = QLabel(self.settingsContainer)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_36.addWidget(self.label_15)

        self.horizontalSlider = QSlider(self.settingsContainer)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: #16191d;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #16191d);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #16191d);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #16191d);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: "
                        "4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.horizontalSlider.setValue(40)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_36.addWidget(self.horizontalSlider)


        self.verticalLayout_9.addWidget(self.settingsContainer, 0, Qt.AlignTop)

        self.checkBox = QCheckBox(self.page_3)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_9.addWidget(self.checkBox)

        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_11 = QVBoxLayout(self.page_2)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.newsContainer = QWidget(self.page_2)
        self.newsContainer.setObjectName(u"newsContainer")

        self.verticalLayout_11.addWidget(self.newsContainer)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_7.addWidget(self.stackedWidget)


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.centerMenuSubContainer)


        self.horizontalLayout_3.addWidget(self.centerMenuContainer)

        self.stackedWidget_3 = QStackedWidget(self.mainContentContainer)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_15 = QVBoxLayout(self.page_6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_2 = QWidget(self.page_6)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_11 = QFrame(self.widget_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 20))
        self.frame_11.setMaximumSize(QSize(16777215, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_2 = QLabel(self.frame_11)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(24, 24))
        self.label_2.setPixmap(QPixmap(u":/icons/icons/white/filter.svg"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_24.addWidget(self.label_2)

        self.filterByPositionComboBox = QComboBox(self.frame_11)
        self.filterByPositionComboBox.addItem("")
        self.filterByPositionComboBox.addItem("")
        self.filterByPositionComboBox.addItem("")
        self.filterByPositionComboBox.addItem("")
        self.filterByPositionComboBox.addItem("")
        self.filterByPositionComboBox.setObjectName(u"filterByPositionComboBox")
        self.filterByPositionComboBox.setMinimumSize(QSize(150, 0))
        self.filterByPositionComboBox.setMaximumSize(QSize(16777215, 16777215))
        self.filterByPositionComboBox.setStyleSheet(u"background-color:#16191d")

        self.horizontalLayout_24.addWidget(self.filterByPositionComboBox)

        self.filterBySalaryComboBox = QComboBox(self.frame_11)
        self.filterBySalaryComboBox.addItem("")
        self.filterBySalaryComboBox.addItem("")
        self.filterBySalaryComboBox.addItem("")
        self.filterBySalaryComboBox.addItem("")
        self.filterBySalaryComboBox.addItem("")
        self.filterBySalaryComboBox.addItem("")
        self.filterBySalaryComboBox.setObjectName(u"filterBySalaryComboBox")
        self.filterBySalaryComboBox.setMinimumSize(QSize(150, 0))
        self.filterBySalaryComboBox.setStyleSheet(u"background-color:#16191d")

        self.horizontalLayout_24.addWidget(self.filterBySalaryComboBox)


        self.horizontalLayout_19.addWidget(self.frame_11)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.deleteSelectedRowsBtn = QPushButton(self.widget_5)
        self.deleteSelectedRowsBtn.setObjectName(u"deleteSelectedRowsBtn")
        self.deleteSelectedRowsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteSelectedRowsBtn.setStyleSheet(u"")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/white/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteSelectedRowsBtn.setIcon(icon15)
        self.deleteSelectedRowsBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_25.addWidget(self.deleteSelectedRowsBtn, 0, Qt.AlignRight)


        self.horizontalLayout_19.addWidget(self.widget_5)


        self.verticalLayout_15.addWidget(self.widget_2)

        self.tableWidget = QTableWidget(self.page_6)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.tableWidget.rowCount() < 10):
            self.tableWidget.setRowCount(10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"")
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_15.addWidget(self.tableWidget)

        self.stackedWidget_3.addWidget(self.page_6)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.verticalLayout_10 = QVBoxLayout(self.page_12)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_3 = QWidget(self.page_12)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(200, 30))
        self.widget_3.setMaximumSize(QSize(16777215, 30))
        self.dashboardIcon = QLabel(self.widget_3)
        self.dashboardIcon.setObjectName(u"dashboardIcon")
        self.dashboardIcon.setGeometry(QRect(30, 0, 31, 31))
        self.dashboardIcon.setPixmap(QPixmap(u":/icons/icons/white/grid.svg"))
        self.dashboardLabel = QLabel(self.widget_3)
        self.dashboardLabel.setObjectName(u"dashboardLabel")
        self.dashboardLabel.setGeometry(QRect(60, 5, 131, 21))
        font3 = QFont()
        font3.setFamily(u"Trebuchet MS")
        font3.setPointSize(16)
        self.dashboardLabel.setFont(font3)

        self.verticalLayout_10.addWidget(self.widget_3, 0, Qt.AlignHCenter)

        self.dashboardCardsContainer = QWidget(self.page_12)
        self.dashboardCardsContainer.setObjectName(u"dashboardCardsContainer")
        self.horizontalLayout_17 = QHBoxLayout(self.dashboardCardsContainer)
        self.horizontalLayout_17.setSpacing(16)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(20, 35, 20, 18)
        self.personsCardContainer = QWidget(self.dashboardCardsContainer)
        self.personsCardContainer.setObjectName(u"personsCardContainer")
        self.personsCardContainer.setAutoFillBackground(False)
        self.personsCardContainer.setStyleSheet(u"background-color:#955251;\n"
"")
        self.verticalLayout_8 = QVBoxLayout(self.personsCardContainer)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 9, -1, -1)
        self.label_16 = QLabel(self.personsCardContainer)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setPixmap(QPixmap(u":/icons/icons/white/users.svg"))

        self.verticalLayout_8.addWidget(self.label_16, 0, Qt.AlignHCenter)

        self.label_17 = QLabel(self.personsCardContainer)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_8.addWidget(self.label_17, 0, Qt.AlignHCenter)

        self.emoloyeeCounterLabel = QLabel(self.personsCardContainer)
        self.emoloyeeCounterLabel.setObjectName(u"emoloyeeCounterLabel")
        font4 = QFont()
        font4.setFamily(u"Trebuchet MS")
        font4.setPointSize(20)
        self.emoloyeeCounterLabel.setFont(font4)

        self.verticalLayout_8.addWidget(self.emoloyeeCounterLabel, 0, Qt.AlignHCenter)


        self.horizontalLayout_17.addWidget(self.personsCardContainer)

        self.avgSalaryCardContainer = QWidget(self.dashboardCardsContainer)
        self.avgSalaryCardContainer.setObjectName(u"avgSalaryCardContainer")
        self.avgSalaryCardContainer.setStyleSheet(u"background-color: #34568B")
        self.verticalLayout_20 = QVBoxLayout(self.avgSalaryCardContainer)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_10 = QLabel(self.avgSalaryCardContainer)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setPixmap(QPixmap(u":/icons/icons/white/trending-up.svg"))

        self.verticalLayout_20.addWidget(self.label_10, 0, Qt.AlignHCenter)

        self.label_22 = QLabel(self.avgSalaryCardContainer)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_20.addWidget(self.label_22, 0, Qt.AlignHCenter)

        self.averageSalaryCounterLabel = QLabel(self.avgSalaryCardContainer)
        self.averageSalaryCounterLabel.setObjectName(u"averageSalaryCounterLabel")
        self.averageSalaryCounterLabel.setFont(font4)

        self.verticalLayout_20.addWidget(self.averageSalaryCounterLabel, 0, Qt.AlignHCenter)


        self.horizontalLayout_17.addWidget(self.avgSalaryCardContainer)

        self.totalSalaryCardContainer = QWidget(self.dashboardCardsContainer)
        self.totalSalaryCardContainer.setObjectName(u"totalSalaryCardContainer")
        self.totalSalaryCardContainer.setStyleSheet(u"background-color: #009B77")
        self.verticalLayout_21 = QVBoxLayout(self.totalSalaryCardContainer)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_23 = QLabel(self.totalSalaryCardContainer)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setPixmap(QPixmap(u":/icons/icons/white/dollar-sign.svg"))

        self.verticalLayout_21.addWidget(self.label_23, 0, Qt.AlignHCenter)

        self.label_24 = QLabel(self.totalSalaryCardContainer)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_21.addWidget(self.label_24, 0, Qt.AlignHCenter)

        self.TotalSalaryCounterLabel = QLabel(self.totalSalaryCardContainer)
        self.TotalSalaryCounterLabel.setObjectName(u"TotalSalaryCounterLabel")
        self.TotalSalaryCounterLabel.setFont(font4)

        self.verticalLayout_21.addWidget(self.TotalSalaryCounterLabel, 0, Qt.AlignHCenter)


        self.horizontalLayout_17.addWidget(self.totalSalaryCardContainer)

        self.ageCardContainer = QWidget(self.dashboardCardsContainer)
        self.ageCardContainer.setObjectName(u"ageCardContainer")
        self.ageCardContainer.setStyleSheet(u"background-color: #E15D44")
        self.verticalLayout_22 = QVBoxLayout(self.ageCardContainer)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_25 = QLabel(self.ageCardContainer)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setPixmap(QPixmap(u":/icons/icons/white/battery-charging.svg"))

        self.verticalLayout_22.addWidget(self.label_25, 0, Qt.AlignHCenter)

        self.label_26 = QLabel(self.ageCardContainer)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_22.addWidget(self.label_26, 0, Qt.AlignHCenter)

        self.averageAgeCounterLabel = QLabel(self.ageCardContainer)
        self.averageAgeCounterLabel.setObjectName(u"averageAgeCounterLabel")
        self.averageAgeCounterLabel.setFont(font4)

        self.verticalLayout_22.addWidget(self.averageAgeCounterLabel, 0, Qt.AlignHCenter)


        self.horizontalLayout_17.addWidget(self.ageCardContainer)


        self.verticalLayout_10.addWidget(self.dashboardCardsContainer, 0, Qt.AlignTop)

        self.tabWidget = QTabWidget(self.page_12)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget.setStyleSheet(u"\n"
"QTabWidget::pane {\n"
"  border: 2px solid #16191d;\n"
"  top:-1px; \n"
"  background: #1f232a;\n"
"\n"
"} \n"
"\n"
"QTabBar::tab {\n"
"  background: #1f232a;; \n"
"  border: 2px solid #16191d; \n"
"  padding: 15px;\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
"  background: #16191d;; \n"
"  margin-bottom: -1px; \n"
"}")
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.plotsTab = QWidget()
        self.plotsTab.setObjectName(u"plotsTab")
        self.horizontalLayout_20 = QHBoxLayout(self.plotsTab)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.barChartContainer = QWidget(self.plotsTab)
        self.barChartContainer.setObjectName(u"barChartContainer")
        sizePolicy2.setHeightForWidth(self.barChartContainer.sizePolicy().hasHeightForWidth())
        self.barChartContainer.setSizePolicy(sizePolicy2)
        self.verticalLayout_23 = QVBoxLayout(self.barChartContainer)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")

        self.verticalLayout_23.addLayout(self.horizontalLayout_21)


        self.horizontalLayout_20.addWidget(self.barChartContainer)

        self.widget_4 = QWidget(self.plotsTab)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy2.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy2)
        self.widget_4.setStyleSheet(u"QTabWidget::pane {\n"
"  border: 1px solid #16191d;\n"
"  top:-1px; \n"
"  background: #1f232a;\n"
"\n"
"} \n"
"\n"
"QTabBar::tab {\n"
"  background: #1f232a;; \n"
"  border: 1px solid #16191d; \n"
"  padding: 15px;\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
"  background: #16191d;; \n"
"  margin-bottom: -1px; \n"
"}")
        self.verticalLayout_24 = QVBoxLayout(self.widget_4)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")

        self.verticalLayout_24.addLayout(self.horizontalLayout_23)


        self.horizontalLayout_20.addWidget(self.widget_4)

        self.tabWidget.addTab(self.plotsTab, "")
        self.tablesTab = QWidget()
        self.tablesTab.setObjectName(u"tablesTab")
        self.horizontalLayout_18 = QHBoxLayout(self.tablesTab)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.widget = QWidget(self.tablesTab)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout_22 = QHBoxLayout(self.widget)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.avgAgePositionContainer = QWidget(self.widget)
        self.avgAgePositionContainer.setObjectName(u"avgAgePositionContainer")
        self.verticalLayout_27 = QVBoxLayout(self.avgAgePositionContainer)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_27 = QLabel(self.avgAgePositionContainer)
        self.label_27.setObjectName(u"label_27")
        font5 = QFont()
        font5.setFamily(u"Trebuchet MS")
        font5.setPointSize(14)
        self.label_27.setFont(font5)

        self.verticalLayout_27.addWidget(self.label_27)

        self.avgAgePositionTable = QTableWidget(self.avgAgePositionContainer)
        if (self.avgAgePositionTable.columnCount() < 2):
            self.avgAgePositionTable.setColumnCount(2)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.avgAgePositionTable.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.avgAgePositionTable.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        if (self.avgAgePositionTable.rowCount() < 4):
            self.avgAgePositionTable.setRowCount(4)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFlags(Qt.NoItemFlags);
        self.avgAgePositionTable.setItem(0, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFlags(Qt.NoItemFlags);
        self.avgAgePositionTable.setItem(0, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFlags(Qt.NoItemFlags);
        self.avgAgePositionTable.setItem(1, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFlags(Qt.NoItemFlags);
        self.avgAgePositionTable.setItem(1, 1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFlags(Qt.NoItemFlags);
        self.avgAgePositionTable.setItem(2, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFlags(Qt.NoItemFlags);
        self.avgAgePositionTable.setItem(2, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFlags(Qt.NoItemFlags);
        self.avgAgePositionTable.setItem(3, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFlags(Qt.NoItemFlags);
        self.avgAgePositionTable.setItem(3, 1, __qtablewidgetitem16)
        self.avgAgePositionTable.setObjectName(u"avgAgePositionTable")
        self.avgAgePositionTable.setStyleSheet(u"")
        self.avgAgePositionTable.setRowCount(4)
        self.avgAgePositionTable.horizontalHeader().setStretchLastSection(True)
        self.avgAgePositionTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_27.addWidget(self.avgAgePositionTable)

        self.top3AgeTable = QTableWidget(self.avgAgePositionContainer)
        if (self.top3AgeTable.columnCount() < 2):
            self.top3AgeTable.setColumnCount(2)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.top3AgeTable.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.top3AgeTable.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        if (self.top3AgeTable.rowCount() < 3):
            self.top3AgeTable.setRowCount(3)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFlags(Qt.NoItemFlags);
        self.top3AgeTable.setItem(0, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFlags(Qt.NoItemFlags);
        self.top3AgeTable.setItem(0, 1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFlags(Qt.NoItemFlags);
        self.top3AgeTable.setItem(1, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFlags(Qt.NoItemFlags);
        self.top3AgeTable.setItem(1, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFlags(Qt.NoItemFlags);
        self.top3AgeTable.setItem(2, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFlags(Qt.NoItemFlags);
        self.top3AgeTable.setItem(2, 1, __qtablewidgetitem24)
        self.top3AgeTable.setObjectName(u"top3AgeTable")
        self.top3AgeTable.setRowCount(3)
        self.top3AgeTable.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_27.addWidget(self.top3AgeTable)


        self.horizontalLayout_22.addWidget(self.avgAgePositionContainer)

        self.salaryPositionTableContainer = QWidget(self.widget)
        self.salaryPositionTableContainer.setObjectName(u"salaryPositionTableContainer")
        sizePolicy.setHeightForWidth(self.salaryPositionTableContainer.sizePolicy().hasHeightForWidth())
        self.salaryPositionTableContainer.setSizePolicy(sizePolicy)
        self.verticalLayout_25 = QVBoxLayout(self.salaryPositionTableContainer)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_19 = QLabel(self.salaryPositionTableContainer)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font5)

        self.verticalLayout_25.addWidget(self.label_19)

        self.salaryPositionTable = QTableWidget(self.salaryPositionTableContainer)
        if (self.salaryPositionTable.columnCount() < 2):
            self.salaryPositionTable.setColumnCount(2)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.salaryPositionTable.setHorizontalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.salaryPositionTable.setHorizontalHeaderItem(1, __qtablewidgetitem26)
        if (self.salaryPositionTable.rowCount() < 4):
            self.salaryPositionTable.setRowCount(4)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem27.setFlags(Qt.NoItemFlags);
        self.salaryPositionTable.setItem(0, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem28.setFlags(Qt.NoItemFlags);
        self.salaryPositionTable.setItem(0, 1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem29.setFlags(Qt.NoItemFlags);
        self.salaryPositionTable.setItem(1, 0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem30.setFlags(Qt.NoItemFlags);
        self.salaryPositionTable.setItem(1, 1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem31.setFlags(Qt.NoItemFlags);
        self.salaryPositionTable.setItem(2, 0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem32.setFlags(Qt.NoItemFlags);
        self.salaryPositionTable.setItem(2, 1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem33.setFlags(Qt.NoItemFlags);
        self.salaryPositionTable.setItem(3, 0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem34.setFlags(Qt.NoItemFlags);
        self.salaryPositionTable.setItem(3, 1, __qtablewidgetitem34)
        self.salaryPositionTable.setObjectName(u"salaryPositionTable")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.salaryPositionTable.sizePolicy().hasHeightForWidth())
        self.salaryPositionTable.setSizePolicy(sizePolicy3)
        self.salaryPositionTable.setRowCount(4)
        self.salaryPositionTable.horizontalHeader().setCascadingSectionResizes(True)
        self.salaryPositionTable.horizontalHeader().setHighlightSections(False)
        self.salaryPositionTable.horizontalHeader().setStretchLastSection(True)
        self.salaryPositionTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_25.addWidget(self.salaryPositionTable)

        self.top3SalaryTable = QTableWidget(self.salaryPositionTableContainer)
        if (self.top3SalaryTable.columnCount() < 2):
            self.top3SalaryTable.setColumnCount(2)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.top3SalaryTable.setHorizontalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.top3SalaryTable.setHorizontalHeaderItem(1, __qtablewidgetitem36)
        if (self.top3SalaryTable.rowCount() < 3):
            self.top3SalaryTable.setRowCount(3)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setFlags(Qt.NoItemFlags);
        self.top3SalaryTable.setItem(0, 0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setFlags(Qt.NoItemFlags);
        self.top3SalaryTable.setItem(0, 1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFlags(Qt.NoItemFlags);
        self.top3SalaryTable.setItem(1, 0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setFlags(Qt.NoItemFlags);
        self.top3SalaryTable.setItem(1, 1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setFlags(Qt.NoItemFlags);
        self.top3SalaryTable.setItem(2, 0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setFlags(Qt.NoItemFlags);
        self.top3SalaryTable.setItem(2, 1, __qtablewidgetitem42)
        self.top3SalaryTable.setObjectName(u"top3SalaryTable")
        self.top3SalaryTable.setRowCount(3)
        self.top3SalaryTable.setColumnCount(2)
        self.top3SalaryTable.horizontalHeader().setHighlightSections(True)
        self.top3SalaryTable.horizontalHeader().setStretchLastSection(True)
        self.top3SalaryTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_25.addWidget(self.top3SalaryTable)


        self.horizontalLayout_22.addWidget(self.salaryPositionTableContainer)

        self.employeePositionTableContainer = QWidget(self.widget)
        self.employeePositionTableContainer.setObjectName(u"employeePositionTableContainer")
        sizePolicy.setHeightForWidth(self.employeePositionTableContainer.sizePolicy().hasHeightForWidth())
        self.employeePositionTableContainer.setSizePolicy(sizePolicy)
        self.verticalLayout_26 = QVBoxLayout(self.employeePositionTableContainer)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_20 = QLabel(self.employeePositionTableContainer)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font5)

        self.verticalLayout_26.addWidget(self.label_20)

        self.employeePositionTable = QTableWidget(self.employeePositionTableContainer)
        if (self.employeePositionTable.columnCount() < 2):
            self.employeePositionTable.setColumnCount(2)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.employeePositionTable.setHorizontalHeaderItem(0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setTextAlignment(Qt.AlignCenter);
        self.employeePositionTable.setHorizontalHeaderItem(1, __qtablewidgetitem44)
        if (self.employeePositionTable.rowCount() < 4):
            self.employeePositionTable.setRowCount(4)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setTextAlignment(Qt.AlignCenter);
        self.employeePositionTable.setItem(0, 0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem46.setFlags(Qt.NoItemFlags);
        self.employeePositionTable.setItem(0, 1, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem47.setFlags(Qt.NoItemFlags);
        self.employeePositionTable.setItem(1, 0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem48.setFlags(Qt.NoItemFlags);
        self.employeePositionTable.setItem(1, 1, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem49.setFlags(Qt.NoItemFlags);
        self.employeePositionTable.setItem(2, 0, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem50.setFlags(Qt.NoItemFlags);
        self.employeePositionTable.setItem(2, 1, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem51.setFlags(Qt.NoItemFlags);
        self.employeePositionTable.setItem(3, 0, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem52.setFlags(Qt.NoItemFlags);
        self.employeePositionTable.setItem(3, 1, __qtablewidgetitem52)
        self.employeePositionTable.setObjectName(u"employeePositionTable")
        self.employeePositionTable.setRowCount(4)
        self.employeePositionTable.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_26.addWidget(self.employeePositionTable)


        self.horizontalLayout_22.addWidget(self.employeePositionTableContainer)


        self.horizontalLayout_18.addWidget(self.widget)

        self.tabWidget.addTab(self.tablesTab, "")

        self.verticalLayout_10.addWidget(self.tabWidget)

        self.stackedWidget_3.addWidget(self.page_12)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_16 = QVBoxLayout(self.page_7)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.hireSectionContainer = QWidget(self.page_7)
        self.hireSectionContainer.setObjectName(u"hireSectionContainer")
        self.hireSectionContainer.setMaximumSize(QSize(1000, 16777215))
        self.verticalLayout_28 = QVBoxLayout(self.hireSectionContainer)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.hireSectionLabel = QLabel(self.hireSectionContainer)
        self.hireSectionLabel.setObjectName(u"hireSectionLabel")
        font6 = QFont()
        font6.setFamily(u"Trebuchet MS")
        font6.setPointSize(24)
        self.hireSectionLabel.setFont(font6)

        self.verticalLayout_28.addWidget(self.hireSectionLabel, 0, Qt.AlignHCenter)

        self.widget_8 = QWidget(self.hireSectionContainer)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 50))
        self.widget_8.setStyleSheet(u"")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.hireSectionNameLineEdit = QLineEdit(self.widget_8)
        self.hireSectionNameLineEdit.setObjectName(u"hireSectionNameLineEdit")
        self.hireSectionNameLineEdit.setMinimumSize(QSize(300, 40))

        self.horizontalLayout_15.addWidget(self.hireSectionNameLineEdit)

        self.hireSectionLastNameLineEdit = QLineEdit(self.widget_8)
        self.hireSectionLastNameLineEdit.setObjectName(u"hireSectionLastNameLineEdit")
        self.hireSectionLastNameLineEdit.setMinimumSize(QSize(300, 40))

        self.horizontalLayout_15.addWidget(self.hireSectionLastNameLineEdit)


        self.verticalLayout_28.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.hireSectionContainer)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 50))
        self.widget_9.setStyleSheet(u"")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.hireSectionPositionComboBox = QComboBox(self.widget_9)
        self.hireSectionPositionComboBox.addItem("")
        self.hireSectionPositionComboBox.addItem("")
        self.hireSectionPositionComboBox.addItem("")
        self.hireSectionPositionComboBox.addItem("")
        self.hireSectionPositionComboBox.setObjectName(u"hireSectionPositionComboBox")
        self.hireSectionPositionComboBox.setMinimumSize(QSize(300, 40))
        self.hireSectionPositionComboBox.setStyleSheet(u"background-color: #16191d")

        self.horizontalLayout_16.addWidget(self.hireSectionPositionComboBox)

        self.hireSectionEmailLineEdit = QLineEdit(self.widget_9)
        self.hireSectionEmailLineEdit.setObjectName(u"hireSectionEmailLineEdit")
        self.hireSectionEmailLineEdit.setMinimumSize(QSize(300, 40))

        self.horizontalLayout_16.addWidget(self.hireSectionEmailLineEdit)


        self.verticalLayout_28.addWidget(self.widget_9)

        self.widget_7 = QWidget(self.hireSectionContainer)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 50))
        self.widget_7.setStyleSheet(u"")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.hireSectionAgeSpinBox = QSpinBox(self.widget_7)
        self.hireSectionAgeSpinBox.setObjectName(u"hireSectionAgeSpinBox")
        self.hireSectionAgeSpinBox.setMinimumSize(QSize(300, 40))
        self.hireSectionAgeSpinBox.setStyleSheet(u"background-color: #16191d;\n"
"padding-left: 10px")
        self.hireSectionAgeSpinBox.setMinimum(18)
        self.hireSectionAgeSpinBox.setMaximum(70)

        self.horizontalLayout_26.addWidget(self.hireSectionAgeSpinBox)

        self.hireSectionSalarySpinBox = QSpinBox(self.widget_7)
        self.hireSectionSalarySpinBox.setObjectName(u"hireSectionSalarySpinBox")
        self.hireSectionSalarySpinBox.setMinimumSize(QSize(300, 40))
        self.hireSectionSalarySpinBox.setStyleSheet(u"background-color: #16191d;\n"
"padding-left: 10px")
        self.hireSectionSalarySpinBox.setMinimum(500)
        self.hireSectionSalarySpinBox.setMaximum(10000)

        self.horizontalLayout_26.addWidget(self.hireSectionSalarySpinBox)


        self.verticalLayout_28.addWidget(self.widget_7)

        self.widget_6 = QWidget(self.hireSectionContainer)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.hireEmployeeBtn = QPushButton(self.widget_6)
        self.hireEmployeeBtn.setObjectName(u"hireEmployeeBtn")
        self.hireEmployeeBtn.setMinimumSize(QSize(100, 30))
        self.hireEmployeeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.hireEmployeeBtn.setStyleSheet(u"background-color: #45B8AC")
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/white/user-check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.hireEmployeeBtn.setIcon(icon16)

        self.horizontalLayout_27.addWidget(self.hireEmployeeBtn, 0, Qt.AlignRight)


        self.verticalLayout_28.addWidget(self.widget_6)


        self.verticalLayout_16.addWidget(self.hireSectionContainer, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.stackedWidget_3.addWidget(self.page_7)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.verticalLayout_17 = QVBoxLayout(self.page_10)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.ganttChartContainer = QWidget(self.page_10)
        self.ganttChartContainer.setObjectName(u"ganttChartContainer")
        self.ganttChartContainer.setMinimumSize(QSize(0, 600))
        self.verticalLayout_31 = QVBoxLayout(self.ganttChartContainer)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.ganttChartVLayout = QVBoxLayout()
        self.ganttChartVLayout.setObjectName(u"ganttChartVLayout")

        self.verticalLayout_31.addLayout(self.ganttChartVLayout)


        self.verticalLayout_17.addWidget(self.ganttChartContainer)

        self.stackedWidget_3.addWidget(self.page_10)

        self.horizontalLayout_3.addWidget(self.stackedWidget_3)


        self.horizontalLayout_9.addWidget(self.mainContentContainer)

        self.rightMenuContainer = QWidget(self.mainBodyContent)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(0, 0))
        self.rightMenuContainer.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setMinimumSize(QSize(250, 0))
        self.verticalLayout_6 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_8 = QFrame(self.rightMenuSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.rightMenuLabel = QLabel(self.frame_8)
        self.rightMenuLabel.setObjectName(u"rightMenuLabel")
        self.rightMenuLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.rightMenuLabel)

        self.closeRightMenuBtn = QPushButton(self.frame_8)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        self.closeRightMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeRightMenuBtn.setIcon(icon13)
        self.closeRightMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.closeRightMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_8)

        self.stackedWidget_2 = QStackedWidget(self.rightMenuSubContainer)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_13 = QVBoxLayout(self.page_8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_10 = QWidget(self.page_8)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_29 = QVBoxLayout(self.widget_10)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.profileAvatarLabel = QLabel(self.widget_10)
        self.profileAvatarLabel.setObjectName(u"profileAvatarLabel")
        self.profileAvatarLabel.setMinimumSize(QSize(90, 90))
        self.profileAvatarLabel.setMaximumSize(QSize(90, 90))
        self.profileAvatarLabel.setPixmap(QPixmap(u":/images/images/avatar.png"))
        self.profileAvatarLabel.setScaledContents(True)

        self.verticalLayout_29.addWidget(self.profileAvatarLabel, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(0, 500))
        self.verticalLayout_30 = QVBoxLayout(self.widget_11)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.widget_12 = QWidget(self.widget_11)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(0, 150))
        self.widget_12.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_32 = QVBoxLayout(self.widget_12)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_4 = QLabel(self.widget_12)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_32.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.label_8 = QLabel(self.widget_12)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_32.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.label_11 = QLabel(self.widget_12)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_32.addWidget(self.label_11, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_2)

        self.rightMenuExitBtn = QPushButton(self.widget_12)
        self.rightMenuExitBtn.setObjectName(u"rightMenuExitBtn")
        self.rightMenuExitBtn.setMinimumSize(QSize(0, 40))
        self.rightMenuExitBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.rightMenuExitBtn.setStyleSheet(u"background-color: #9B2335;\n"
"border-radius: 20px")
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons/white/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rightMenuExitBtn.setIcon(icon17)

        self.verticalLayout_32.addWidget(self.rightMenuExitBtn)


        self.verticalLayout_30.addWidget(self.widget_12, 0, Qt.AlignTop)


        self.verticalLayout_29.addWidget(self.widget_11)


        self.verticalLayout_13.addWidget(self.widget_10)

        self.stackedWidget_2.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.verticalLayout_14 = QVBoxLayout(self.page_9)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_9 = QLabel(self.page_9)
        self.label_9.setObjectName(u"label_9")
        font7 = QFont()
        font7.setFamily(u"Trebuchet MS")
        font7.setPointSize(13)
        self.label_9.setFont(font7)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)

        self.stackedWidget_2.addWidget(self.page_9)

        self.verticalLayout_6.addWidget(self.stackedWidget_2)


        self.verticalLayout_5.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_9.addWidget(self.rightMenuContainer, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.mainBodyContent)

        self.footerContainer = QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.footerContainer.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_12 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.footerContainer)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(15, -1, -1, -1)
        self.footerLabel = QLabel(self.frame_10)
        self.footerLabel.setObjectName(u"footerLabel")

        self.horizontalLayout_13.addWidget(self.footerLabel)


        self.horizontalLayout_12.addWidget(self.frame_10)

        self.sizeGrip = QFrame(self.footerContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(10, 10))
        self.sizeGrip.setMaximumSize(QSize(40, 40))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.sizeGrip)


        self.verticalLayout_12.addWidget(self.footerContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.settingsFontComboBox.setCurrentIndex(0)
        self.settingsFormatComboBox.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.dashboardBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View Dashboard", None))
#endif // QT_CONFIG(tooltip)
        self.dashboardBtn.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
#if QT_CONFIG(tooltip)
        self.personnelBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View  Personnel", None))
#endif // QT_CONFIG(tooltip)
        self.personnelBtn.setText(QCoreApplication.translate("MainWindow", u"Personnel", None))
#if QT_CONFIG(tooltip)
        self.hireBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Data Analysis", None))
#endif // QT_CONFIG(tooltip)
        self.hireBtn.setText(QCoreApplication.translate("MainWindow", u"Hire", None))
#if QT_CONFIG(tooltip)
        self.reportBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View Reports", None))
#endif // QT_CONFIG(tooltip)
        self.reportBtn.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Go to Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.newsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View Information", None))
#endif // QT_CONFIG(tooltip)
        self.newsBtn.setText(QCoreApplication.translate("MainWindow", u"News", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Get More Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"HT Modern UI", None))
#if QT_CONFIG(tooltip)
        self.searchBox.setToolTip(QCoreApplication.translate("MainWindow", u"Search for Personnel", None))
#endif // QT_CONFIG(tooltip)
        self.searchBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Search...", None))
#if QT_CONFIG(tooltip)
        self.notificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Show Notifications", None))
#endif // QT_CONFIG(tooltip)
        self.notificationBtn.setText("")
#if QT_CONFIG(tooltip)
        self.profileBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View Profile", None))
#endif // QT_CONFIG(tooltip)
        self.profileBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize Window", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.popupNotificationLabel.setText(QCoreApplication.translate("MainWindow", u"No Notification", None))
        self.centerMenuLabel.setText(QCoreApplication.translate("MainWindow", u"More Options", None))
        self.closeCenterMenuBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"For More Projects Visit", None))
        self.githubBtn.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Version  1.0.0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Font:", None))
        self.settingsFontComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Trebuchet MS", None))
        self.settingsFontComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Arial", None))
        self.settingsFontComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Gerogia", None))
        self.settingsFontComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Comic", None))

        self.settingsFontComboBox.setPlaceholderText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Image Format:", None))
        self.settingsFormatComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u".png", None))
        self.settingsFormatComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u".jpg", None))
        self.settingsFormatComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u".svg", None))

        self.settingsFormatComboBox.setPlaceholderText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Adjust Variator: (50)", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Sound Effect: (40)", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Light Mode", None))
        self.label_2.setText("")
        self.filterByPositionComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"All Positions", None))
        self.filterByPositionComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Manager", None))
        self.filterByPositionComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Marketing Specialist", None))
        self.filterByPositionComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Software Engineer", None))
        self.filterByPositionComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Supervisor", None))

        self.filterBySalaryComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"All Salaries", None))
        self.filterBySalaryComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"<1000", None))
        self.filterBySalaryComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u">1000 And <1500", None))
        self.filterBySalaryComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u">1500 And <2000", None))
        self.filterBySalaryComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u">2000 And <2500", None))
        self.filterBySalaryComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u">2500", None))

#if QT_CONFIG(tooltip)
        self.deleteSelectedRowsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Delete Selected Employees", None))
#endif // QT_CONFIG(tooltip)
        self.deleteSelectedRowsBtn.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Employee ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Lastname", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Salary", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Position", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.dashboardIcon.setText("")
        self.dashboardLabel.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_16.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Employees", None))
        self.emoloyeeCounterLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_10.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Average Salary($)", None))
        self.averageSalaryCounterLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_23.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Total Salary($)", None))
        self.TotalSalaryCounterLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_25.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Average Age", None))
        self.averageAgeCounterLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.plotsTab), QCoreApplication.translate("MainWindow", u"Plots", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Avg Age Per Position ", None))
        ___qtablewidgetitem7 = self.avgAgePositionTable.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Positon", None));
        ___qtablewidgetitem8 = self.avgAgePositionTable.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Avg Age", None));

        __sortingEnabled = self.avgAgePositionTable.isSortingEnabled()
        self.avgAgePositionTable.setSortingEnabled(False)
        self.avgAgePositionTable.setSortingEnabled(__sortingEnabled)

        ___qtablewidgetitem9 = self.top3AgeTable.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem10 = self.top3AgeTable.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Age", None));

        __sortingEnabled1 = self.top3AgeTable.isSortingEnabled()
        self.top3AgeTable.setSortingEnabled(False)
        self.top3AgeTable.setSortingEnabled(__sortingEnabled1)

        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Salary Per Position", None))
        ___qtablewidgetitem11 = self.salaryPositionTable.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Position", None));
        ___qtablewidgetitem12 = self.salaryPositionTable.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Salary($)", None));

        __sortingEnabled2 = self.salaryPositionTable.isSortingEnabled()
        self.salaryPositionTable.setSortingEnabled(False)
        self.salaryPositionTable.setSortingEnabled(__sortingEnabled2)

        ___qtablewidgetitem13 = self.top3SalaryTable.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem14 = self.top3SalaryTable.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Salary($)", None));

        __sortingEnabled3 = self.top3SalaryTable.isSortingEnabled()
        self.top3SalaryTable.setSortingEnabled(False)
        self.top3SalaryTable.setSortingEnabled(__sortingEnabled3)

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Person Per Position", None))
        ___qtablewidgetitem15 = self.employeePositionTable.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Position", None));
        ___qtablewidgetitem16 = self.employeePositionTable.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Count", None));

        __sortingEnabled4 = self.employeePositionTable.isSortingEnabled()
        self.employeePositionTable.setSortingEnabled(False)
        self.employeePositionTable.setSortingEnabled(__sortingEnabled4)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tablesTab), QCoreApplication.translate("MainWindow", u"Tables", None))
        self.hireSectionLabel.setText(QCoreApplication.translate("MainWindow", u"Hire Employee", None))
        self.hireSectionNameLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Name", None))
        self.hireSectionLastNameLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Last Name", None))
        self.hireSectionPositionComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Software Engineer", None))
        self.hireSectionPositionComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Marketing Specialist", None))
        self.hireSectionPositionComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Supervisor", None))
        self.hireSectionPositionComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Manager", None))

        self.hireSectionEmailLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Email", None))
        self.hireSectionAgeSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" Years Old", None))
        self.hireSectionSalarySpinBox.setSuffix(QCoreApplication.translate("MainWindow", u" $", None))
        self.hireEmployeeBtn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.rightMenuLabel.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
#if QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setText("")
        self.profileAvatarLabel.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"User: Admin", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Email : mail@mail.com", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Position : Manager", None))
#if QT_CONFIG(tooltip)
        self.rightMenuExitBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Exit", None))
#endif // QT_CONFIG(tooltip)
        self.rightMenuExitBtn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"More...", None))
        self.footerLabel.setText(QCoreApplication.translate("MainWindow", u"Copyrigth Ht2", None))
    # retranslateUi

