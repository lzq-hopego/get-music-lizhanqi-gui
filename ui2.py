# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\test2\ui2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1258, 807)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(80, 50, 1141, 671))
        self.widget.setMinimumSize(QtCore.QSize(1141, 671))
        self.widget.setStyleSheet("#widget{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00515464 rgba(85, 170, 255, 255), stop:1 rgba(245, 134, 255, 255));\n"
"border-radius:22px;}")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setStyleSheet("#frame{\n"
"border-top-left-radius:22px;\n"
"border-bottom-left-radius:22px;\n"
"background-color: rgb(255, 170, 0);\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_17 = QtWidgets.QFrame(self.frame)
        self.frame_17.setStyleSheet("#frame_17{\n"
"background-color: rgb(255, 207, 192);\n"
"border-top-left-radius:20px;\n"
"}")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_17)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.pushButton_9.setStyleSheet("border-image: url(:/image/image/圆形_round (1).png);")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_17)
        self.pushButton_10.setGeometry(QtCore.QRect(60, 10, 41, 41))
        self.pushButton_10.setStyleSheet("border-image: url(:/image/image/圆形_round.png);")
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_4.addWidget(self.frame_17)
        self.frame_18 = QtWidgets.QFrame(self.frame)
        self.frame_18.setStyleSheet("background-color: rgb(250, 176, 255);")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_18)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 20, 41, 41))
        self.pushButton_11.setStyleSheet("border-image: url(:/image/image/左-圆_left-c.png);")
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_18)
        self.pushButton_12.setGeometry(QtCore.QRect(60, 20, 41, 41))
        self.pushButton_12.setStyleSheet("border-image: url(:/image/image/右-圆_right-c.png);")
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_4.addWidget(self.frame_18)
        self.frame_19 = QtWidgets.QFrame(self.frame)
        self.frame_19.setStyleSheet("#frame_19{\n"
"background-color: rgb(196, 209, 255);\n"
"border-bottom-left-radius:20px;\n"
"}")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_4.addWidget(self.frame_19)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 8)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setStyleSheet("#frame_2{\n"
"border-top-right-radius:22px;\n"
"border-bottom-right-radius:22px;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setStyleSheet("\n"
"#frame_3{\n"
"border-top-right-radius:22px;\n"
"background-color: rgb(255, 0, 127);\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_12 = QtWidgets.QFrame(self.frame_3)
        self.frame_12.setStyleSheet("background-color: rgb(255, 210, 254);")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.comboBox = QtWidgets.QComboBox(self.frame_12)
        self.comboBox.setGeometry(QtCore.QRect(20, 10, 141, 41))
        self.comboBox.setStyleSheet("font: 16pt \"幼圆\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_7.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_3)
        self.frame_13.setStyleSheet("background-color: rgb(212, 255, 235);")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_13)
        self.lineEdit.setGeometry(QtCore.QRect(30, 10, 561, 41))
        self.lineEdit.setStyleSheet("font: 16pt \"幼圆\";")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_7.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.frame_3)
        self.frame_14.setStyleSheet("background-color: rgb(255, 245, 221);\n"
"border-top-right-radius:20px;")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 0, 211, 61))
        self.pushButton_6.setStyleSheet("font: 14pt \"幼圆\";\n"
"border-radius:4px;\n"
"border-top-right-radius:20px;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_7.addWidget(self.frame_14)
        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 6)
        self.horizontalLayout_7.setStretch(2, 2)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_15 = QtWidgets.QFrame(self.frame_4)
        self.frame_15.setStyleSheet("background-color: rgb(255, 144, 179);")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.frame_20 = QtWidgets.QFrame(self.frame_15)
        self.frame_20.setGeometry(QtCore.QRect(230, 10, 471, 510))
        self.frame_20.setMinimumSize(QtCore.QSize(471, 510))
        self.frame_20.setMaximumSize(QtCore.QSize(471, 510))
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.frame_20)
        self.label_5.setStyleSheet("font: 14pt \"幼圆\";\n"
"color: rgb(39, 255, 237);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame_20)
        self.label_6.setStyleSheet("font: 16pt \"幼圆\";\n"
"color: rgb(39, 255, 237);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.frame_20)
        self.label_7.setStyleSheet("font: 18pt \"幼圆\";\n"
"color: rgb(39, 255, 237);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.frame_20)
        self.label_8.setStyleSheet("font: 22pt \"幼圆\";\n"
"color: rgb(0, 255, 127);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.frame_20)
        self.label_9.setStyleSheet("font: 18pt \"幼圆\";\n"
"color: rgb(39, 255, 237);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.frame_20)
        self.label_10.setStyleSheet("font: 16pt \"幼圆\";\n"
"color: rgb(39, 255, 237);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.frame_20)
        self.label_11.setStyleSheet("font: 14pt \"幼圆\";\n"
"color: rgb(39, 255, 237);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_5.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.frame_15)
        self.label_12.setGeometry(QtCore.QRect(70, 50, 160, 160))
        self.label_12.setStyleSheet("border-image: url(:/image/image/5.jpg);\n"
"border-radius:80px;")
        self.label_12.setText("")
        self.label_12.setTextFormat(QtCore.Qt.AutoText)
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.listWidget_2 = QtWidgets.QListWidget(self.frame_15)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 10, 691, 501))
        self.listWidget_2.setStyleSheet("border-radius:20px;\n"
"font: 12pt \"幼圆\";")
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout_8.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.frame_4)
        self.frame_16.setStyleSheet("background-color: rgb(203, 255, 194);")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.listWidget = QtWidgets.QListWidget(self.frame_16)
        self.listWidget.setGeometry(QtCore.QRect(20, 10, 271, 501))
        self.listWidget.setStyleSheet("border-radius:20px;")
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_8.addWidget(self.frame_16)
        self.horizontalLayout_8.setStretch(0, 7)
        self.horizontalLayout_8.setStretch(1, 3)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setStyleSheet("\n"
"#frame_5{\n"
"border-bottom-right-radius:22px;\n"
"\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_6)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton.setMaximumSize(QtCore.QSize(80, 80))
        self.pushButton.setStyleSheet("border-radius:40px;\n"
"border-image: url(:/image/image/星光派对-赵希予-封面.jpg);\n"
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"color:rgb(255,255,255);\n"
"}")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignLeft)
        self.label_2 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"color:rgb(255,255,255);\n"
"}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_3.addWidget(self.frame_9)
        self.horizontalLayout_2.addWidget(self.frame_6, 0, QtCore.Qt.AlignLeft)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_10 = QtWidgets.QFrame(self.frame_7)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_2.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setStyleSheet("border-image: url(:/image/image/上一曲_go-start.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_3.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setStyleSheet("border:none;")
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/image/播放_play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_4.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_4.setStyleSheet("border-image: url(:/image/image/下一曲_go-end.png);")
        self.pushButton_4.setText("")
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_7)
        self.frame_11.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.horizontalSlider = QtWidgets.QSlider(self.frame_11)
        self.horizontalSlider.setStyleSheet("QSlider::groove:horizontal{\n"
"border:1px solid rgb(129,129,129);\n"
"height:8px;\n"
"backgroud:rgb(56,56,63);\n"
"}\n"
"QSlider::handle:horizontal{\n"
"backgroud:rgb(85,255,255);\n"
"width:4px;\n"
"}\n"
"QSlider::add-page:horizontal{\n"
"background:rgb(56,56,63);\n"
"}\n"
"QSlider::sub-page:horizontal{\n"
"background(85,255,255);\n"
"}")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_5.addWidget(self.horizontalSlider)
        self.label_4 = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.verticalLayout_3.addWidget(self.frame_11)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_7.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_7.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_7.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_7.setStyleSheet("border:none;")
        self.pushButton_7.setText("")
        self.pushButton_7.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_7.setAutoRepeatDelay(304)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_6.addWidget(self.pushButton_7)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.frame_8)
        self.horizontalSlider_2.setMaximumSize(QtCore.QSize(100, 30))
        self.horizontalSlider_2.setStyleSheet("QSlider::groove:horizontal{\n"
"border:1px solid rgb(129,129,129);\n"
"height:6px;\n"
"backgroud:rgb(56,56,63);\n"
"}\n"
"QSlider::handle:horizontal{\n"
"backgroud:rgb(85,255,255);\n"
"width:4px;\n"
"}\n"
"QSlider::add-page:horizontal{\n"
"background:rgb(56,56,63);\n"
"}\n"
"QSlider::sub-page:horizontal{\n"
"background(85,255,255);\n"
"}")
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalLayout_6.addWidget(self.horizontalSlider_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_5.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_5.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_5.setStyleSheet("border:none;")
        self.pushButton_5.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/image/cycle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_6.addWidget(self.pushButton_5)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 1)
        self.horizontalLayout_2.addWidget(self.frame_8)
        self.verticalLayout.addWidget(self.frame_5)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 8)
        self.verticalLayout.setStretch(2, 1)
        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1258, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.pushButton_9.clicked.connect(MainWindow.close)
        self.pushButton_10.clicked.connect(MainWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "音乐播放器"))
        self.pushButton_9.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>退出</p></body></html>"))
        self.pushButton_10.setToolTip(_translate("MainWindow", "<html><head/><body><p>最小化</p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "酷狗音乐"))
        self.comboBox.setItemText(1, _translate("MainWindow", "网易云"))
        self.comboBox.setItemText(2, _translate("MainWindow", "酷我音乐"))
        self.comboBox.setItemText(3, _translate("MainWindow", "QQ音乐"))
        self.comboBox.setItemText(4, _translate("MainWindow", "千千静听"))
        self.comboBox.setItemText(5, _translate("MainWindow", "咪咕音乐"))
        self.comboBox.setItemText(6, _translate("MainWindow", "51原唱"))
        self.comboBox.setItemText(7, _translate("MainWindow", "51翻唱"))
        self.comboBox.setItemText(8, _translate("MainWindow", "一听音乐"))
        self.pushButton_6.setText(_translate("MainWindow", "搜索"))
        self.label.setText(_translate("MainWindow", "星光派对"))
        self.label_2.setText(_translate("MainWindow", "赵希予"))
        self.label_3.setText(_translate("MainWindow", "00:00"))
        self.label_4.setText(_translate("MainWindow", "00:00"))
import image_rc
