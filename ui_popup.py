# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popupJgqKPz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_PopupWindow(object):
    def setupUi(self, PopupWindow):
        if not PopupWindow.objectName():
            PopupWindow.setObjectName(u"PopupWindow")
        PopupWindow.resize(512, 424)
        PopupWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"background-color:#16191d;\n"
"padding:0;\n"
"margin:0;\n"
"color:#fff;\n"
"font-family:Trebuchet MS  \n"
"}\n"
"\n"
"QComboBox{\n"
" position: relative;\n"
" line-height: 2;\n"
" border-radius: 2px;\n"
" border: 1px solid #DFCFBE;\n"
" letter-spacing: 1px;\n"
" background-color: #1f232a;\n"
" color: white;\n"
"padding-left: 5px;\n"
"padding-bottom:3px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"padding-left: 5px;\n"
" background-color: #1f232a\n"
" }")
        self.popupContainer = QWidget(PopupWindow)
        self.popupContainer.setObjectName(u"popupContainer")
        self.horizontalLayout = QHBoxLayout(self.popupContainer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.popupMessageContainer = QWidget(self.popupContainer)
        self.popupMessageContainer.setObjectName(u"popupMessageContainer")
        self.popupMessageContainer.setMinimumSize(QSize(450, 0))
        self.verticalLayout_2 = QVBoxLayout(self.popupMessageContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 9)
        self.popupHeaderContainer = QWidget(self.popupMessageContainer)
        self.popupHeaderContainer.setObjectName(u"popupHeaderContainer")
        self.popupHeaderContainer.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.popupHeaderContainer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.popupHeaderSubContainer = QWidget(self.popupHeaderContainer)
        self.popupHeaderSubContainer.setObjectName(u"popupHeaderSubContainer")
        self.popupHeaderSubContainer.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.popupHeaderSubContainer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.popupIconLabel = QLabel(self.popupHeaderSubContainer)
        self.popupIconLabel.setObjectName(u"popupIconLabel")
        self.popupIconLabel.setMaximumSize(QSize(24, 24))
        self.popupIconLabel.setPixmap(QPixmap(u":/icons/icons/white/alert-circle.svg"))
        self.popupIconLabel.setScaledContents(False)

        self.horizontalLayout_2.addWidget(self.popupIconLabel)

        self.popupTitleLabel = QLabel(self.popupHeaderSubContainer)
        self.popupTitleLabel.setObjectName(u"popupTitleLabel")
        self.popupTitleLabel.setMinimumSize(QSize(400, 0))

        self.horizontalLayout_2.addWidget(self.popupTitleLabel)


        self.verticalLayout_3.addWidget(self.popupHeaderSubContainer)

        self.line = QFrame(self.popupHeaderContainer)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color:#1f232a")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)


        self.verticalLayout_2.addWidget(self.popupHeaderContainer, 0, Qt.AlignTop)

        self.popupMessageSubContainer = QWidget(self.popupMessageContainer)
        self.popupMessageSubContainer.setObjectName(u"popupMessageSubContainer")
        self.popupMessageSubContainer.setMinimumSize(QSize(0, 80))
        self.popupMessageSubContainer.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.popupMessageSubContainer)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(15, -1, -1, -1)
        self.popupMessage = QLabel(self.popupMessageSubContainer)
        self.popupMessage.setObjectName(u"popupMessage")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popupMessage.sizePolicy().hasHeightForWidth())
        self.popupMessage.setSizePolicy(sizePolicy)
        self.popupMessage.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.popupMessage)


        self.verticalLayout_2.addWidget(self.popupMessageSubContainer)

        self.popupUpdateContainer = QWidget(self.popupMessageContainer)
        self.popupUpdateContainer.setObjectName(u"popupUpdateContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.popupUpdateContainer.sizePolicy().hasHeightForWidth())
        self.popupUpdateContainer.setSizePolicy(sizePolicy1)
        self.popupUpdateContainer.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.popupUpdateContainer)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.popupUpdateSubContainerComboBox = QWidget(self.popupUpdateContainer)
        self.popupUpdateSubContainerComboBox.setObjectName(u"popupUpdateSubContainerComboBox")
        sizePolicy1.setHeightForWidth(self.popupUpdateSubContainerComboBox.sizePolicy().hasHeightForWidth())
        self.popupUpdateSubContainerComboBox.setSizePolicy(sizePolicy1)
        self.verticalLayout_6 = QVBoxLayout(self.popupUpdateSubContainerComboBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.popupUpdateComboBox = QComboBox(self.popupUpdateSubContainerComboBox)
        self.popupUpdateComboBox.addItem("")
        self.popupUpdateComboBox.addItem("")
        self.popupUpdateComboBox.addItem("")
        self.popupUpdateComboBox.addItem("")
        self.popupUpdateComboBox.setObjectName(u"popupUpdateComboBox")
        self.popupUpdateComboBox.setMinimumSize(QSize(0, 30))
        self.popupUpdateComboBox.setStyleSheet(u"color:white;\n"
"background-color:#1f232a")

        self.verticalLayout_6.addWidget(self.popupUpdateComboBox)


        self.verticalLayout_5.addWidget(self.popupUpdateSubContainerComboBox)

        self.popupUpdateSubContainerQLineEdit = QWidget(self.popupUpdateContainer)
        self.popupUpdateSubContainerQLineEdit.setObjectName(u"popupUpdateSubContainerQLineEdit")
        sizePolicy1.setHeightForWidth(self.popupUpdateSubContainerQLineEdit.sizePolicy().hasHeightForWidth())
        self.popupUpdateSubContainerQLineEdit.setSizePolicy(sizePolicy1)
        self.popupUpdateSubContainerQLineEdit.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.popupUpdateSubContainerQLineEdit)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.updateNameLineEdit = QLineEdit(self.popupUpdateSubContainerQLineEdit)
        self.updateNameLineEdit.setObjectName(u"updateNameLineEdit")
        self.updateNameLineEdit.setMinimumSize(QSize(0, 30))
        self.updateNameLineEdit.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.updateNameLineEdit)


        self.verticalLayout_5.addWidget(self.popupUpdateSubContainerQLineEdit)

        self.popupUpdateSubContainerQSpinBox = QWidget(self.popupUpdateContainer)
        self.popupUpdateSubContainerQSpinBox.setObjectName(u"popupUpdateSubContainerQSpinBox")
        self.verticalLayout_7 = QVBoxLayout(self.popupUpdateSubContainerQSpinBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.updateSpinBox = QSpinBox(self.popupUpdateSubContainerQSpinBox)
        self.updateSpinBox.setObjectName(u"updateSpinBox")
        self.updateSpinBox.setMinimumSize(QSize(0, 30))
        self.updateSpinBox.setStyleSheet(u"background-color: #1f232a;\n"
"padding-left: 10px")
        self.updateSpinBox.setReadOnly(False)
        self.updateSpinBox.setMinimum(18)
        self.updateSpinBox.setMaximum(70)

        self.verticalLayout_7.addWidget(self.updateSpinBox)


        self.verticalLayout_5.addWidget(self.popupUpdateSubContainerQSpinBox)


        self.verticalLayout_2.addWidget(self.popupUpdateContainer)


        self.horizontalLayout.addWidget(self.popupMessageContainer)

        self.popupButtonsContainer = QWidget(self.popupContainer)
        self.popupButtonsContainer.setObjectName(u"popupButtonsContainer")
        self.verticalLayout = QVBoxLayout(self.popupButtonsContainer)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 0, 5, 0)
        self.popupDoneBtn = QPushButton(self.popupButtonsContainer)
        self.popupDoneBtn.setObjectName(u"popupDoneBtn")
        self.popupDoneBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.popupDoneBtn.setStyleSheet(u"background-color:#009B77")
        icon = QIcon()
        icon.addFile(u":/icons/icons/dark/check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.popupDoneBtn.setIcon(icon)
        self.popupDoneBtn.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.popupDoneBtn, 0, Qt.AlignBottom)

        self.popupCancelBtn = QPushButton(self.popupButtonsContainer)
        self.popupCancelBtn.setObjectName(u"popupCancelBtn")
        self.popupCancelBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.popupCancelBtn.setStyleSheet(u"background-color:#9B2335")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/dark/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.popupCancelBtn.setIcon(icon1)
        self.popupCancelBtn.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.popupCancelBtn, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.popupButtonsContainer)

        PopupWindow.setCentralWidget(self.popupContainer)

        self.retranslateUi(PopupWindow)

        QMetaObject.connectSlotsByName(PopupWindow)
    # setupUi

    def retranslateUi(self, PopupWindow):
        PopupWindow.setWindowTitle(QCoreApplication.translate("PopupWindow", u"MainWindow", None))
        self.popupIconLabel.setText("")
        self.popupTitleLabel.setText(QCoreApplication.translate("PopupWindow", u"TextLabel", None))
        self.popupMessage.setText(QCoreApplication.translate("PopupWindow", u"Msg", None))
        self.popupUpdateComboBox.setItemText(0, QCoreApplication.translate("PopupWindow", u"Software Engineer", None))
        self.popupUpdateComboBox.setItemText(1, QCoreApplication.translate("PopupWindow", u"Marketing Specialist", None))
        self.popupUpdateComboBox.setItemText(2, QCoreApplication.translate("PopupWindow", u"Supervisor", None))
        self.popupUpdateComboBox.setItemText(3, QCoreApplication.translate("PopupWindow", u"Manager", None))

        self.popupUpdateComboBox.setPlaceholderText("")
        self.updateNameLineEdit.setPlaceholderText(QCoreApplication.translate("PopupWindow", u"Enter", None))
        self.updateSpinBox.setSuffix("")
#if QT_CONFIG(tooltip)
        self.popupDoneBtn.setToolTip(QCoreApplication.translate("PopupWindow", u"Confirm", None))
#endif // QT_CONFIG(tooltip)
        self.popupDoneBtn.setText("")
#if QT_CONFIG(tooltip)
        self.popupCancelBtn.setToolTip(QCoreApplication.translate("PopupWindow", u"Cancle", None))
#endif // QT_CONFIG(tooltip)
        self.popupCancelBtn.setText("")
    # retranslateUi

