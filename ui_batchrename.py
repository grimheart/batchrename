# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'batchrename.ui'
#
# Created: Mon Mar  3 04:23:43 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_BatchRename(object):
    def setupUi(self, BatchRename):
        BatchRename.setObjectName(_fromUtf8("BatchRename"))
        BatchRename.resize(989, 689)
        BatchRename.setMinimumSize(QtCore.QSize(989, 689))
        BatchRename.setMaximumSize(QtCore.QSize(989, 689))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        BatchRename.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri,Bitstream Vera Sans,Sans,sans-serif"))
        BatchRename.setFont(font)
        BatchRename.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../home/nn/.designer/backup/icon16.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BatchRename.setWindowIcon(icon)
        BatchRename.setAutoFillBackground(False)
        BatchRename.setStyleSheet(_fromUtf8("#BatchRename {\n"
"    background-color: #454545;\n"
"    font-family: Calibri, Bitstream Vera Sans, Sans, sans-serif;\n"
"}\n"
"\n"
"#exitGroup {\n"
"    background-image: url(./xquit.png);\n"
"}\n"
"#directoryUp {\n"
"    background-image: url(./arrow-up.png);\n"
"}\n"
"#directoryUpGroup {\n"
"    background-color: #bfbfe2;\n"
"    border-radius: 2px;\n"
"}\n"
"#directoryBack {\n"
"    background-image: url(./arrow-back.png);\n"
"}\n"
"#directoryBackGroup {\n"
"    background-color: #bfbfe2;\n"
"    border-radius: 2px;\n"
"}\n"
"#exitButton, #directoryUp, #directoryBack {\n"
"    background-color: none;\n"
"    border: none;\n"
"}\n"
"\n"
"QWidget {\n"
"    background-color: white;\n"
"}\n"
"\n"
"#Wrapper {\n"
"    background-color: white;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QLineEdit, QComboBox {\n"
"    background-color: #6e7fd2;\n"
"    color: #FFFFFF;\n"
"    padding: 3px;\n"
"    border-style: solid;\n"
"    border-radius: 2px;\n"
"    font-family: Terminus, Consolas, \"Courier New\", monospace;\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-family: Calibri, Bitstream Vera Sans, Sans, sans-serif;\n"
"    background-color: #bfbfe2;\n"
"    color: #202050;\n"
"    padding: 5px;\n"
"    border-radius: 2px;\n"
"    font-family: Candara;\n"
"    font-weight: bold;\n"
"    font-style: normal;\n"
"    font-size: 8pt;\n"
"}\n"
"QPushButton:!enabled {\n"
"    background-color: #cfcfcf;\n"
"    color: #909090;\n"
"}\n"
"\n"
"QToolTip {\n"
"    font-family: Calibri, Bitstream Vera Sans, Sans, sans-serif;\n"
"    color: #191919;\n"
"    background-color: #ffffe0;\n"
"    border: 1px solid #454545;\n"
"    font-size: 8pt;\n"
"}\n"
"QTableWidget  {\n"
"    font-family: Terminus, Consolas, \"Courier New\", monospace;\n"
"\n"
"\n"
"}\n"
"QHeaderView {\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: white;\n"
"    border: 0px;\n"
"}\n"
"QTableCornerButton {\n"
"}\n"
"\n"
"QLabel {\n"
"    font-family: Calibri, Bitstream Vera Sans, Sans, sans-serif;\n"
"    font-weight: bold;\n"
"    color: #252525;\n"
"}"))
        self.Wrapper = QtGui.QWidget(BatchRename)
        self.Wrapper.setGeometry(QtCore.QRect(4, 4, 981, 681))
        self.Wrapper.setStyleSheet(_fromUtf8(""))
        self.Wrapper.setObjectName(_fromUtf8("Wrapper"))
        self.logo = QtGui.QWidget(self.Wrapper)
        self.logo.setGeometry(QtCore.QRect(800, 20, 141, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Candara"))
        font.setPointSize(10)
        self.logo.setFont(font)
        self.logo.setToolTip(_fromUtf8(""))
        self.logo.setStyleSheet(_fromUtf8("background-image: url(./logo.png); background-color: transparent;"))
        self.logo.setObjectName(_fromUtf8("logo"))
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.Wrapper)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 20, 741, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Candara"))
        font.setPointSize(10)
        self.horizontalLayoutWidget_3.setFont(font)
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.directoryGroup = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.directoryGroup.setMargin(0)
        self.directoryGroup.setObjectName(_fromUtf8("directoryGroup"))
        self.directoryBackGroup = QtGui.QWidget(self.horizontalLayoutWidget_3)
        self.directoryBackGroup.setMinimumSize(QtCore.QSize(25, 25))
        self.directoryBackGroup.setMaximumSize(QtCore.QSize(25, 25))
        self.directoryBackGroup.setObjectName(_fromUtf8("directoryBackGroup"))
        self.directoryBack = QtGui.QPushButton(self.directoryBackGroup)
        self.directoryBack.setEnabled(False)
        self.directoryBack.setGeometry(QtCore.QRect(0, 0, 25, 25))
        self.directoryBack.setMinimumSize(QtCore.QSize(25, 25))
        self.directoryBack.setMaximumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Candara"))
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.directoryBack.setFont(font)
        self.directoryBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.directoryBack.setStyleSheet(_fromUtf8(""))
        self.directoryBack.setText(_fromUtf8(""))
        self.directoryBack.setFlat(False)
        self.directoryBack.setObjectName(_fromUtf8("directoryBack"))
        self.directoryGroup.addWidget(self.directoryBackGroup)
        self.directoryUpGroup = QtGui.QWidget(self.horizontalLayoutWidget_3)
        self.directoryUpGroup.setMinimumSize(QtCore.QSize(25, 25))
        self.directoryUpGroup.setMaximumSize(QtCore.QSize(25, 25))
        self.directoryUpGroup.setObjectName(_fromUtf8("directoryUpGroup"))
        self.directoryUp = QtGui.QPushButton(self.directoryUpGroup)
        self.directoryUp.setEnabled(True)
        self.directoryUp.setGeometry(QtCore.QRect(0, 0, 25, 25))
        self.directoryUp.setMinimumSize(QtCore.QSize(25, 25))
        self.directoryUp.setMaximumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Candara"))
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.directoryUp.setFont(font)
        self.directoryUp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.directoryUp.setStyleSheet(_fromUtf8(""))
        self.directoryUp.setText(_fromUtf8(""))
        self.directoryUp.setFlat(False)
        self.directoryUp.setObjectName(_fromUtf8("directoryUp"))
        self.directoryGroup.addWidget(self.directoryUpGroup)
        self.directoryLabel = QtGui.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri,Bitstream Vera Sans,Sans,sans-serif"))
        font.setBold(True)
        font.setWeight(75)
        self.directoryLabel.setFont(font)
        self.directoryLabel.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.directoryLabel.setObjectName(_fromUtf8("directoryLabel"))
        self.directoryGroup.addWidget(self.directoryLabel)
        self.directoryInput = QtGui.QLineEdit(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Terminus,Consolas,Courier New,monospace"))
        self.directoryInput.setFont(font)
        self.directoryInput.setToolTip(_fromUtf8(""))
        self.directoryInput.setStyleSheet(_fromUtf8(""))
        self.directoryInput.setObjectName(_fromUtf8("directoryInput"))
        self.directoryGroup.addWidget(self.directoryInput)
        self.directoryBrowse = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Candara"))
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.directoryBrowse.setFont(font)
        self.directoryBrowse.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.directoryBrowse.setStyleSheet(_fromUtf8(""))
        self.directoryBrowse.setFlat(False)
        self.directoryBrowse.setObjectName(_fromUtf8("directoryBrowse"))
        self.directoryGroup.addWidget(self.directoryBrowse)
        self.horizontalLayoutWidget_9 = QtGui.QWidget(self.Wrapper)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(840, 590, 121, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Candara"))
        font.setPointSize(10)
        self.horizontalLayoutWidget_9.setFont(font)
        self.horizontalLayoutWidget_9.setObjectName(_fromUtf8("horizontalLayoutWidget_9"))
        self.startAtGroup = QtGui.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.startAtGroup.setMargin(0)
        self.startAtGroup.setObjectName(_fromUtf8("startAtGroup"))
        self.startAtLabel = QtGui.QLabel(self.horizontalLayoutWidget_9)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri,Bitstream Vera Sans,Sans,sans-serif"))
        font.setBold(True)
        font.setWeight(75)
        self.startAtLabel.setFont(font)
        self.startAtLabel.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.startAtLabel.setObjectName(_fromUtf8("startAtLabel"))
        self.startAtGroup.addWidget(self.startAtLabel)
        self.startAtInput = QtGui.QLineEdit(self.horizontalLayoutWidget_9)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Terminus,Consolas,Courier New,monospace"))
        self.startAtInput.setFont(font)
        self.startAtInput.setToolTip(_fromUtf8(""))
        self.startAtInput.setStyleSheet(_fromUtf8(""))
        self.startAtInput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.startAtInput.setObjectName(_fromUtf8("startAtInput"))
        self.startAtGroup.addWidget(self.startAtInput)
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.Wrapper)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(500, 590, 221, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Candara"))
        font.setPointSize(10)
        self.horizontalLayoutWidget_4.setFont(font)
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.basenameGroup = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.basenameGroup.setMargin(0)
        self.basenameGroup.setObjectName(_fromUtf8("basenameGroup"))
        self.basenameLabel = QtGui.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri,Bitstream Vera Sans,Sans,sans-serif"))
        font.setBold(True)
        font.setWeight(75)
        self.basenameLabel.setFont(font)
        self.basenameLabel.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.basenameLabel.setObjectName(_fromUtf8("basenameLabel"))
        self.basenameGroup.addWidget(self.basenameLabel)
        self.basenameInput = QtGui.QLineEdit(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Terminus,Consolas,Courier New,monospace"))
        self.basenameInput.setFont(font)
        self.basenameInput.setToolTip(_fromUtf8(""))
        self.basenameInput.setStyleSheet(_fromUtf8(""))
        self.basenameInput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.basenameInput.setObjectName(_fromUtf8("basenameInput"))
        self.basenameGroup.addWidget(self.basenameInput)
        self.horizontalLayoutWidget_6 = QtGui.QWidget(self.Wrapper)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(730, 590, 102, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Candara"))
        font.setPointSize(10)
        self.horizontalLayoutWidget_6.setFont(font)
        self.horizontalLayoutWidget_6.setObjectName(_fromUtf8("horizontalLayoutWidget_6"))
        self.paddingGroup = QtGui.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.paddingGroup.setMargin(0)
        self.paddingGroup.setObjectName(_fromUtf8("paddingGroup"))
        self.paddingLabel = QtGui.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri,Bitstream Vera Sans,Sans,sans-serif"))
        font.setBold(True)
        font.setWeight(75)
        self.paddingLabel.setFont(font)
        self.paddingLabel.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.paddingLabel.setObjectName(_fromUtf8("paddingLabel"))
        self.paddingGroup.addWidget(self.paddingLabel)
        self.paddingInput = QtGui.QLineEdit(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Terminus,Consolas,Courier New,monospace"))
        self.paddingInput.setFont(font)
        self.paddingInput.setToolTip(_fromUtf8(""))
        self.paddingInput.setStyleSheet(_fromUtf8(""))
        self.paddingInput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.paddingInput.setObjectName(_fromUtf8("paddingInput"))
        self.paddingGroup.addWidget(self.paddingInput)
        self.gridLayoutWidget = QtGui.QWidget(self.Wrapper)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 70, 981, 511))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Candara"))
        font.setPointSize(10)
        self.gridLayoutWidget.setFont(font)
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.previewGroup = QtGui.QGridLayout(self.gridLayoutWidget)
        self.previewGroup.setMargin(0)
        self.previewGroup.setObjectName(_fromUtf8("previewGroup"))
        self.previewTable = QtGui.QTableWidget(self.gridLayoutWidget)
        self.previewTable.setFrameShape(QtGui.QFrame.NoFrame)
        self.previewTable.setFrameShadow(QtGui.QFrame.Plain)
        self.previewTable.setAlternatingRowColors(True)
        self.previewTable.setShowGrid(False)
        self.previewTable.setGridStyle(QtCore.Qt.DashDotLine)
        self.previewTable.setCornerButtonEnabled(False)
        self.previewTable.setRowCount(16)
        self.previewTable.setColumnCount(2)
        self.previewTable.setObjectName(_fromUtf8("previewTable"))
        item = QtGui.QTableWidgetItem()
        self.previewTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.previewTable.setHorizontalHeaderItem(1, item)
        self.previewTable.horizontalHeader().setCascadingSectionResizes(False)
        self.previewTable.horizontalHeader().setDefaultSectionSize(200)
        self.previewTable.horizontalHeader().setHighlightSections(False)
        self.previewTable.horizontalHeader().setSortIndicatorShown(False)
        self.previewTable.horizontalHeader().setStretchLastSection(True)
        self.previewTable.verticalHeader().setVisible(False)
        self.previewTable.verticalHeader().setHighlightSections(False)
        self.previewGroup.addWidget(self.previewTable, 0, 0, 1, 1)
        self.bottomSpacer = QtGui.QFrame(self.Wrapper)
        self.bottomSpacer.setGeometry(QtCore.QRect(20, 630, 641, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Candara"))
        font.setPointSize(10)
        self.bottomSpacer.setFont(font)
        self.bottomSpacer.setFrameShape(QtGui.QFrame.HLine)
        self.bottomSpacer.setFrameShadow(QtGui.QFrame.Sunken)
        self.bottomSpacer.setObjectName(_fromUtf8("bottomSpacer"))
        self.horizontalLayoutWidget_7 = QtGui.QWidget(self.Wrapper)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(20, 590, 471, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Candara"))
        font.setPointSize(10)
        self.horizontalLayoutWidget_7.setFont(font)
        self.horizontalLayoutWidget_7.setObjectName(_fromUtf8("horizontalLayoutWidget_7"))
        self.filterGroup = QtGui.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.filterGroup.setMargin(0)
        self.filterGroup.setObjectName(_fromUtf8("filterGroup"))
        self.filterLabel = QtGui.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri,Bitstream Vera Sans,Sans,sans-serif"))
        font.setBold(True)
        font.setWeight(75)
        self.filterLabel.setFont(font)
        self.filterLabel.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.filterLabel.setObjectName(_fromUtf8("filterLabel"))
        self.filterGroup.addWidget(self.filterLabel)
        self.filterInput = QtGui.QLineEdit(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Terminus,Consolas,Courier New,monospace"))
        self.filterInput.setFont(font)
        self.filterInput.setToolTip(_fromUtf8(""))
        self.filterInput.setStyleSheet(_fromUtf8(""))
        self.filterInput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.filterInput.setObjectName(_fromUtf8("filterInput"))
        self.filterGroup.addWidget(self.filterInput)
        self.horizontalLayoutWidget_5 = QtGui.QWidget(self.Wrapper)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(670, 630, 293, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Candara"))
        font.setPointSize(10)
        self.horizontalLayoutWidget_5.setFont(font)
        self.horizontalLayoutWidget_5.setObjectName(_fromUtf8("horizontalLayoutWidget_5"))
        self.controlGroup = QtGui.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.controlGroup.setMargin(0)
        self.controlGroup.setObjectName(_fromUtf8("controlGroup"))
        self.outputButton = QtGui.QPushButton(self.horizontalLayoutWidget_5)
        self.outputButton.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Candara"))
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.outputButton.setFont(font)
        self.outputButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.outputButton.setStyleSheet(_fromUtf8(""))
        self.outputButton.setObjectName(_fromUtf8("outputButton"))
        self.controlGroup.addWidget(self.outputButton)
        self.cleanupButton = QtGui.QPushButton(self.horizontalLayoutWidget_5)
        self.cleanupButton.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Candara"))
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.cleanupButton.setFont(font)
        self.cleanupButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cleanupButton.setStyleSheet(_fromUtf8(""))
        self.cleanupButton.setObjectName(_fromUtf8("cleanupButton"))
        self.controlGroup.addWidget(self.cleanupButton)
        self.safetyToggle = QtGui.QCheckBox(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Candara"))
        font.setPointSize(8)
        self.safetyToggle.setFont(font)
        self.safetyToggle.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.safetyToggle.setChecked(True)
        self.safetyToggle.setObjectName(_fromUtf8("safetyToggle"))
        self.controlGroup.addWidget(self.safetyToggle)
        self.renameButton = QtGui.QPushButton(self.horizontalLayoutWidget_5)
        self.renameButton.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Candara"))
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.renameButton.setFont(font)
        self.renameButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.renameButton.setStyleSheet(_fromUtf8(""))
        self.renameButton.setCheckable(False)
        self.renameButton.setObjectName(_fromUtf8("renameButton"))
        self.controlGroup.addWidget(self.renameButton)
        self.exitGroup = QtGui.QWidget(self.Wrapper)
        self.exitGroup.setGeometry(QtCore.QRect(956, 0, 25, 25))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitGroup.sizePolicy().hasHeightForWidth())
        self.exitGroup.setSizePolicy(sizePolicy)
        self.exitGroup.setMinimumSize(QtCore.QSize(25, 25))
        self.exitGroup.setMaximumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        self.exitGroup.setFont(font)
        self.exitGroup.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exitGroup.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.exitGroup.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.exitGroup.setAutoFillBackground(False)
        self.exitGroup.setStyleSheet(_fromUtf8(""))
        self.exitGroup.setObjectName(_fromUtf8("exitGroup"))
        self.exitButton = QtGui.QPushButton(self.exitGroup)
        self.exitButton.setGeometry(QtCore.QRect(0, 0, 25, 25))
        self.exitButton.setStyleSheet(_fromUtf8(""))
        self.exitButton.setText(_fromUtf8(""))
        self.exitButton.setIconSize(QtCore.QSize(25, 25))
        self.exitButton.setFlat(True)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.directoryLabel.setBuddy(self.directoryInput)
        self.startAtLabel.setBuddy(self.startAtInput)
        self.basenameLabel.setBuddy(self.basenameInput)
        self.paddingLabel.setBuddy(self.paddingInput)
        self.filterLabel.setBuddy(self.filterInput)

        self.retranslateUi(BatchRename)
        QtCore.QObject.connect(self.directoryInput, QtCore.SIGNAL(_fromUtf8("editingFinished()")), BatchRename.changeDirectory)
        QtCore.QObject.connect(self.directoryBrowse, QtCore.SIGNAL(_fromUtf8("released()")), BatchRename.browseDirectory)
        QtCore.QObject.connect(self.basenameInput, QtCore.SIGNAL(_fromUtf8("editingFinished()")), BatchRename.changeBasename)
        QtCore.QObject.connect(self.renameButton, QtCore.SIGNAL(_fromUtf8("released()")), BatchRename.rename)
        QtCore.QObject.connect(self.filterInput, QtCore.SIGNAL(_fromUtf8("editingFinished()")), BatchRename.updateFilter)
        QtCore.QObject.connect(self.paddingInput, QtCore.SIGNAL(_fromUtf8("editingFinished()")), BatchRename.updatePadding)
        QtCore.QObject.connect(self.startAtInput, QtCore.SIGNAL(_fromUtf8("editingFinished()")), BatchRename.updateStart)
        QtCore.QObject.connect(self.safetyToggle, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), BatchRename.toggleSafety)
        QtCore.QObject.connect(self.outputButton, QtCore.SIGNAL(_fromUtf8("released()")), BatchRename.openOutputDir)
        QtCore.QObject.connect(self.exitButton, QtCore.SIGNAL(_fromUtf8("released()")), BatchRename.doExit)
        QtCore.QObject.connect(self.cleanupButton, QtCore.SIGNAL(_fromUtf8("released()")), BatchRename.cleanup)
        QtCore.QObject.connect(self.directoryBack, QtCore.SIGNAL(_fromUtf8("released()")), BatchRename.backDirectory)
        QtCore.QObject.connect(self.directoryUp, QtCore.SIGNAL(_fromUtf8("released()")), BatchRename.upDirectory)
        QtCore.QMetaObject.connectSlotsByName(BatchRename)
        BatchRename.setTabOrder(self.directoryInput, self.directoryBrowse)
        BatchRename.setTabOrder(self.directoryBrowse, self.filterInput)
        BatchRename.setTabOrder(self.filterInput, self.basenameInput)
        BatchRename.setTabOrder(self.basenameInput, self.paddingInput)
        BatchRename.setTabOrder(self.paddingInput, self.startAtInput)
        BatchRename.setTabOrder(self.startAtInput, self.outputButton)
        BatchRename.setTabOrder(self.outputButton, self.cleanupButton)
        BatchRename.setTabOrder(self.cleanupButton, self.safetyToggle)
        BatchRename.setTabOrder(self.safetyToggle, self.renameButton)
        BatchRename.setTabOrder(self.renameButton, self.exitButton)

    def retranslateUi(self, BatchRename):
        BatchRename.setWindowTitle(_translate("BatchRename", "studio25 Batch Renamer", None))
        self.directoryBack.setToolTip(_translate("BatchRename", "Open the folder containing the renamed files", None))
        self.directoryUp.setToolTip(_translate("BatchRename", "Open the folder containing the renamed files", None))
        self.directoryLabel.setToolTip(_translate("BatchRename", "Enter or browse for the directory containing the files to be renamed", None))
        self.directoryLabel.setText(_translate("BatchRename", "Directory:", None))
        self.directoryInput.setText(_translate("BatchRename", "/foo/bar/baz", None))
        self.directoryBrowse.setToolTip(_translate("BatchRename", "Select a target directory with the file browser", None))
        self.directoryBrowse.setText(_translate("BatchRename", "Browse ...", None))
        self.startAtLabel.setToolTip(_translate("BatchRename", "Renamed files will be numbered starting from this value", None))
        self.startAtLabel.setText(_translate("BatchRename", "Count from:", None))
        self.startAtInput.setText(_translate("BatchRename", "1", None))
        self.basenameLabel.setToolTip(_translate("BatchRename", "Select the basename for the renamed files", None))
        self.basenameLabel.setText(_translate("BatchRename", "Basename:", None))
        self.basenameInput.setText(_translate("BatchRename", "base", None))
        self.paddingLabel.setToolTip(_translate("BatchRename", "Select the number of decimal places to be padded with zeroes", None))
        self.paddingLabel.setText(_translate("BatchRename", "Zero pad:", None))
        self.paddingInput.setText(_translate("BatchRename", "3", None))
        self.previewTable.setSortingEnabled(False)
        item = self.previewTable.horizontalHeaderItem(0)
        item.setText(_translate("BatchRename", "Matching Files", None))
        item = self.previewTable.horizontalHeaderItem(1)
        item.setText(_translate("BatchRename", "Rename Preview", None))
        self.filterLabel.setToolTip(_translate("BatchRename", "Only target files matching this filter. *.ext will match any file with the given extension. Multiple space-seperate filters may be given", None))
        self.filterLabel.setText(_translate("BatchRename", "Filter:", None))
        self.filterInput.setText(_translate("BatchRename", "*.jpg *.jpeg *.png *.tif *.gif", None))
        self.outputButton.setToolTip(_translate("BatchRename", "Open the folder containing the renamed files", None))
        self.outputButton.setText(_translate("BatchRename", "Output", None))
        self.cleanupButton.setToolTip(_translate("BatchRename", "Delete any existing renamed files", None))
        self.cleanupButton.setText(_translate("BatchRename", "Cleanup", None))
        self.safetyToggle.setToolTip(_translate("BatchRename", "Enable rename operations", None))
        self.safetyToggle.setText(_translate("BatchRename", "Arm", None))
        self.renameButton.setToolTip(_translate("BatchRename", "Rename the listed targets according to the current settings. \"Arm\" must be selected", None))
        self.renameButton.setText(_translate("BatchRename", "Rename!", None))

