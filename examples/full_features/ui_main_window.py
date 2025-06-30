# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCalendarWidget, QCheckBox,
    QComboBox, QDateEdit, QDateTimeEdit, QDockWidget,
    QDoubleSpinBox, QFontComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QKeySequenceEdit,
    QLCDNumber, QLabel, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QMdiArea,
    QMenu, QMenuBar, QPlainTextEdit, QProgressBar,
    QPushButton, QRadioButton, QScrollBar, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QSplitter,
    QStackedWidget, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QTimeEdit, QToolBar,
    QToolBox, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1501, 925)
        self.actionSubmenu_2 = QAction(MainWindow)
        self.actionSubmenu_2.setObjectName(u"actionSubmenu_2")
        self.actionSubmenu_2.setCheckable(True)
        self.actionSubmenu_3 = QAction(MainWindow)
        self.actionSubmenu_3.setObjectName(u"actionSubmenu_3")
        self.actionSUBSUB = QAction(MainWindow)
        self.actionSUBSUB.setObjectName(u"actionSUBSUB")
        self.actionSUBSUB_2 = QAction(MainWindow)
        self.actionSUBSUB_2.setObjectName(u"actionSUBSUB_2")
        self.actionSUBSUB_3 = QAction(MainWindow)
        self.actionSUBSUB_3.setObjectName(u"actionSUBSUB_3")
        self.actiondissabled = QAction(MainWindow)
        self.actiondissabled.setObjectName(u"actiondissabled")
        self.actiondissabled.setEnabled(False)
        self.actionSubmenu = QAction(MainWindow)
        self.actionSubmenu.setObjectName(u"actionSubmenu")
        self.actionSubmenu.setCheckable(True)
        self.actionSubmenu.setChecked(True)
        self.actionSubmenu_4 = QAction(MainWindow)
        self.actionSubmenu_4.setObjectName(u"actionSubmenu_4")
        self.actionSubmenu_4.setCheckable(True)
        self.actionSubmenu_5 = QAction(MainWindow)
        self.actionSubmenu_5.setObjectName(u"actionSubmenu_5")
        self.actionSubmenu_5.setCheckable(True)
        self.actionSubmenu_5.setEnabled(False)
        self.actionToolbar = QAction(MainWindow)
        self.actionToolbar.setObjectName(u"actionToolbar")
        self.actionSelected = QAction(MainWindow)
        self.actionSelected.setObjectName(u"actionSelected")
        self.actionSelected.setCheckable(True)
        self.actionSelected.setChecked(True)
        self.actionaction = QAction(MainWindow)
        self.actionaction.setObjectName(u"actionaction")
        self.actionaction2 = QAction(MainWindow)
        self.actionaction2.setObjectName(u"actionaction2")
        self.actionaction3 = QAction(MainWindow)
        self.actionaction3.setObjectName(u"actionaction3")
        self.action111 = QAction(MainWindow)
        self.action111.setObjectName(u"action111")
        self.action111.setCheckable(True)
        self.action222 = QAction(MainWindow)
        self.action222.setObjectName(u"action222")
        self.action222.setCheckable(True)
        self.action333 = QAction(MainWindow)
        self.action333.setObjectName(u"action333")
        self.action333.setCheckable(True)
        self.actionsubmenu = QAction(MainWindow)
        self.actionsubmenu.setObjectName(u"actionsubmenu")
        icon = QIcon(QIcon.fromTheme(u"document-new"))
        self.actionsubmenu.setIcon(icon)
        self.actionsubmenu_2 = QAction(MainWindow)
        self.actionsubmenu_2.setObjectName(u"actionsubmenu_2")
        icon1 = QIcon(QIcon.fromTheme(u"folder"))
        self.actionsubmenu_2.setIcon(icon1)
        self.actionsubmenu_3 = QAction(MainWindow)
        self.actionsubmenu_3.setObjectName(u"actionsubmenu_3")
        icon2 = QIcon(QIcon.fromTheme(u"document-save-as"))
        self.actionsubmenu_3.setIcon(icon2)
        self.actionsubmenu_4 = QAction(MainWindow)
        self.actionsubmenu_4.setObjectName(u"actionsubmenu_4")
        icon3 = QIcon(QIcon.fromTheme(u"document-save"))
        self.actionsubmenu_4.setIcon(icon3)
        self.actionSave_all = QAction(MainWindow)
        self.actionSave_all.setObjectName(u"actionSave_all")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        icon4 = QIcon(QIcon.fromTheme(u"window-close"))
        self.actionClose.setIcon(icon4)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(0, 0, 0, 0))
        self.splitter_2.setOrientation(Qt.Orientation.Vertical)
        self.gridLayout_17 = QGridLayout(self.centralwidget)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.tabWidget_4 = QTabWidget(self.centralwidget)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.tabWidget_4.setTabPosition(QTabWidget.TabPosition.West)
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.gridLayout_11 = QGridLayout(self.tab_11)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.groupBox_2 = QGroupBox(self.tab_11)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setCheckable(True)
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setEnabled(False)

        self.gridLayout_2.addWidget(self.radioButton_3, 3, 0, 1, 1)

        self.radioButton_2 = QRadioButton(self.groupBox_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setAutoExclusive(False)

        self.gridLayout_2.addWidget(self.radioButton_2, 1, 0, 1, 1)

        self.radioButton_4 = QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setEnabled(False)
        self.radioButton_4.setChecked(False)

        self.gridLayout_2.addWidget(self.radioButton_4, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.radioButton = QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)
        self.radioButton.setAutoExclusive(False)

        self.gridLayout_2.addWidget(self.radioButton, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_2, 1, 0, 1, 2)

        self.groupBox_3 = QGroupBox(self.tab_11)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setCheckable(True)
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.checkBox_2 = QCheckBox(self.groupBox_3)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(False)

        self.gridLayout_3.addWidget(self.checkBox_2, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.checkBox = QCheckBox(self.groupBox_3)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)
        self.checkBox.setTristate(True)

        self.gridLayout_3.addWidget(self.checkBox, 0, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.groupBox_3)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setTristate(True)

        self.gridLayout_3.addWidget(self.checkBox_3, 1, 0, 1, 1)

        self.checkBox_4 = QCheckBox(self.groupBox_3)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setEnabled(False)
        self.checkBox_4.setChecked(True)

        self.gridLayout_3.addWidget(self.checkBox_4, 2, 0, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_3, 1, 2, 1, 2)

        self.groupBox = QGroupBox(self.tab_11)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setCheckable(True)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setChecked(True)

        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.groupBox)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setEnabled(False)
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setChecked(False)
        self.pushButton_6.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_6, 0, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.groupBox)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setChecked(True)
        self.pushButton_7.setFlat(False)

        self.gridLayout.addWidget(self.pushButton_7, 1, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.groupBox)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_11, 1, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.groupBox)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setChecked(False)
        self.pushButton_5.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_5, 1, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox, 0, 0, 1, 4)

        self.tabWidget_4.addTab(self.tab_11, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.gridLayout_24 = QGridLayout(self.tab_13)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton_7 = QRadioButton(self.tab_13)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setChecked(True)
        self.radioButton_7.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.radioButton_7)

        self.radioButton_5 = QRadioButton(self.tab_13)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.tab_13)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setEnabled(False)

        self.verticalLayout.addWidget(self.radioButton_6)

        self.radioButton_8 = QRadioButton(self.tab_13)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setEnabled(False)
        self.radioButton_8.setChecked(True)

        self.verticalLayout.addWidget(self.radioButton_8)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.gridLayout_24.addLayout(self.verticalLayout, 2, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_24.addItem(self.verticalSpacer_5, 1, 0, 1, 2)

        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.pushButton_2 = QPushButton(self.tab_13)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_27.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.tab_13)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setChecked(True)

        self.gridLayout_27.addWidget(self.pushButton_12, 0, 1, 1, 1)

        self.pushButton_17 = QPushButton(self.tab_13)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setEnabled(False)
        self.pushButton_17.setFlat(True)

        self.gridLayout_27.addWidget(self.pushButton_17, 2, 0, 1, 1)

        self.pushButton_14 = QPushButton(self.tab_13)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setEnabled(False)
        self.pushButton_14.setCheckable(True)
        self.pushButton_14.setChecked(True)
        self.pushButton_14.setFlat(False)

        self.gridLayout_27.addWidget(self.pushButton_14, 1, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.tab_13)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setEnabled(False)
        self.pushButton_13.setCheckable(False)
        self.pushButton_13.setChecked(False)
        self.pushButton_13.setFlat(False)

        self.gridLayout_27.addWidget(self.pushButton_13, 0, 2, 1, 1)

        self.pushButton_16 = QPushButton(self.tab_13)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setCheckable(True)
        self.pushButton_16.setChecked(False)
        self.pushButton_16.setFlat(True)

        self.gridLayout_27.addWidget(self.pushButton_16, 1, 2, 1, 1)

        self.pushButton_15 = QPushButton(self.tab_13)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setFlat(True)

        self.gridLayout_27.addWidget(self.pushButton_15, 1, 1, 1, 1)


        self.gridLayout_24.addLayout(self.gridLayout_27, 0, 0, 1, 2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox_5 = QCheckBox(self.tab_13)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setTristate(True)

        self.verticalLayout_2.addWidget(self.checkBox_5)

        self.checkBox_6 = QCheckBox(self.tab_13)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setEnabled(False)

        self.verticalLayout_2.addWidget(self.checkBox_6)

        self.checkBox_7 = QCheckBox(self.tab_13)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setEnabled(False)
        self.checkBox_7.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBox_7)

        self.checkBox_8 = QCheckBox(self.tab_13)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setChecked(True)
        self.checkBox_8.setTristate(True)

        self.verticalLayout_2.addWidget(self.checkBox_8)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)


        self.gridLayout_24.addLayout(self.verticalLayout_2, 2, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_24.addItem(self.verticalSpacer_6, 3, 0, 1, 2)

        self.tabWidget_4.addTab(self.tab_13, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.gridLayout_39 = QGridLayout(self.tab_12)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.groupBox_6 = QGroupBox(self.tab_12)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setCheckable(False)
        self.gridLayout_38 = QGridLayout(self.groupBox_6)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.pushButton_8 = QPushButton(self.groupBox_6)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_38.addWidget(self.pushButton_8, 0, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.groupBox_6)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setCheckable(True)
        self.pushButton_9.setChecked(True)

        self.gridLayout_38.addWidget(self.pushButton_9, 0, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.groupBox_6)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setEnabled(False)
        self.pushButton_10.setCheckable(False)
        self.pushButton_10.setChecked(False)
        self.pushButton_10.setFlat(False)

        self.gridLayout_38.addWidget(self.pushButton_10, 0, 2, 1, 1)

        self.pushButton_24 = QPushButton(self.groupBox_6)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setEnabled(False)
        self.pushButton_24.setCheckable(True)
        self.pushButton_24.setChecked(True)
        self.pushButton_24.setFlat(False)

        self.gridLayout_38.addWidget(self.pushButton_24, 1, 0, 1, 1)

        self.pushButton_25 = QPushButton(self.groupBox_6)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setFlat(True)

        self.gridLayout_38.addWidget(self.pushButton_25, 1, 1, 1, 1)

        self.pushButton_26 = QPushButton(self.groupBox_6)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setCheckable(True)
        self.pushButton_26.setChecked(False)
        self.pushButton_26.setFlat(True)

        self.gridLayout_38.addWidget(self.pushButton_26, 1, 2, 1, 1)

        self.pushButton_27 = QPushButton(self.groupBox_6)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setEnabled(False)
        self.pushButton_27.setFlat(True)

        self.gridLayout_38.addWidget(self.pushButton_27, 2, 0, 1, 1)


        self.gridLayout_39.addWidget(self.groupBox_6, 0, 0, 1, 2)

        self.groupBox_5 = QGroupBox(self.tab_12)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setCheckable(False)
        self.gridLayout_37 = QGridLayout(self.groupBox_5)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.radioButton_9 = QRadioButton(self.groupBox_5)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setEnabled(False)

        self.gridLayout_37.addWidget(self.radioButton_9, 3, 0, 1, 1)

        self.radioButton_10 = QRadioButton(self.groupBox_5)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setAutoExclusive(False)

        self.gridLayout_37.addWidget(self.radioButton_10, 1, 0, 1, 1)

        self.radioButton_11 = QRadioButton(self.groupBox_5)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setEnabled(False)
        self.radioButton_11.setChecked(False)

        self.gridLayout_37.addWidget(self.radioButton_11, 2, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_37.addItem(self.verticalSpacer_8, 4, 0, 1, 1)

        self.radioButton_12 = QRadioButton(self.groupBox_5)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setChecked(True)
        self.radioButton_12.setAutoExclusive(False)

        self.gridLayout_37.addWidget(self.radioButton_12, 0, 0, 1, 1)


        self.gridLayout_39.addWidget(self.groupBox_5, 1, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.tab_12)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setCheckable(False)
        self.gridLayout_36 = QGridLayout(self.groupBox_4)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.checkBox_9 = QCheckBox(self.groupBox_4)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setEnabled(False)

        self.gridLayout_36.addWidget(self.checkBox_9, 3, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_36.addItem(self.verticalSpacer_7, 4, 0, 1, 1)

        self.checkBox_10 = QCheckBox(self.groupBox_4)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setChecked(True)
        self.checkBox_10.setTristate(True)

        self.gridLayout_36.addWidget(self.checkBox_10, 0, 0, 1, 1)

        self.checkBox_11 = QCheckBox(self.groupBox_4)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setTristate(True)

        self.gridLayout_36.addWidget(self.checkBox_11, 1, 0, 1, 1)

        self.checkBox_12 = QCheckBox(self.groupBox_4)
        self.checkBox_12.setObjectName(u"checkBox_12")
        self.checkBox_12.setEnabled(False)
        self.checkBox_12.setChecked(True)

        self.gridLayout_36.addWidget(self.checkBox_12, 2, 0, 1, 1)


        self.gridLayout_39.addWidget(self.groupBox_4, 1, 1, 1, 1)

        self.tabWidget_4.addTab(self.tab_12, "")

        self.gridLayout_17.addWidget(self.tabWidget_4, 0, 0, 1, 1)

        self.tabWidget_3 = QTabWidget(self.centralwidget)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setTabPosition(QTabWidget.TabPosition.South)
        self.tabWidget_3.setDocumentMode(True)
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_16 = QGridLayout(self.tab_7)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.tabWidget = QTabWidget(self.tab_7)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setTabsClosable(True)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_6 = QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.splitter = QSplitter(self.tab_3)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.splitter_3 = QSplitter(self.frame)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Orientation.Vertical)
        self.frame_3 = QFrame(self.splitter_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_3)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.horizontalScrollBar_2 = QScrollBar(self.frame_3)
        self.horizontalScrollBar_2.setObjectName(u"horizontalScrollBar_2")
        self.horizontalScrollBar_2.setValue(50)
        self.horizontalScrollBar_2.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_12.addWidget(self.horizontalScrollBar_2, 0, 0, 1, 1)

        self.splitter_3.addWidget(self.frame_3)
        self.frame_4 = QFrame(self.splitter_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_4)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.horizontalSlider_2 = QSlider(self.frame_4)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setValue(50)
        self.horizontalSlider_2.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_15.addWidget(self.horizontalSlider_2, 0, 0, 1, 1)

        self.splitter_3.addWidget(self.frame_4)
        self.frame_5 = QFrame(self.splitter_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_5)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.progressBar_2 = QProgressBar(self.frame_5)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setValue(24)

        self.gridLayout_19.addWidget(self.progressBar_2, 0, 0, 1, 1)

        self.splitter_3.addWidget(self.frame_5)

        self.gridLayout_5.addWidget(self.splitter_3, 0, 0, 1, 1)

        self.splitter.addWidget(self.frame)
        self.frame_2 = QFrame(self.splitter)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_18 = QGridLayout(self.page_5)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.verticalScrollBar_2 = QScrollBar(self.page_5)
        self.verticalScrollBar_2.setObjectName(u"verticalScrollBar_2")
        self.verticalScrollBar_2.setValue(50)
        self.verticalScrollBar_2.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout_18.addWidget(self.verticalScrollBar_2, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(8, 108, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.verticalSlider_2 = QSlider(self.page_5)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        self.verticalSlider_2.setValue(50)
        self.verticalSlider_2.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout_18.addWidget(self.verticalSlider_2, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(32, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.stackedWidget.addWidget(self.page_6)

        self.gridLayout_13.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.splitter.addWidget(self.frame_2)

        self.gridLayout_6.addWidget(self.splitter, 0, 0, 1, 1)

        self.listWidget_2 = QListWidget(self.tab_3)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.listWidget_2.setIconSize(QSize(64, 64))
        self.listWidget_2.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.listWidget_2.setMovement(QListView.Movement.Static)
        self.listWidget_2.setFlow(QListView.Flow.TopToBottom)
        self.listWidget_2.setProperty(u"isWrapping", False)
        self.listWidget_2.setResizeMode(QListView.ResizeMode.Fixed)
        self.listWidget_2.setLayoutMode(QListView.LayoutMode.Batched)
        self.listWidget_2.setSpacing(15)
        self.listWidget_2.setViewMode(QListView.ViewMode.ListMode)
        self.listWidget_2.setSelectionRectVisible(False)
        self.listWidget_2.setSortingEnabled(True)

        self.gridLayout_6.addWidget(self.listWidget_2, 0, 2, 1, 1)

        self.treeWidget = QTreeWidget(self.tab_3)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem2 = QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        self.treeWidget.setObjectName(u"treeWidget")

        self.gridLayout_6.addWidget(self.treeWidget, 0, 1, 1, 1)

        self.tableWidget = QTableWidget(self.tab_3)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        icon5 = QIcon()
        iconThemeName = u"media-playback-start"
        if QIcon.hasThemeIcon(iconThemeName):
            icon5 = QIcon.fromTheme(iconThemeName)
        else:
            icon5.addFile(u"../../../../../../.designer/backup", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setIcon(icon5);
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setCheckState(Qt.Checked);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setCheckState(Qt.Checked);
        self.tableWidget.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setCheckState(Qt.Checked);
        __qtablewidgetitem12.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget.setItem(2, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget.setItem(2, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget.setItem(2, 2, __qtablewidgetitem14)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_6.addWidget(self.tableWidget, 0, 3, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.gridLayout_29 = QGridLayout(self.tab_15)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.widget = QWidget(self.tab_15)
        self.widget.setObjectName(u"widget")
        self.gridLayout_34 = QGridLayout(self.widget)
        self.gridLayout_34.setObjectName(u"gridLayout_34")

        self.gridLayout_29.addWidget(self.widget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_15, "")
        self.tab_16 = QWidget()
        self.tab_16.setObjectName(u"tab_16")
        self.gridLayout_30 = QGridLayout(self.tab_16)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.frame_6 = QFrame(self.tab_16)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout_30.addWidget(self.frame_6, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_16, "")
        self.tab_18 = QWidget()
        self.tab_18.setObjectName(u"tab_18")
        self.gridLayout_35 = QGridLayout(self.tab_18)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.tableWidget_2 = QTableWidget(self.tab_18)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        if (self.tableWidget_2.rowCount() < 3):
            self.tableWidget_2.setRowCount(3)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setIcon(icon5);
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setCheckState(Qt.Checked);
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setCheckState(Qt.Checked);
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setCheckState(Qt.Checked);
        __qtablewidgetitem27.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(2, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(2, 1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(2, 2, __qtablewidgetitem29)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_35.addWidget(self.tableWidget_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_18, "")
        self.tab_19 = QWidget()
        self.tab_19.setObjectName(u"tab_19")
        self.gridLayout_40 = QGridLayout(self.tab_19)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.groupBox_7 = QGroupBox(self.tab_19)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setCheckable(True)
        self.gridLayout_42 = QGridLayout(self.groupBox_7)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_41 = QGridLayout()
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.pushButton_28 = QPushButton(self.groupBox_7)
        self.pushButton_28.setObjectName(u"pushButton_28")

        self.gridLayout_41.addWidget(self.pushButton_28, 0, 0, 1, 1)

        self.pushButton_29 = QPushButton(self.groupBox_7)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setFlat(True)

        self.gridLayout_41.addWidget(self.pushButton_29, 1, 1, 1, 1)

        self.pushButton_30 = QPushButton(self.groupBox_7)
        self.pushButton_30.setObjectName(u"pushButton_30")

        self.gridLayout_41.addWidget(self.pushButton_30, 0, 2, 1, 1)

        self.pushButton_31 = QPushButton(self.groupBox_7)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setFlat(True)

        self.gridLayout_41.addWidget(self.pushButton_31, 1, 2, 1, 1)

        self.pushButton_32 = QPushButton(self.groupBox_7)
        self.pushButton_32.setObjectName(u"pushButton_32")

        self.gridLayout_41.addWidget(self.pushButton_32, 0, 1, 1, 1)

        self.pushButton_33 = QPushButton(self.groupBox_7)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setFlat(True)

        self.gridLayout_41.addWidget(self.pushButton_33, 1, 0, 1, 1)


        self.gridLayout_42.addLayout(self.gridLayout_41, 0, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_42.addItem(self.verticalSpacer_9, 1, 0, 1, 1)


        self.gridLayout_40.addWidget(self.groupBox_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_19, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_10 = QGridLayout(self.tab_6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.tabWidget_5 = QTabWidget(self.tab_6)
        self.tabWidget_5.setObjectName(u"tabWidget_5")
        self.tabWidget_5.setTabPosition(QTabWidget.TabPosition.East)
        self.tab_20 = QWidget()
        self.tab_20.setObjectName(u"tab_20")
        self.gridLayout_25 = QGridLayout(self.tab_20)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.tabWidget_6 = QTabWidget(self.tab_20)
        self.tabWidget_6.setObjectName(u"tabWidget_6")
        self.tabWidget_6.setTabPosition(QTabWidget.TabPosition.South)
        self.tab_22 = QWidget()
        self.tab_22.setObjectName(u"tab_22")
        self.gridLayout_28 = QGridLayout(self.tab_22)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.tabWidget_7 = QTabWidget(self.tab_22)
        self.tabWidget_7.setObjectName(u"tabWidget_7")
        self.tabWidget_7.setTabPosition(QTabWidget.TabPosition.West)
        self.tab_24 = QWidget()
        self.tab_24.setObjectName(u"tab_24")
        self.tabWidget_7.addTab(self.tab_24, "")
        self.tab_38 = QWidget()
        self.tab_38.setObjectName(u"tab_38")
        self.tabWidget_7.addTab(self.tab_38, "")
        self.tab_39 = QWidget()
        self.tab_39.setObjectName(u"tab_39")
        self.tabWidget_7.addTab(self.tab_39, "")
        self.tab_25 = QWidget()
        self.tab_25.setObjectName(u"tab_25")
        self.tabWidget_7.addTab(self.tab_25, "")

        self.gridLayout_28.addWidget(self.tabWidget_7, 0, 0, 1, 1)

        self.tabWidget_6.addTab(self.tab_22, "")
        self.tab_23 = QWidget()
        self.tab_23.setObjectName(u"tab_23")
        self.tabWidget_6.addTab(self.tab_23, "")
        self.tab_28 = QWidget()
        self.tab_28.setObjectName(u"tab_28")
        self.tabWidget_6.addTab(self.tab_28, "")
        self.tab_29 = QWidget()
        self.tab_29.setObjectName(u"tab_29")
        self.tabWidget_6.addTab(self.tab_29, "")
        self.tab_30 = QWidget()
        self.tab_30.setObjectName(u"tab_30")
        self.tabWidget_6.addTab(self.tab_30, "")
        self.tab_31 = QWidget()
        self.tab_31.setObjectName(u"tab_31")
        self.tabWidget_6.addTab(self.tab_31, "")
        self.tab_32 = QWidget()
        self.tab_32.setObjectName(u"tab_32")
        self.tabWidget_6.addTab(self.tab_32, "")
        self.tab_33 = QWidget()
        self.tab_33.setObjectName(u"tab_33")
        self.tabWidget_6.addTab(self.tab_33, "")
        self.tab_34 = QWidget()
        self.tab_34.setObjectName(u"tab_34")
        self.tabWidget_6.addTab(self.tab_34, "")
        self.tab_35 = QWidget()
        self.tab_35.setObjectName(u"tab_35")
        self.tabWidget_6.addTab(self.tab_35, "")
        self.tab_36 = QWidget()
        self.tab_36.setObjectName(u"tab_36")
        self.tabWidget_6.addTab(self.tab_36, "")
        self.tab_37 = QWidget()
        self.tab_37.setObjectName(u"tab_37")
        self.tabWidget_6.addTab(self.tab_37, "")

        self.gridLayout_25.addWidget(self.tabWidget_6, 0, 0, 1, 1)

        self.tabWidget_5.addTab(self.tab_20, "")
        self.tab_26 = QWidget()
        self.tab_26.setObjectName(u"tab_26")
        self.tabWidget_5.addTab(self.tab_26, "")
        self.tab_21 = QWidget()
        self.tab_21.setObjectName(u"tab_21")
        self.tabWidget_5.addTab(self.tab_21, "")
        self.tab_27 = QWidget()
        self.tab_27.setObjectName(u"tab_27")
        self.tabWidget_5.addTab(self.tab_27, "")

        self.gridLayout_10.addWidget(self.tabWidget_5, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.gridLayout_43 = QGridLayout(self.tab_14)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.comboBox_8 = QComboBox(self.tab_14)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")

        self.verticalLayout_4.addWidget(self.comboBox_8)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_10)


        self.gridLayout_43.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.fontComboBox = QFontComboBox(self.tab_14)
        self.fontComboBox.setObjectName(u"fontComboBox")

        self.verticalLayout_7.addWidget(self.fontComboBox)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_11)


        self.gridLayout_43.addLayout(self.verticalLayout_7, 0, 1, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lineEdit_5 = QLineEdit(self.tab_14)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_6.addWidget(self.lineEdit_5)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_12)


        self.gridLayout_43.addLayout(self.verticalLayout_6, 0, 2, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.spinBox_3 = QSpinBox(self.tab_14)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.verticalLayout_8.addWidget(self.spinBox_3)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_13)


        self.gridLayout_43.addLayout(self.verticalLayout_8, 0, 3, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.doubleSpinBox_3 = QDoubleSpinBox(self.tab_14)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")

        self.verticalLayout_9.addWidget(self.doubleSpinBox_3)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_14)


        self.gridLayout_43.addLayout(self.verticalLayout_9, 0, 4, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.timeEdit_2 = QTimeEdit(self.tab_14)
        self.timeEdit_2.setObjectName(u"timeEdit_2")

        self.verticalLayout_10.addWidget(self.timeEdit_2)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_15)


        self.gridLayout_43.addLayout(self.verticalLayout_10, 0, 5, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.dateEdit_2 = QDateEdit(self.tab_14)
        self.dateEdit_2.setObjectName(u"dateEdit_2")

        self.verticalLayout_11.addWidget(self.dateEdit_2)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_16)


        self.gridLayout_43.addLayout(self.verticalLayout_11, 0, 6, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.dateTimeEdit_2 = QDateTimeEdit(self.tab_14)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")

        self.verticalLayout_5.addWidget(self.dateTimeEdit_2)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_17)


        self.gridLayout_43.addLayout(self.verticalLayout_5, 0, 7, 1, 1)

        self.tabWidget.addTab(self.tab_14, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_8 = QGridLayout(self.tab_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.tabWidget.addTab(self.tab_5, "")

        self.gridLayout_16.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_7, "")
        self.tab_17 = QWidget()
        self.tab_17.setObjectName(u"tab_17")
        self.gridLayout_31 = QGridLayout(self.tab_17)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.tab_17)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_33 = QGridLayout(self.frame_7)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.line_2 = QFrame(self.frame_7)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.line_3 = QFrame(self.frame_7)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.line = QFrame(self.frame_7)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)


        self.gridLayout_33.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.line_4 = QFrame(self.frame_7)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_4)

        self.line_5 = QFrame(self.frame_7)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_5)

        self.line_6 = QFrame(self.frame_7)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_6)


        self.gridLayout_33.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.gridLayout_33.setColumnStretch(0, 1)
        self.gridLayout_33.setColumnStretch(1, 1)

        self.gridLayout_31.addWidget(self.frame_7, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_17, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_32 = QGridLayout(self.tab_8)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.tab_8)
        self.widget_2.setObjectName(u"widget_2")

        self.gridLayout_32.addWidget(self.widget_2, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.tabWidget_3.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.tabWidget_3.addTab(self.tab_10, "")

        self.gridLayout_17.addWidget(self.tabWidget_3, 2, 0, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_file_dialog = QPushButton(self.centralwidget)
        self.pushButton_file_dialog.setObjectName(u"pushButton_file_dialog")

        self.horizontalLayout_3.addWidget(self.pushButton_file_dialog)

        self.pushButton_folder_dialog = QPushButton(self.centralwidget)
        self.pushButton_folder_dialog.setObjectName(u"pushButton_folder_dialog")

        self.horizontalLayout_3.addWidget(self.pushButton_folder_dialog)


        self.gridLayout_17.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.tabWidget_2 = QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setTabPosition(QTabWidget.TabPosition.East)
        self.tabWidget_2.setTabsClosable(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_22 = QGridLayout(self.tab)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.toolBox = QToolBox(self.tab)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 537, 240))
        self.gridLayout_14 = QGridLayout(self.page)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.webEngineView = QWebEngineView(self.page)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setProperty(u"url", QUrl(u"https://www.python.org/"))

        self.gridLayout_14.addWidget(self.webEngineView, 0, 0, 1, 1)

        self.toolBox.addItem(self.page, u"WebEngine")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 537, 270))
        self.gridLayout_9 = QGridLayout(self.page_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.lcdNumber = QLCDNumber(self.page_3)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(10)
        self.lcdNumber.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.lcdNumber.setProperty(u"value", 3.141592000000000)

        self.gridLayout_9.addWidget(self.lcdNumber, 0, 2, 2, 1)

        self.timeEdit = QTimeEdit(self.page_3)
        self.timeEdit.setObjectName(u"timeEdit")

        self.gridLayout_9.addWidget(self.timeEdit, 0, 0, 1, 1)

        self.dateTimeEdit = QDateTimeEdit(self.page_3)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.gridLayout_9.addWidget(self.dateTimeEdit, 1, 0, 1, 1)

        self.dateEdit = QDateEdit(self.page_3)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setDateTime(QDateTime(QDate(1991, 2, 8), QTime(5, 0, 0)))
        self.dateEdit.setCalendarPopup(True)

        self.gridLayout_9.addWidget(self.dateEdit, 0, 1, 1, 1)

        self.keySequenceEdit = QKeySequenceEdit(self.page_3)
        self.keySequenceEdit.setObjectName(u"keySequenceEdit")

        self.gridLayout_9.addWidget(self.keySequenceEdit, 1, 1, 1, 1)

        self.calendarWidget = QCalendarWidget(self.page_3)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.gridLayout_9.addWidget(self.calendarWidget, 2, 0, 1, 3)

        self.gridLayout_9.setColumnStretch(0, 1)
        self.gridLayout_9.setColumnStretch(1, 1)
        self.gridLayout_9.setColumnStretch(2, 2)
        self.toolBox.addItem(self.page_3, u"Date controls")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 537, 396))
        self.gridLayout_21 = QGridLayout(self.page_4)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_3 = QLabel(self.page_4)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setBold(True)
        self.label_3.setFont(font)

        self.gridLayout_21.addWidget(self.label_3, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(427, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_4, 0, 3, 1, 1)

        self.label = QLabel(self.page_4)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)

        self.gridLayout_21.addWidget(self.label, 0, 2, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEdit_3 = QLineEdit(self.page_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_4.addWidget(self.lineEdit_3, 7, 0, 1, 1)

        self.spinBox = QSpinBox(self.page_4)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout_4.addWidget(self.spinBox, 4, 0, 1, 1)

        self.comboBox_4 = QComboBox(self.page_4)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setEnabled(False)

        self.gridLayout_4.addWidget(self.comboBox_4, 3, 1, 1, 1)

        self.comboBox_6 = QComboBox(self.page_4)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setEnabled(False)
        self.comboBox_6.setFrame(False)

        self.gridLayout_4.addWidget(self.comboBox_6, 2, 1, 1, 1)

        self.comboBox = QComboBox(self.page_4)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEditable(True)

        self.gridLayout_4.addWidget(self.comboBox, 0, 0, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.page_4)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.gridLayout_4.addWidget(self.doubleSpinBox, 5, 0, 1, 1)

        self.comboBox_7 = QComboBox(self.page_4)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setEditable(True)

        self.gridLayout_4.addWidget(self.comboBox_7, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.page_4)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_4.addWidget(self.lineEdit, 6, 0, 1, 1)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.page_4)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setEnabled(False)

        self.gridLayout_4.addWidget(self.doubleSpinBox_2, 5, 1, 1, 1)

        self.spinBox_2 = QSpinBox(self.page_4)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setEnabled(False)

        self.gridLayout_4.addWidget(self.spinBox_2, 4, 1, 1, 1)

        self.comboBox_3 = QComboBox(self.page_4)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setEnabled(False)
        self.comboBox_3.setEditable(True)

        self.gridLayout_4.addWidget(self.comboBox_3, 0, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.page_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(False)

        self.gridLayout_4.addWidget(self.lineEdit_2, 6, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.page_4)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_4.addWidget(self.comboBox_2, 3, 0, 1, 1)

        self.comboBox_5 = QComboBox(self.page_4)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setFrame(False)

        self.gridLayout_4.addWidget(self.comboBox_5, 2, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.page_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setEnabled(False)

        self.gridLayout_4.addWidget(self.lineEdit_4, 7, 1, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout_4, 2, 0, 1, 4)

        self.label_2 = QLabel(self.page_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_21.addWidget(self.label_2, 0, 0, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pushButton_18 = QPushButton(self.page_4)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.gridLayout_7.addWidget(self.pushButton_18, 0, 0, 1, 1)

        self.pushButton_22 = QPushButton(self.page_4)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setFlat(True)

        self.gridLayout_7.addWidget(self.pushButton_22, 1, 1, 1, 1)

        self.pushButton_19 = QPushButton(self.page_4)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.gridLayout_7.addWidget(self.pushButton_19, 0, 2, 1, 1)

        self.pushButton_21 = QPushButton(self.page_4)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setFlat(True)

        self.gridLayout_7.addWidget(self.pushButton_21, 1, 2, 1, 1)

        self.pushButton_20 = QPushButton(self.page_4)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.gridLayout_7.addWidget(self.pushButton_20, 0, 1, 1, 1)

        self.pushButton_23 = QPushButton(self.page_4)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setFlat(True)

        self.gridLayout_7.addWidget(self.pushButton_23, 1, 0, 1, 1)


        self.gridLayout_21.addLayout(self.gridLayout_7, 1, 0, 1, 4)

        self.toolBox.addItem(self.page_4, u"Inputs")

        self.gridLayout_22.addWidget(self.toolBox, 0, 0, 2, 2)

        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_23 = QGridLayout(self.tab_2)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.mdiArea = QMdiArea(self.tab_2)
        self.mdiArea.setObjectName(u"mdiArea")

        self.gridLayout_23.addWidget(self.mdiArea, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_2, "")

        self.gridLayout_17.addWidget(self.tabWidget_2, 0, 1, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_6 = QDockWidget(MainWindow)
        self.dockWidget_6.setObjectName(u"dockWidget_6")
        self.dockWidgetContents_5 = QWidget()
        self.dockWidgetContents_5.setObjectName(u"dockWidgetContents_5")
        self.gridLayout_20 = QGridLayout(self.dockWidgetContents_5)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.listWidget = QListWidget(self.dockWidgetContents_5)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setCheckState(Qt.Checked);
        __qlistwidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setCheckState(Qt.Unchecked);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem3.setCheckState(Qt.Checked);
        __qlistwidgetitem3.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem4.setCheckState(Qt.Unchecked);
        __qlistwidgetitem4.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        __qlistwidgetitem5 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem5.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem5.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        QListWidgetItem(self.listWidget)
        __qlistwidgetitem6 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem6.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout_20.addWidget(self.listWidget, 0, 0, 1, 1)

        self.dockWidget_6.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockWidget_6)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.toolBar_vertical = QToolBar(MainWindow)
        self.toolBar_vertical.setObjectName(u"toolBar_vertical")
        MainWindow.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.toolBar_vertical)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout_26 = QGridLayout(self.dockWidgetContents)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.textEdit = QTextEdit(self.dockWidgetContents)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout_26.addWidget(self.textEdit, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.dockWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_26.addWidget(self.plainTextEdit, 1, 0, 1, 1)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockWidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1501, 24))
        self.menumenu = QMenu(self.menubar)
        self.menumenu.setObjectName(u"menumenu")
        self.menuSubmenu = QMenu(self.menumenu)
        self.menuSubmenu.setObjectName(u"menuSubmenu")
        self.menumenu2 = QMenu(self.menubar)
        self.menumenu2.setObjectName(u"menumenu2")
        self.menumenu_disabled = QMenu(self.menubar)
        self.menumenu_disabled.setObjectName(u"menumenu_disabled")
        self.menumenu_disabled.setEnabled(False)
        self.menuStyles = QMenu(self.menubar)
        self.menuStyles.setObjectName(u"menuStyles")
        self.menuDensity = QMenu(self.menubar)
        self.menuDensity.setObjectName(u"menuDensity")
        self.menuMenu_with_icons = QMenu(self.menubar)
        self.menuMenu_with_icons.setObjectName(u"menuMenu_with_icons")
        self.menuMenu3 = QMenu(self.menubar)
        self.menuMenu3.setObjectName(u"menuMenu3")
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.tabWidget_4, self.groupBox)
        QWidget.setTabOrder(self.groupBox, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.pushButton_6)
        QWidget.setTabOrder(self.pushButton_6, self.pushButton_7)
        QWidget.setTabOrder(self.pushButton_7, self.pushButton_11)
        QWidget.setTabOrder(self.pushButton_11, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.groupBox_2)
        QWidget.setTabOrder(self.groupBox_2, self.groupBox_3)
        QWidget.setTabOrder(self.groupBox_3, self.radioButton)
        QWidget.setTabOrder(self.radioButton, self.radioButton_4)
        QWidget.setTabOrder(self.radioButton_4, self.radioButton_2)
        QWidget.setTabOrder(self.radioButton_2, self.radioButton_3)
        QWidget.setTabOrder(self.radioButton_3, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.checkBox_3)
        QWidget.setTabOrder(self.checkBox_3, self.checkBox_4)
        QWidget.setTabOrder(self.checkBox_4, self.checkBox_2)
        QWidget.setTabOrder(self.checkBox_2, self.pushButton_file_dialog)
        QWidget.setTabOrder(self.pushButton_file_dialog, self.pushButton_folder_dialog)
        QWidget.setTabOrder(self.pushButton_folder_dialog, self.tabWidget_3)
        QWidget.setTabOrder(self.tabWidget_3, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.horizontalSlider_2)
        QWidget.setTabOrder(self.horizontalSlider_2, self.verticalSlider_2)
        QWidget.setTabOrder(self.verticalSlider_2, self.treeWidget)
        QWidget.setTabOrder(self.treeWidget, self.listWidget_2)
        QWidget.setTabOrder(self.listWidget_2, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.tabWidget_2)
        QWidget.setTabOrder(self.tabWidget_2, self.pushButton_18)
        QWidget.setTabOrder(self.pushButton_18, self.pushButton_20)
        QWidget.setTabOrder(self.pushButton_20, self.pushButton_19)
        QWidget.setTabOrder(self.pushButton_19, self.pushButton_23)
        QWidget.setTabOrder(self.pushButton_23, self.pushButton_22)
        QWidget.setTabOrder(self.pushButton_22, self.pushButton_21)
        QWidget.setTabOrder(self.pushButton_21, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.comboBox_7)
        QWidget.setTabOrder(self.comboBox_7, self.comboBox_5)
        QWidget.setTabOrder(self.comboBox_5, self.comboBox_2)
        QWidget.setTabOrder(self.comboBox_2, self.spinBox)
        QWidget.setTabOrder(self.spinBox, self.doubleSpinBox)
        QWidget.setTabOrder(self.doubleSpinBox, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.comboBox_3)
        QWidget.setTabOrder(self.comboBox_3, self.comboBox_6)
        QWidget.setTabOrder(self.comboBox_6, self.comboBox_4)
        QWidget.setTabOrder(self.comboBox_4, self.spinBox_2)
        QWidget.setTabOrder(self.spinBox_2, self.doubleSpinBox_2)
        QWidget.setTabOrder(self.doubleSpinBox_2, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.dateEdit_2)
        QWidget.setTabOrder(self.dateEdit_2, self.listWidget)
        QWidget.setTabOrder(self.listWidget, self.textEdit)
        QWidget.setTabOrder(self.textEdit, self.plainTextEdit)
        QWidget.setTabOrder(self.plainTextEdit, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_12)
        QWidget.setTabOrder(self.pushButton_12, self.pushButton_13)
        QWidget.setTabOrder(self.pushButton_13, self.pushButton_14)
        QWidget.setTabOrder(self.pushButton_14, self.pushButton_15)
        QWidget.setTabOrder(self.pushButton_15, self.pushButton_16)
        QWidget.setTabOrder(self.pushButton_16, self.pushButton_17)
        QWidget.setTabOrder(self.pushButton_17, self.radioButton_7)
        QWidget.setTabOrder(self.radioButton_7, self.radioButton_5)
        QWidget.setTabOrder(self.radioButton_5, self.radioButton_6)
        QWidget.setTabOrder(self.radioButton_6, self.radioButton_8)
        QWidget.setTabOrder(self.radioButton_8, self.checkBox_5)
        QWidget.setTabOrder(self.checkBox_5, self.checkBox_6)
        QWidget.setTabOrder(self.checkBox_6, self.checkBox_7)
        QWidget.setTabOrder(self.checkBox_7, self.checkBox_8)
        QWidget.setTabOrder(self.checkBox_8, self.pushButton_8)
        QWidget.setTabOrder(self.pushButton_8, self.pushButton_9)
        QWidget.setTabOrder(self.pushButton_9, self.pushButton_10)
        QWidget.setTabOrder(self.pushButton_10, self.pushButton_24)
        QWidget.setTabOrder(self.pushButton_24, self.pushButton_25)
        QWidget.setTabOrder(self.pushButton_25, self.pushButton_26)
        QWidget.setTabOrder(self.pushButton_26, self.pushButton_27)
        QWidget.setTabOrder(self.pushButton_27, self.radioButton_12)
        QWidget.setTabOrder(self.radioButton_12, self.radioButton_10)
        QWidget.setTabOrder(self.radioButton_10, self.radioButton_11)
        QWidget.setTabOrder(self.radioButton_11, self.radioButton_9)
        QWidget.setTabOrder(self.radioButton_9, self.checkBox_10)
        QWidget.setTabOrder(self.checkBox_10, self.checkBox_11)
        QWidget.setTabOrder(self.checkBox_11, self.checkBox_12)
        QWidget.setTabOrder(self.checkBox_12, self.checkBox_9)
        QWidget.setTabOrder(self.checkBox_9, self.timeEdit)
        QWidget.setTabOrder(self.timeEdit, self.dateEdit)
        QWidget.setTabOrder(self.dateEdit, self.dateTimeEdit)
        QWidget.setTabOrder(self.dateTimeEdit, self.keySequenceEdit)
        QWidget.setTabOrder(self.keySequenceEdit, self.calendarWidget)
        QWidget.setTabOrder(self.calendarWidget, self.groupBox_7)
        QWidget.setTabOrder(self.groupBox_7, self.pushButton_28)
        QWidget.setTabOrder(self.pushButton_28, self.pushButton_32)
        QWidget.setTabOrder(self.pushButton_32, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.pushButton_30)
        QWidget.setTabOrder(self.pushButton_30, self.pushButton_33)
        QWidget.setTabOrder(self.pushButton_33, self.pushButton_29)
        QWidget.setTabOrder(self.pushButton_29, self.pushButton_31)
        QWidget.setTabOrder(self.pushButton_31, self.doubleSpinBox_3)
        QWidget.setTabOrder(self.doubleSpinBox_3, self.timeEdit_2)
        QWidget.setTabOrder(self.timeEdit_2, self.dateTimeEdit_2)
        QWidget.setTabOrder(self.dateTimeEdit_2, self.comboBox_8)
        QWidget.setTabOrder(self.comboBox_8, self.tabWidget_6)
        QWidget.setTabOrder(self.tabWidget_6, self.fontComboBox)
        QWidget.setTabOrder(self.fontComboBox, self.tabWidget_5)
        QWidget.setTabOrder(self.tabWidget_5, self.tabWidget_7)
        QWidget.setTabOrder(self.tabWidget_7, self.spinBox_3)
        QWidget.setTabOrder(self.spinBox_3, self.tableWidget_2)
        QWidget.setTabOrder(self.tableWidget_2, self.lineEdit_5)

        self.toolBar.addAction(self.actionToolbar)
        self.toolBar.addAction(self.actionSelected)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionaction)
        self.toolBar.addAction(self.actionaction2)
        self.toolBar.addAction(self.actionaction3)
        self.toolBar_vertical.addAction(self.actionToolbar)
        self.toolBar_vertical.addAction(self.actionSelected)
        self.menubar.addAction(self.menuStyles.menuAction())
        self.menubar.addAction(self.menuDensity.menuAction())
        self.menubar.addAction(self.menumenu.menuAction())
        self.menubar.addAction(self.menumenu2.menuAction())
        self.menubar.addAction(self.menuMenu_with_icons.menuAction())
        self.menubar.addAction(self.menumenu_disabled.menuAction())
        self.menubar.addAction(self.menuMenu3.menuAction())
        self.menumenu.addAction(self.menuSubmenu.menuAction())
        self.menumenu.addAction(self.actionSubmenu_2)
        self.menumenu.addSeparator()
        self.menumenu.addAction(self.actionSubmenu_3)
        self.menumenu.addAction(self.actiondissabled)
        self.menuSubmenu.addAction(self.actionSUBSUB)
        self.menuSubmenu.addAction(self.actionSUBSUB_2)
        self.menuSubmenu.addSeparator()
        self.menuSubmenu.addAction(self.actionSUBSUB_3)
        self.menumenu2.addAction(self.actionSubmenu)
        self.menumenu2.addAction(self.actionSubmenu_4)
        self.menumenu2.addAction(self.actionSubmenu_5)
        self.menuMenu_with_icons.addAction(self.actionsubmenu)
        self.menuMenu_with_icons.addAction(self.actionsubmenu_2)
        self.menuMenu_with_icons.addSeparator()
        self.menuMenu_with_icons.addAction(self.actionsubmenu_4)
        self.menuMenu_with_icons.addAction(self.actionsubmenu_3)
        self.menuMenu_with_icons.addAction(self.actionSave_all)
        self.menuMenu_with_icons.addSeparator()
        self.menuMenu_with_icons.addAction(self.actionClose)

        self.retranslateUi(MainWindow)

        self.tabWidget_4.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        self.tabWidget_6.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Qt Material", None))
        self.actionSubmenu_2.setText(QCoreApplication.translate("MainWindow", u"Submenu", None))
        self.actionSubmenu_3.setText(QCoreApplication.translate("MainWindow", u"Submenu", None))
        self.actionSUBSUB.setText(QCoreApplication.translate("MainWindow", u"SUBSUB", None))
        self.actionSUBSUB_2.setText(QCoreApplication.translate("MainWindow", u"SUBSUB", None))
        self.actionSUBSUB_3.setText(QCoreApplication.translate("MainWindow", u"SUBSUB", None))
        self.actiondissabled.setText(QCoreApplication.translate("MainWindow", u"dissabled", None))
        self.actionSubmenu.setText(QCoreApplication.translate("MainWindow", u"Submenu", None))
        self.actionSubmenu_4.setText(QCoreApplication.translate("MainWindow", u"Submenu", None))
        self.actionSubmenu_5.setText(QCoreApplication.translate("MainWindow", u"Submenu", None))
        self.actionToolbar.setText(QCoreApplication.translate("MainWindow", u"Qt Material Theme", None))
#if QT_CONFIG(tooltip)
        self.actionToolbar.setToolTip(QCoreApplication.translate("MainWindow", u"Qt Material Theme", None))
#endif // QT_CONFIG(tooltip)
        self.actionSelected.setText(QCoreApplication.translate("MainWindow", u"Selected", None))
        self.actionaction.setText(QCoreApplication.translate("MainWindow", u"action", None))
        self.actionaction2.setText(QCoreApplication.translate("MainWindow", u"action2", None))
        self.actionaction3.setText(QCoreApplication.translate("MainWindow", u"action3", None))
        self.action111.setText(QCoreApplication.translate("MainWindow", u"111", None))
        self.action222.setText(QCoreApplication.translate("MainWindow", u"222", None))
        self.action333.setText(QCoreApplication.translate("MainWindow", u"333", None))
        self.actionsubmenu.setText(QCoreApplication.translate("MainWindow", u"New...", None))
        self.actionsubmenu_2.setText(QCoreApplication.translate("MainWindow", u"Open...", None))
        self.actionsubmenu_3.setText(QCoreApplication.translate("MainWindow", u"Save as...", None))
        self.actionsubmenu_4.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_all.setText(QCoreApplication.translate("MainWindow", u"Save all", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Radio", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Check", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Buttons", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Checked", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Disable checked", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Flat", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Flat checkeable", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Flat disabled", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"Page", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Checked", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Flat disabled", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Disable checked", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Flat checkeable", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Flat", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"Page", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Buttons", None))
        self.groupBox_6.setProperty(u"class", QCoreApplication.translate("MainWindow", u"fill_background", None))
#if QT_CONFIG(tooltip)
        self.pushButton_8.setToolTip(QCoreApplication.translate("MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Checked", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Disable checked", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Flat", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"Flat checkeable", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"Flat disabled", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Radio", None))
        self.groupBox_5.setProperty(u"class", QCoreApplication.translate("MainWindow", u"fill_background", None))
        self.radioButton_9.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_11.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_12.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Check", None))
        self.groupBox_4.setProperty(u"class", QCoreApplication.translate("MainWindow", u"fill_background", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"Long Page Name", None))

        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_2.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem1 = self.listWidget_2.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem2 = self.listWidget_2.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        self.listWidget_2.setSortingEnabled(__sortingEnabled)

        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Material Tree", None));

        __sortingEnabled1 = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Tree #1", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Subitem #1", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"Subitem #2", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem3.child(0)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"New Subitem", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem3.child(1)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qtreewidgetitem6 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"Tree #2", None));
        ___qtreewidgetitem7 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"Subitem #4", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem7.child(0)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"Subitem #41", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem7.child(1)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"Subitem #42", None));
        ___qtreewidgetitem10 = self.treeWidget.topLevelItem(3)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"Subitem #5", None));
        ___qtreewidgetitem11 = self.treeWidget.topLevelItem(4)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"Tree #3", None));
        ___qtreewidgetitem12 = self.treeWidget.topLevelItem(5)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"Tree #4", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled1)

        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Duration", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Datetime", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Row-1", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Row-3", None));

        __sortingEnabled2 = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"00:05:02", None));
        ___qtablewidgetitem6 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"2020-04-27 17:31:34", None));
        ___qtablewidgetitem7 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Unamed-1", None));
        ___qtablewidgetitem8 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"00:01:02", None));
        ___qtablewidgetitem9 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"2020-04-27 17:31:34", None));
        ___qtablewidgetitem10 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Unamed-2", None));
        ___qtablewidgetitem11 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"00:07:02", None));
        ___qtablewidgetitem12 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"2020-04-27 17:31:34", None));
        ___qtablewidgetitem13 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Unamed-3", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled2)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Widgets", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_15), QCoreApplication.translate("MainWindow", u"Widget area", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_16), QCoreApplication.translate("MainWindow", u"Frame area", None))
        ___qtablewidgetitem14 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Duration", None));
        ___qtablewidgetitem15 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Datetime", None));
        ___qtablewidgetitem16 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem17 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Row-1", None));
        ___qtablewidgetitem18 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Row-3", None));

        __sortingEnabled3 = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem19 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"00:05:02", None));
        ___qtablewidgetitem20 = self.tableWidget_2.item(0, 1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"2020-04-27 17:31:34", None));
        ___qtablewidgetitem21 = self.tableWidget_2.item(0, 2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Unamed-1", None));
        ___qtablewidgetitem22 = self.tableWidget_2.item(1, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"00:01:02", None));
        ___qtablewidgetitem23 = self.tableWidget_2.item(1, 1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"2020-04-27 17:31:34", None));
        ___qtablewidgetitem24 = self.tableWidget_2.item(1, 2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Unamed-2", None));
        ___qtablewidgetitem25 = self.tableWidget_2.item(2, 0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"00:07:02", None));
        ___qtablewidgetitem26 = self.tableWidget_2.item(2, 1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"2020-04-27 17:31:34", None));
        ___qtablewidgetitem27 = self.tableWidget_2.item(2, 2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Unamed-3", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled3)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_18), QCoreApplication.translate("MainWindow", u"Table", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"Danger", None))
        self.pushButton_28.setProperty(u"class", QCoreApplication.translate("MainWindow", u"danger", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"Success", None))
        self.pushButton_29.setProperty(u"class", QCoreApplication.translate("MainWindow", u"success", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"Warning", None))
        self.pushButton_30.setProperty(u"class", QCoreApplication.translate("MainWindow", u"warning", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"Warning", None))
        self.pushButton_31.setProperty(u"class", QCoreApplication.translate("MainWindow", u"warning", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"Success", None))
        self.pushButton_32.setProperty(u"class", QCoreApplication.translate("MainWindow", u"success", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"Danger", None))
        self.pushButton_33.setProperty(u"class", QCoreApplication.translate("MainWindow", u"danger", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_19), QCoreApplication.translate("MainWindow", u"Buttons colored", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_24), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_38), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_39), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_25), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_22), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_23), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_28), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_29), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_30), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_31), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_32), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_33), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_34), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_35), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_36), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_37), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_20), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_26), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_21), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_27), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Tabs", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_8.setItemText(2, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_8.setItemText(3, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_8.setItemText(4, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_8.setItemText(5, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"Inputs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_17), QCoreApplication.translate("MainWindow", u"Lines", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"Long Page Name", None))
        self.pushButton_file_dialog.setText(QCoreApplication.translate("MainWindow", u"QFileDialog", None))
        self.pushButton_folder_dialog.setText(QCoreApplication.translate("MainWindow", u"QFolderDialog", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"WebEngine", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"Date controls", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Material theme", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Material theme", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Placeholder text", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"New Item1", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"New Item2", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("MainWindow", u"New Item3", None))
        self.comboBox_6.setItemText(3, QCoreApplication.translate("MainWindow", u"New Item4", None))
        self.comboBox_6.setItemText(4, QCoreApplication.translate("MainWindow", u"New Item5", None))
        self.comboBox_6.setItemText(5, QCoreApplication.translate("MainWindow", u"New Item6", None))
        self.comboBox_6.setItemText(6, QCoreApplication.translate("MainWindow", u"New Item7", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_7.setItemText(3, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_7.setItemText(4, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Lorem ipsum dolor sit amet", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"Lorem ipsum dolor sit amet", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"New Item1", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"New Item2", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"New Item3", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"New Item4", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"New Item5", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"New Item6", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"New Item7", None))

        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"New Item1", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"New Item2", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"New Item3", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("MainWindow", u"New Item4", None))
        self.comboBox_5.setItemText(4, QCoreApplication.translate("MainWindow", u"New Item5", None))
        self.comboBox_5.setItemText(5, QCoreApplication.translate("MainWindow", u"New Item6", None))
        self.comboBox_5.setItemText(6, QCoreApplication.translate("MainWindow", u"New Item7", None))

        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Placeholder text", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Material theme", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Danger", None))
        self.pushButton_18.setProperty(u"class", QCoreApplication.translate("MainWindow", u"danger", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Success", None))
        self.pushButton_22.setProperty(u"class", QCoreApplication.translate("MainWindow", u"success", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Warning", None))
        self.pushButton_19.setProperty(u"class", QCoreApplication.translate("MainWindow", u"warning", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Warning", None))
        self.pushButton_21.setProperty(u"class", QCoreApplication.translate("MainWindow", u"warning", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Success", None))
        self.pushButton_20.setProperty(u"class", QCoreApplication.translate("MainWindow", u"success", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Danger", None))
        self.pushButton_23.setProperty(u"class", QCoreApplication.translate("MainWindow", u"danger", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"Inputs", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Long Page Name", None))
        self.dockWidget_6.setWindowTitle(QCoreApplication.translate("MainWindow", u"Top Dock", None))

        __sortingEnabled4 = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem3 = self.listWidget.item(0)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Item (editable)", None));
        ___qlistwidgetitem4 = self.listWidget.item(1)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem5 = self.listWidget.item(2)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem6 = self.listWidget.item(3)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem7 = self.listWidget.item(4)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem8 = self.listWidget.item(5)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem9 = self.listWidget.item(6)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem10 = self.listWidget.item(7)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        self.listWidget.setSortingEnabled(__sortingEnabled4)

        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_vertical.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("MainWindow", u"Right Doc", None))
        self.textEdit.setMarkdown(QCoreApplication.translate("MainWindow", u"textEdit Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\n"
"eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim\n"
"veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo\n"
"consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse\n"
"cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non\n"
"proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n"
"\n"
"", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans';\">textEdit Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepte"
                        "ur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</span></p></body></html>", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"plainTextEdit\n"
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", None))
        self.menumenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuSubmenu.setTitle(QCoreApplication.translate("MainWindow", u"Submenu", None))
        self.menumenu2.setTitle(QCoreApplication.translate("MainWindow", u"Menu2", None))
        self.menumenu_disabled.setTitle(QCoreApplication.translate("MainWindow", u"Menu3 disabled", None))
        self.menuStyles.setTitle(QCoreApplication.translate("MainWindow", u"Styles", None))
        self.menuDensity.setTitle(QCoreApplication.translate("MainWindow", u"Density", None))
        self.menuMenu_with_icons.setTitle(QCoreApplication.translate("MainWindow", u"Menu with icons", None))
        self.menuMenu3.setTitle(QCoreApplication.translate("MainWindow", u"Menu4", None))
    # retranslateUi

