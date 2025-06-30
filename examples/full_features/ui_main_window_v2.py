# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_v2.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QComboBox,
    QDateEdit, QDateTimeEdit, QDoubleSpinBox, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QKeySequenceEdit, QLCDNumber, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMdiArea, QMenu, QMenuBar, QPlainTextEdit,
    QProgressBar, QPushButton, QRadioButton, QScrollBar,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QStackedWidget, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QTimeEdit, QToolBar,
    QToolBox, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(2080, 1148)
        MainWindow.setMinimumSize(QSize(0, 0))
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
        self.action_widgets = QAction(MainWindow)
        self.action_widgets.setObjectName(u"action_widgets")
        self.action_widgets.setCheckable(True)
        self.action_widgets.setChecked(True)
        self.action_tabs = QAction(MainWindow)
        self.action_tabs.setObjectName(u"action_tabs")
        self.action_tabs.setCheckable(True)
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
        self.action_examples = QAction(MainWindow)
        self.action_examples.setObjectName(u"action_examples")
        self.action_examples.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_11 = QGridLayout(self.centralwidget)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_22 = QGridLayout(self.page)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.toolBox = QToolBox(self.page)
        self.toolBox.setObjectName(u"toolBox")
        self.page_22 = QWidget()
        self.page_22.setObjectName(u"page_22")
        self.page_22.setGeometry(QRect(0, 0, 1925, 447))
        self.gridLayout_18 = QGridLayout(self.page_22)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_13, 3, 1, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_10, 0, 1, 1, 1)

        self.gridLayout_28 = QGridLayout()
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.pushButton_3 = QPushButton(self.page_22)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_28.addWidget(self.pushButton_3, 0, 0, 1, 1)

        self.pushButton_18 = QPushButton(self.page_22)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setCheckable(True)
        self.pushButton_18.setChecked(True)

        self.gridLayout_28.addWidget(self.pushButton_18, 0, 1, 1, 1)

        self.pushButton_19 = QPushButton(self.page_22)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setEnabled(False)
        self.pushButton_19.setFlat(True)

        self.gridLayout_28.addWidget(self.pushButton_19, 2, 0, 1, 1)

        self.pushButton_20 = QPushButton(self.page_22)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setEnabled(False)
        self.pushButton_20.setCheckable(True)
        self.pushButton_20.setChecked(True)
        self.pushButton_20.setFlat(False)

        self.gridLayout_28.addWidget(self.pushButton_20, 1, 0, 1, 1)

        self.pushButton_21 = QPushButton(self.page_22)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setEnabled(False)
        self.pushButton_21.setCheckable(False)
        self.pushButton_21.setChecked(False)
        self.pushButton_21.setFlat(False)

        self.gridLayout_28.addWidget(self.pushButton_21, 0, 2, 1, 1)

        self.pushButton_22 = QPushButton(self.page_22)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setCheckable(True)
        self.pushButton_22.setChecked(False)
        self.pushButton_22.setFlat(True)

        self.gridLayout_28.addWidget(self.pushButton_22, 1, 2, 1, 1)

        self.pushButton_23 = QPushButton(self.page_22)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setFlat(True)

        self.gridLayout_28.addWidget(self.pushButton_23, 1, 1, 1, 1)


        self.gridLayout_18.addLayout(self.gridLayout_28, 1, 1, 1, 1)

        self.gridLayout_29 = QGridLayout()
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.pushButton_33 = QPushButton(self.page_22)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setEnabled(False)
        self.pushButton_33.setFlat(True)

        self.gridLayout_29.addWidget(self.pushButton_33, 2, 1, 1, 1)

        self.pushButton_30 = QPushButton(self.page_22)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setEnabled(False)
        self.pushButton_30.setCheckable(True)
        self.pushButton_30.setChecked(True)
        self.pushButton_30.setFlat(False)

        self.gridLayout_29.addWidget(self.pushButton_30, 2, 0, 1, 1)

        self.pushButton_28 = QPushButton(self.page_22)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setEnabled(False)
        self.pushButton_28.setCheckable(True)
        self.pushButton_28.setChecked(True)

        self.gridLayout_29.addWidget(self.pushButton_28, 1, 1, 1, 1)

        self.pushButton_29 = QPushButton(self.page_22)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setEnabled(False)
        self.pushButton_29.setFlat(True)

        self.gridLayout_29.addWidget(self.pushButton_29, 3, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.page_22)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(False)

        self.gridLayout_29.addWidget(self.pushButton_4, 1, 0, 1, 1)

        self.pushButton_32 = QPushButton(self.page_22)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setEnabled(False)
        self.pushButton_32.setCheckable(True)
        self.pushButton_32.setChecked(False)
        self.pushButton_32.setFlat(True)

        self.gridLayout_29.addWidget(self.pushButton_32, 2, 2, 1, 1)

        self.pushButton_31 = QPushButton(self.page_22)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setEnabled(False)
        self.pushButton_31.setCheckable(False)
        self.pushButton_31.setChecked(False)
        self.pushButton_31.setFlat(False)

        self.gridLayout_29.addWidget(self.pushButton_31, 1, 2, 1, 1)


        self.gridLayout_18.addLayout(self.gridLayout_29, 4, 1, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_12, 5, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_3, 1, 0, 4, 1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_20, 1, 2, 4, 1)

        self.toolBox.addItem(self.page_22, u"Buttons")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.page_7.setGeometry(QRect(0, 0, 1925, 447))
        self.gridLayout_4 = QGridLayout(self.page_7)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_37 = QGridLayout()
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.pushButton_57 = QPushButton(self.page_7)
        self.pushButton_57.setObjectName(u"pushButton_57")
        self.pushButton_57.setEnabled(False)

        self.gridLayout_37.addWidget(self.pushButton_57, 1, 2, 1, 1)

        self.pushButton_58 = QPushButton(self.page_7)
        self.pushButton_58.setObjectName(u"pushButton_58")
        self.pushButton_58.setEnabled(False)
        self.pushButton_58.setFlat(True)

        self.gridLayout_37.addWidget(self.pushButton_58, 2, 0, 1, 1)

        self.pushButton_59 = QPushButton(self.page_7)
        self.pushButton_59.setObjectName(u"pushButton_59")
        self.pushButton_59.setEnabled(False)
        self.pushButton_59.setFlat(True)

        self.gridLayout_37.addWidget(self.pushButton_59, 2, 1, 1, 1)

        self.pushButton_60 = QPushButton(self.page_7)
        self.pushButton_60.setObjectName(u"pushButton_60")
        self.pushButton_60.setEnabled(False)

        self.gridLayout_37.addWidget(self.pushButton_60, 1, 1, 1, 1)

        self.pushButton_61 = QPushButton(self.page_7)
        self.pushButton_61.setObjectName(u"pushButton_61")
        self.pushButton_61.setEnabled(False)
        self.pushButton_61.setFlat(True)

        self.gridLayout_37.addWidget(self.pushButton_61, 2, 2, 1, 1)

        self.pushButton_62 = QPushButton(self.page_7)
        self.pushButton_62.setObjectName(u"pushButton_62")
        self.pushButton_62.setEnabled(False)

        self.gridLayout_37.addWidget(self.pushButton_62, 1, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_37, 4, 1, 1, 2)

        self.gridLayout_36 = QGridLayout()
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.pushButton_24 = QPushButton(self.page_7)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.gridLayout_36.addWidget(self.pushButton_24, 1, 2, 1, 1)

        self.pushButton_25 = QPushButton(self.page_7)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setFlat(True)

        self.gridLayout_36.addWidget(self.pushButton_25, 2, 0, 1, 1)

        self.pushButton_27 = QPushButton(self.page_7)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setFlat(True)

        self.gridLayout_36.addWidget(self.pushButton_27, 2, 1, 1, 1)

        self.pushButton_55 = QPushButton(self.page_7)
        self.pushButton_55.setObjectName(u"pushButton_55")

        self.gridLayout_36.addWidget(self.pushButton_55, 1, 1, 1, 1)

        self.pushButton_56 = QPushButton(self.page_7)
        self.pushButton_56.setObjectName(u"pushButton_56")
        self.pushButton_56.setFlat(True)

        self.gridLayout_36.addWidget(self.pushButton_56, 2, 2, 1, 1)

        self.pushButton_26 = QPushButton(self.page_7)
        self.pushButton_26.setObjectName(u"pushButton_26")

        self.gridLayout_36.addWidget(self.pushButton_26, 1, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_36, 2, 1, 1, 2)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_17, 2, 0, 3, 1)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_21, 2, 3, 3, 1)

        self.verticalSpacer_8 = QSpacerItem(741, 63, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_8, 5, 1, 1, 2)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_23, 3, 1, 1, 2)

        self.verticalSpacer_22 = QSpacerItem(20, 51, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_22, 1, 1, 1, 2)

        self.label_75 = QLabel(self.page_7)
        self.label_75.setObjectName(u"label_75")

        self.gridLayout_4.addWidget(self.label_75, 6, 1, 1, 2)

        self.toolBox.addItem(self.page_7, u"Colored Buttons")
        self.page_23 = QWidget()
        self.page_23.setObjectName(u"page_23")
        self.page_23.setGeometry(QRect(0, 0, 1925, 447))
        self.gridLayout_19 = QGridLayout(self.page_23)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_22)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_14)

        self.radioButton_7 = QRadioButton(self.page_23)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setChecked(True)
        self.radioButton_7.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.radioButton_7)

        self.radioButton_5 = QRadioButton(self.page_23)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.radioButton_5)

        self.radioButton_8 = QRadioButton(self.page_23)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setEnabled(False)
        self.radioButton_8.setChecked(True)

        self.verticalLayout.addWidget(self.radioButton_8)

        self.radioButton_6 = QRadioButton(self.page_23)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setEnabled(False)

        self.verticalLayout.addWidget(self.radioButton_6)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout_19.addLayout(self.verticalLayout)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_24)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_15)

        self.checkBox_8 = QCheckBox(self.page_23)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setChecked(True)
        self.checkBox_8.setTristate(True)

        self.verticalLayout_2.addWidget(self.checkBox_8)

        self.checkBox_5 = QCheckBox(self.page_23)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setTristate(True)

        self.verticalLayout_2.addWidget(self.checkBox_5)

        self.checkBox_7 = QCheckBox(self.page_23)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setEnabled(False)
        self.checkBox_7.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkBox_7)

        self.checkBox_6 = QCheckBox(self.page_23)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setEnabled(False)

        self.verticalLayout_2.addWidget(self.checkBox_6)

        self.checkBox_13 = QCheckBox(self.page_23)
        self.checkBox_13.setObjectName(u"checkBox_13")
        self.checkBox_13.setTristate(True)

        self.verticalLayout_2.addWidget(self.checkBox_13)

        self.checkBox_14 = QCheckBox(self.page_23)
        self.checkBox_14.setObjectName(u"checkBox_14")
        self.checkBox_14.setEnabled(False)
        self.checkBox_14.setTristate(True)

        self.verticalLayout_2.addWidget(self.checkBox_14)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)


        self.horizontalLayout_19.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_23)


        self.gridLayout_19.addLayout(self.horizontalLayout_19, 0, 0, 1, 1)

        self.toolBox.addItem(self.page_23, u"Radios and Checkboxes")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 1925, 447))
        self.verticalLayout_16 = QVBoxLayout(self.page_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.label_4 = QLabel(self.page_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)

        self.label_5 = QLabel(self.page_4)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)

        self.label_6 = QLabel(self.page_4)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setItalic(True)
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_10)

        self.label_7 = QLabel(self.page_4)
        self.label_7.setObjectName(u"label_7")
        font2 = QFont()
        font2.setItalic(False)
        font2.setUnderline(True)
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_11)

        self.label_8 = QLabel(self.page_4)
        self.label_8.setObjectName(u"label_8")
        font3 = QFont()
        font3.setStrikeOut(True)
        self.label_8.setFont(font3)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_8)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_16.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.label_11 = QLabel(self.page_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setEnabled(False)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_11)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_12)

        self.label_13 = QLabel(self.page_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setEnabled(False)
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_13)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_13)

        self.label_10 = QLabel(self.page_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setEnabled(False)
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_10)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_14)

        self.label_9 = QLabel(self.page_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setEnabled(False)
        self.label_9.setFont(font3)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_9)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_15)

        self.label_12 = QLabel(self.page_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setEnabled(False)
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_12)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout_16.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page_4, u"Labels")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 1925, 447))
        self.gridLayout_16 = QGridLayout(self.page_2)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_25, 0, 0, 1, 1)

        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.lineEdit_6 = QLineEdit(self.page_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_21.addWidget(self.lineEdit_6, 4, 0, 1, 2)

        self.comboBox_11 = QComboBox(self.page_2)
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.setObjectName(u"comboBox_11")
        self.comboBox_11.setEditable(True)

        self.gridLayout_21.addWidget(self.comboBox_11, 0, 0, 1, 2)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.spinBox_4 = QSpinBox(self.page_2)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setValue(3)

        self.verticalLayout_18.addWidget(self.spinBox_4)

        self.spinBox_6 = QSpinBox(self.page_2)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setValue(7)

        self.verticalLayout_18.addWidget(self.spinBox_6)

        self.spinBox_7 = QSpinBox(self.page_2)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setValue(9)

        self.verticalLayout_18.addWidget(self.spinBox_7)

        self.spinBox_8 = QSpinBox(self.page_2)
        self.spinBox_8.setObjectName(u"spinBox_8")
        self.spinBox_8.setValue(11)

        self.verticalLayout_18.addWidget(self.spinBox_8)


        self.gridLayout_21.addLayout(self.verticalLayout_18, 2, 0, 1, 1)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.doubleSpinBox_4 = QDoubleSpinBox(self.page_2)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")
        self.doubleSpinBox_4.setDecimals(5)
        self.doubleSpinBox_4.setValue(3.141590000000000)

        self.verticalLayout_17.addWidget(self.doubleSpinBox_4)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.page_2)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")
        self.doubleSpinBox_6.setDecimals(5)
        self.doubleSpinBox_6.setValue(3.141590000000000)

        self.verticalLayout_17.addWidget(self.doubleSpinBox_6)

        self.doubleSpinBox_7 = QDoubleSpinBox(self.page_2)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")
        self.doubleSpinBox_7.setDecimals(5)
        self.doubleSpinBox_7.setValue(3.141590000000000)

        self.verticalLayout_17.addWidget(self.doubleSpinBox_7)

        self.doubleSpinBox_8 = QDoubleSpinBox(self.page_2)
        self.doubleSpinBox_8.setObjectName(u"doubleSpinBox_8")
        self.doubleSpinBox_8.setDecimals(5)
        self.doubleSpinBox_8.setValue(3.141590000000000)

        self.verticalLayout_17.addWidget(self.doubleSpinBox_8)


        self.gridLayout_21.addLayout(self.verticalLayout_17, 2, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.page_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_21.addWidget(self.lineEdit_7, 3, 0, 1, 2)

        self.comboBox_13 = QComboBox(self.page_2)
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.setObjectName(u"comboBox_13")
        self.comboBox_13.setEditable(True)
        self.comboBox_13.setFrame(False)

        self.gridLayout_21.addWidget(self.comboBox_13, 1, 0, 1, 2)


        self.gridLayout_16.addLayout(self.gridLayout_21, 0, 1, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_16, 0, 2, 1, 1)

        self.gridLayout_38 = QGridLayout()
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.comboBox_12 = QComboBox(self.page_2)
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.setObjectName(u"comboBox_12")
        self.comboBox_12.setEnabled(False)
        self.comboBox_12.setEditable(True)

        self.gridLayout_38.addWidget(self.comboBox_12, 0, 0, 1, 2)

        self.lineEdit_9 = QLineEdit(self.page_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setEnabled(False)

        self.gridLayout_38.addWidget(self.lineEdit_9, 4, 0, 1, 2)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.spinBox_5 = QSpinBox(self.page_2)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setEnabled(False)
        self.spinBox_5.setValue(3)

        self.verticalLayout_20.addWidget(self.spinBox_5)

        self.spinBox_9 = QSpinBox(self.page_2)
        self.spinBox_9.setObjectName(u"spinBox_9")
        self.spinBox_9.setEnabled(False)
        self.spinBox_9.setValue(7)

        self.verticalLayout_20.addWidget(self.spinBox_9)

        self.spinBox_10 = QSpinBox(self.page_2)
        self.spinBox_10.setObjectName(u"spinBox_10")
        self.spinBox_10.setEnabled(False)
        self.spinBox_10.setValue(9)

        self.verticalLayout_20.addWidget(self.spinBox_10)

        self.spinBox_11 = QSpinBox(self.page_2)
        self.spinBox_11.setObjectName(u"spinBox_11")
        self.spinBox_11.setEnabled(False)
        self.spinBox_11.setValue(11)

        self.verticalLayout_20.addWidget(self.spinBox_11)


        self.gridLayout_38.addLayout(self.verticalLayout_20, 2, 0, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.doubleSpinBox_5 = QDoubleSpinBox(self.page_2)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")
        self.doubleSpinBox_5.setEnabled(False)
        self.doubleSpinBox_5.setDecimals(5)
        self.doubleSpinBox_5.setValue(3.141590000000000)

        self.verticalLayout_19.addWidget(self.doubleSpinBox_5)

        self.doubleSpinBox_9 = QDoubleSpinBox(self.page_2)
        self.doubleSpinBox_9.setObjectName(u"doubleSpinBox_9")
        self.doubleSpinBox_9.setEnabled(False)
        self.doubleSpinBox_9.setDecimals(5)
        self.doubleSpinBox_9.setValue(3.141590000000000)

        self.verticalLayout_19.addWidget(self.doubleSpinBox_9)

        self.doubleSpinBox_10 = QDoubleSpinBox(self.page_2)
        self.doubleSpinBox_10.setObjectName(u"doubleSpinBox_10")
        self.doubleSpinBox_10.setEnabled(False)
        self.doubleSpinBox_10.setDecimals(5)
        self.doubleSpinBox_10.setValue(3.141590000000000)

        self.verticalLayout_19.addWidget(self.doubleSpinBox_10)

        self.doubleSpinBox_11 = QDoubleSpinBox(self.page_2)
        self.doubleSpinBox_11.setObjectName(u"doubleSpinBox_11")
        self.doubleSpinBox_11.setEnabled(False)
        self.doubleSpinBox_11.setDecimals(5)
        self.doubleSpinBox_11.setValue(3.141590000000000)

        self.verticalLayout_19.addWidget(self.doubleSpinBox_11)


        self.gridLayout_38.addLayout(self.verticalLayout_19, 2, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.page_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setEnabled(False)

        self.gridLayout_38.addWidget(self.lineEdit_8, 3, 0, 1, 2)

        self.comboBox_14 = QComboBox(self.page_2)
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.setObjectName(u"comboBox_14")
        self.comboBox_14.setEnabled(False)
        self.comboBox_14.setEditable(True)
        self.comboBox_14.setFrame(False)

        self.gridLayout_38.addWidget(self.comboBox_14, 1, 0, 1, 2)


        self.gridLayout_16.addLayout(self.gridLayout_38, 0, 3, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_26, 0, 4, 1, 1)

        self.toolBox.addItem(self.page_2, u"Inputs")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 1925, 447))
        self.gridLayout_48 = QGridLayout(self.page_3)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_48.addItem(self.horizontalSpacer_27, 0, 0, 1, 1)

        self.gridLayout_47 = QGridLayout()
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.keySequenceEdit_4 = QKeySequenceEdit(self.page_3)
        self.keySequenceEdit_4.setObjectName(u"keySequenceEdit_4")
        self.keySequenceEdit_4.setEnabled(False)

        self.gridLayout_47.addWidget(self.keySequenceEdit_4, 1, 1, 1, 1)

        self.timeEdit_4 = QTimeEdit(self.page_3)
        self.timeEdit_4.setObjectName(u"timeEdit_4")
        self.timeEdit_4.setEnabled(False)

        self.gridLayout_47.addWidget(self.timeEdit_4, 0, 0, 1, 1)

        self.dateEdit_4 = QDateEdit(self.page_3)
        self.dateEdit_4.setObjectName(u"dateEdit_4")
        self.dateEdit_4.setEnabled(False)
        self.dateEdit_4.setDateTime(QDateTime(QDate(1991, 2, 9), QTime(11, 0, 0)))
        self.dateEdit_4.setCalendarPopup(True)

        self.gridLayout_47.addWidget(self.dateEdit_4, 0, 1, 1, 1)

        self.dateTimeEdit_4 = QDateTimeEdit(self.page_3)
        self.dateTimeEdit_4.setObjectName(u"dateTimeEdit_4")
        self.dateTimeEdit_4.setEnabled(False)

        self.gridLayout_47.addWidget(self.dateTimeEdit_4, 1, 0, 1, 1)

        self.lcdNumber_2 = QLCDNumber(self.page_3)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setEnabled(False)
        self.lcdNumber_2.setSmallDecimalPoint(True)
        self.lcdNumber_2.setDigitCount(10)
        self.lcdNumber_2.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.lcdNumber_2.setProperty(u"value", 3.141592000000000)

        self.gridLayout_47.addWidget(self.lcdNumber_2, 0, 2, 2, 1)

        self.calendarWidget_2 = QCalendarWidget(self.page_3)
        self.calendarWidget_2.setObjectName(u"calendarWidget_2")
        self.calendarWidget_2.setEnabled(False)

        self.gridLayout_47.addWidget(self.calendarWidget_2, 2, 0, 1, 3)

        self.gridLayout_47.setColumnStretch(0, 1)
        self.gridLayout_47.setColumnStretch(1, 1)
        self.gridLayout_47.setColumnStretch(2, 3)

        self.gridLayout_48.addLayout(self.gridLayout_47, 0, 3, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_48.addItem(self.horizontalSpacer_28, 0, 4, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.keySequenceEdit = QKeySequenceEdit(self.page_3)
        self.keySequenceEdit.setObjectName(u"keySequenceEdit")

        self.gridLayout_9.addWidget(self.keySequenceEdit, 1, 1, 1, 1)

        self.timeEdit = QTimeEdit(self.page_3)
        self.timeEdit.setObjectName(u"timeEdit")

        self.gridLayout_9.addWidget(self.timeEdit, 0, 0, 1, 1)

        self.dateEdit = QDateEdit(self.page_3)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setDateTime(QDateTime(QDate(1991, 2, 9), QTime(6, 0, 0)))
        self.dateEdit.setCalendarPopup(True)

        self.gridLayout_9.addWidget(self.dateEdit, 0, 1, 1, 1)

        self.dateTimeEdit = QDateTimeEdit(self.page_3)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.gridLayout_9.addWidget(self.dateTimeEdit, 1, 0, 1, 1)

        self.lcdNumber = QLCDNumber(self.page_3)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(10)
        self.lcdNumber.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.lcdNumber.setProperty(u"value", 3.141592000000000)

        self.gridLayout_9.addWidget(self.lcdNumber, 0, 2, 2, 1)

        self.calendarWidget = QCalendarWidget(self.page_3)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.gridLayout_9.addWidget(self.calendarWidget, 2, 0, 1, 3)

        self.gridLayout_9.setColumnStretch(0, 1)
        self.gridLayout_9.setColumnStretch(1, 1)
        self.gridLayout_9.setColumnStretch(2, 2)

        self.gridLayout_48.addLayout(self.gridLayout_9, 0, 1, 1, 1)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_48.addItem(self.horizontalSpacer_29, 0, 2, 1, 1)

        self.toolBox.addItem(self.page_3, u"Other Inputs")
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.page_10.setGeometry(QRect(0, 0, 1925, 447))
        self.gridLayout_33 = QGridLayout(self.page_10)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.widget_10 = QWidget(self.page_10)
        self.widget_10.setObjectName(u"widget_10")
        self.gridLayout_27 = QGridLayout(self.widget_10)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_19, 0, 2, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_30, 0, 0, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_34 = QLabel(self.widget_10)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_34)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalScrollBar_4 = QScrollBar(self.widget_10)
        self.verticalScrollBar_4.setObjectName(u"verticalScrollBar_4")
        self.verticalScrollBar_4.setEnabled(False)
        self.verticalScrollBar_4.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_7.addWidget(self.verticalScrollBar_4)

        self.verticalScrollBar_5 = QScrollBar(self.widget_10)
        self.verticalScrollBar_5.setObjectName(u"verticalScrollBar_5")
        self.verticalScrollBar_5.setEnabled(False)
        self.verticalScrollBar_5.setValue(50)
        self.verticalScrollBar_5.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_7.addWidget(self.verticalScrollBar_5)


        self.verticalLayout_13.addLayout(self.horizontalLayout_7)

        self.verticalLayout_13.setStretch(1, 1)

        self.gridLayout_27.addLayout(self.verticalLayout_13, 0, 3, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_33 = QLabel(self.widget_10)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_33)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalScrollBar = QScrollBar(self.widget_10)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_6.addWidget(self.verticalScrollBar)

        self.verticalScrollBar_3 = QScrollBar(self.widget_10)
        self.verticalScrollBar_3.setObjectName(u"verticalScrollBar_3")
        self.verticalScrollBar_3.setValue(50)
        self.verticalScrollBar_3.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_6.addWidget(self.verticalScrollBar_3)


        self.verticalLayout_12.addLayout(self.horizontalLayout_6)

        self.verticalLayout_12.setStretch(1, 1)

        self.gridLayout_27.addLayout(self.verticalLayout_12, 0, 1, 1, 1)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_32, 0, 4, 1, 1)


        self.gridLayout_33.addWidget(self.widget_10, 0, 0, 1, 1)

        self.widget_11 = QWidget(self.page_10)
        self.widget_11.setObjectName(u"widget_11")
        self.gridLayout_32 = QGridLayout(self.widget_11)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_6)

        self.label_35 = QLabel(self.widget_11)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_35)

        self.horizontalScrollBar = QScrollBar(self.widget_11)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_14.addWidget(self.horizontalScrollBar)

        self.horizontalScrollBar_3 = QScrollBar(self.widget_11)
        self.horizontalScrollBar_3.setObjectName(u"horizontalScrollBar_3")
        self.horizontalScrollBar_3.setValue(50)
        self.horizontalScrollBar_3.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_14.addWidget(self.horizontalScrollBar_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_14.addItem(self.verticalSpacer_5)

        self.label_36 = QLabel(self.widget_11)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_36)

        self.horizontalScrollBar_5 = QScrollBar(self.widget_11)
        self.horizontalScrollBar_5.setObjectName(u"horizontalScrollBar_5")
        self.horizontalScrollBar_5.setEnabled(False)
        self.horizontalScrollBar_5.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_14.addWidget(self.horizontalScrollBar_5)

        self.horizontalScrollBar_4 = QScrollBar(self.widget_11)
        self.horizontalScrollBar_4.setObjectName(u"horizontalScrollBar_4")
        self.horizontalScrollBar_4.setEnabled(False)
        self.horizontalScrollBar_4.setValue(50)
        self.horizontalScrollBar_4.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_14.addWidget(self.horizontalScrollBar_4)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_18)


        self.gridLayout_32.addLayout(self.verticalLayout_14, 0, 0, 1, 1)


        self.gridLayout_33.addWidget(self.widget_11, 0, 1, 1, 1)

        self.gridLayout_33.setColumnStretch(0, 1)
        self.gridLayout_33.setColumnStretch(1, 1)
        self.toolBox.addItem(self.page_10, u"Scroll Bars")
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.page_11.setGeometry(QRect(0, 0, 1925, 447))
        self.gridLayout_8 = QGridLayout(self.page_11)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.widget_13 = QWidget(self.page_11)
        self.widget_13.setObjectName(u"widget_13")
        self.gridLayout_50 = QGridLayout(self.widget_13)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.label_38 = QLabel(self.widget_13)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_50.addWidget(self.label_38, 1, 1, 1, 1)

        self.label_37 = QLabel(self.widget_13)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_50.addWidget(self.label_37, 1, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalSlider = QSlider(self.widget_13)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_9.addWidget(self.verticalSlider)

        self.verticalSlider_3 = QSlider(self.widget_13)
        self.verticalSlider_3.setObjectName(u"verticalSlider_3")
        self.verticalSlider_3.setValue(50)
        self.verticalSlider_3.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_9.addWidget(self.verticalSlider_3)

        self.verticalSlider_4 = QSlider(self.widget_13)
        self.verticalSlider_4.setObjectName(u"verticalSlider_4")
        self.verticalSlider_4.setOrientation(Qt.Orientation.Vertical)
        self.verticalSlider_4.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.verticalSlider_4.setTickInterval(5)

        self.horizontalLayout_9.addWidget(self.verticalSlider_4)

        self.verticalSlider_5 = QSlider(self.widget_13)
        self.verticalSlider_5.setObjectName(u"verticalSlider_5")
        self.verticalSlider_5.setValue(50)
        self.verticalSlider_5.setOrientation(Qt.Orientation.Vertical)
        self.verticalSlider_5.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.verticalSlider_5.setTickInterval(5)

        self.horizontalLayout_9.addWidget(self.verticalSlider_5)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_31)

        self.verticalSlider_7 = QSlider(self.widget_13)
        self.verticalSlider_7.setObjectName(u"verticalSlider_7")
        self.verticalSlider_7.setEnabled(False)
        self.verticalSlider_7.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_9.addWidget(self.verticalSlider_7)

        self.verticalSlider_6 = QSlider(self.widget_13)
        self.verticalSlider_6.setObjectName(u"verticalSlider_6")
        self.verticalSlider_6.setEnabled(False)
        self.verticalSlider_6.setValue(50)
        self.verticalSlider_6.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_9.addWidget(self.verticalSlider_6)

        self.verticalSlider_8 = QSlider(self.widget_13)
        self.verticalSlider_8.setObjectName(u"verticalSlider_8")
        self.verticalSlider_8.setEnabled(False)
        self.verticalSlider_8.setOrientation(Qt.Orientation.Vertical)
        self.verticalSlider_8.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.verticalSlider_8.setTickInterval(5)

        self.horizontalLayout_9.addWidget(self.verticalSlider_8)

        self.verticalSlider_9 = QSlider(self.widget_13)
        self.verticalSlider_9.setObjectName(u"verticalSlider_9")
        self.verticalSlider_9.setEnabled(False)
        self.verticalSlider_9.setValue(50)
        self.verticalSlider_9.setOrientation(Qt.Orientation.Vertical)
        self.verticalSlider_9.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.verticalSlider_9.setTickInterval(5)

        self.horizontalLayout_9.addWidget(self.verticalSlider_9)


        self.gridLayout_50.addLayout(self.horizontalLayout_9, 2, 0, 1, 2)


        self.gridLayout_8.addWidget(self.widget_13, 0, 0, 1, 1)

        self.widget_14 = QWidget(self.page_11)
        self.widget_14.setObjectName(u"widget_14")
        self.gridLayout_52 = QGridLayout(self.widget_14)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.horizontalSlider_2 = QSlider(self.widget_14)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_26.addWidget(self.horizontalSlider_2)

        self.horizontalSlider_11 = QSlider(self.widget_14)
        self.horizontalSlider_11.setObjectName(u"horizontalSlider_11")
        self.horizontalSlider_11.setValue(50)
        self.horizontalSlider_11.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_26.addWidget(self.horizontalSlider_11)

        self.horizontalSlider_10 = QSlider(self.widget_14)
        self.horizontalSlider_10.setObjectName(u"horizontalSlider_10")
        self.horizontalSlider_10.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_10.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.horizontalSlider_10.setTickInterval(5)

        self.verticalLayout_26.addWidget(self.horizontalSlider_10)

        self.horizontalSlider_12 = QSlider(self.widget_14)
        self.horizontalSlider_12.setObjectName(u"horizontalSlider_12")
        self.horizontalSlider_12.setValue(50)
        self.horizontalSlider_12.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_12.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.horizontalSlider_12.setTickInterval(5)

        self.verticalLayout_26.addWidget(self.horizontalSlider_12)


        self.gridLayout_52.addLayout(self.verticalLayout_26, 1, 0, 1, 1)

        self.label_39 = QLabel(self.widget_14)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_52.addWidget(self.label_39, 0, 0, 1, 1)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.horizontalSlider_15 = QSlider(self.widget_14)
        self.horizontalSlider_15.setObjectName(u"horizontalSlider_15")
        self.horizontalSlider_15.setEnabled(False)
        self.horizontalSlider_15.setValue(50)
        self.horizontalSlider_15.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_27.addWidget(self.horizontalSlider_15)

        self.horizontalSlider_14 = QSlider(self.widget_14)
        self.horizontalSlider_14.setObjectName(u"horizontalSlider_14")
        self.horizontalSlider_14.setEnabled(False)
        self.horizontalSlider_14.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_27.addWidget(self.horizontalSlider_14)

        self.horizontalSlider_13 = QSlider(self.widget_14)
        self.horizontalSlider_13.setObjectName(u"horizontalSlider_13")
        self.horizontalSlider_13.setEnabled(False)
        self.horizontalSlider_13.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_13.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.horizontalSlider_13.setTickInterval(5)

        self.verticalLayout_27.addWidget(self.horizontalSlider_13)

        self.horizontalSlider_16 = QSlider(self.widget_14)
        self.horizontalSlider_16.setObjectName(u"horizontalSlider_16")
        self.horizontalSlider_16.setEnabled(False)
        self.horizontalSlider_16.setValue(50)
        self.horizontalSlider_16.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_16.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.horizontalSlider_16.setTickInterval(5)

        self.verticalLayout_27.addWidget(self.horizontalSlider_16)


        self.gridLayout_52.addLayout(self.verticalLayout_27, 3, 0, 1, 1)

        self.label_40 = QLabel(self.widget_14)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_52.addWidget(self.label_40, 2, 0, 1, 1)


        self.gridLayout_8.addWidget(self.widget_14, 0, 1, 1, 1)

        self.gridLayout_8.setColumnStretch(0, 1)
        self.gridLayout_8.setColumnStretch(1, 1)
        self.toolBox.addItem(self.page_11, u"Sliders")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 1925, 447))
        self.gridLayout_13 = QGridLayout(self.page_5)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.widget = QWidget(self.page_5)
        self.widget.setObjectName(u"widget")
        self.gridLayout_10 = QGridLayout(self.widget)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_73 = QLabel(self.widget)
        self.label_73.setObjectName(u"label_73")

        self.horizontalLayout_15.addWidget(self.label_73)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_20)

        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout_3.addWidget(self.progressBar)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_21)


        self.horizontalLayout_15.addLayout(self.verticalLayout_3)


        self.gridLayout_10.addLayout(self.horizontalLayout_15, 1, 0, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_74 = QLabel(self.widget)
        self.label_74.setObjectName(u"label_74")

        self.horizontalLayout_16.addWidget(self.label_74)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_9)

        self.progressBar_2 = QProgressBar(self.widget)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setEnabled(False)
        self.progressBar_2.setValue(24)
        self.progressBar_2.setTextVisible(True)
        self.progressBar_2.setInvertedAppearance(True)

        self.verticalLayout_22.addWidget(self.progressBar_2)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_19)


        self.horizontalLayout_16.addLayout(self.verticalLayout_22)


        self.gridLayout_10.addLayout(self.horizontalLayout_16, 2, 0, 1, 1)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_24, 0, 0, 1, 1)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_25, 3, 0, 1, 1)


        self.gridLayout_13.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.page_5)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_12 = QGridLayout(self.widget_2)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_72 = QLabel(self.widget_2)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_72)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_33)

        self.progressBar_4 = QProgressBar(self.widget_2)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setEnabled(False)
        self.progressBar_4.setValue(24)
        self.progressBar_4.setTextVisible(True)
        self.progressBar_4.setOrientation(Qt.Orientation.Vertical)
        self.progressBar_4.setInvertedAppearance(True)

        self.horizontalLayout_14.addWidget(self.progressBar_4)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_34)


        self.verticalLayout_21.addLayout(self.horizontalLayout_14)


        self.gridLayout_12.addLayout(self.verticalLayout_21, 0, 2, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_53 = QLabel(self.widget_2)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_53)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.progressBar_3 = QProgressBar(self.widget_2)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setValue(24)
        self.progressBar_3.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout.addWidget(self.progressBar_3)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_18)


        self.verticalLayout_15.addLayout(self.horizontalLayout)


        self.gridLayout_12.addLayout(self.verticalLayout_15, 0, 1, 1, 1)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_35, 0, 0, 1, 1)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_36, 0, 3, 1, 1)


        self.gridLayout_13.addWidget(self.widget_2, 0, 1, 1, 1)

        self.toolBox.addItem(self.page_5, u"Progress Bar")
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.page_13.setGeometry(QRect(0, 0, 1925, 447))
        self.gridLayout_51 = QGridLayout(self.page_13)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.label_41 = QLabel(self.page_13)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_51.addWidget(self.label_41, 0, 0, 1, 1)

        self.treeWidget = QTreeWidget(self.page_13)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem1 = QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem2 = QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        __qtreewidgetitem3 = QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem3.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        __qtreewidgetitem4 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem4.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        __qtreewidgetitem5 = QTreeWidgetItem(__qtreewidgetitem4)
        __qtreewidgetitem5.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        __qtreewidgetitem6 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem7 = QTreeWidgetItem(__qtreewidgetitem6)
        __qtreewidgetitem7.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        QTreeWidgetItem(__qtreewidgetitem6)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setAlternatingRowColors(True)

        self.gridLayout_51.addWidget(self.treeWidget, 1, 0, 1, 1)

        self.treeWidget_2 = QTreeWidget(self.page_13)
        __qtreewidgetitem8 = QTreeWidgetItem(self.treeWidget_2)
        __qtreewidgetitem9 = QTreeWidgetItem(__qtreewidgetitem8)
        __qtreewidgetitem10 = QTreeWidgetItem(__qtreewidgetitem9)
        __qtreewidgetitem10.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        __qtreewidgetitem11 = QTreeWidgetItem(__qtreewidgetitem8)
        __qtreewidgetitem11.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        __qtreewidgetitem12 = QTreeWidgetItem(self.treeWidget_2)
        __qtreewidgetitem12.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        __qtreewidgetitem13 = QTreeWidgetItem(__qtreewidgetitem12)
        __qtreewidgetitem13.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        __qtreewidgetitem14 = QTreeWidgetItem(self.treeWidget_2)
        __qtreewidgetitem15 = QTreeWidgetItem(__qtreewidgetitem14)
        __qtreewidgetitem15.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        QTreeWidgetItem(__qtreewidgetitem14)
        self.treeWidget_2.setObjectName(u"treeWidget_2")
        self.treeWidget_2.setEnabled(False)
        self.treeWidget_2.setAlternatingRowColors(True)

        self.gridLayout_51.addWidget(self.treeWidget_2, 1, 1, 1, 1)

        self.treeWidget_3 = QTreeWidget(self.page_13)
        __qtreewidgetitem16 = QTreeWidgetItem(self.treeWidget_3)
        __qtreewidgetitem17 = QTreeWidgetItem(__qtreewidgetitem16)
        __qtreewidgetitem18 = QTreeWidgetItem(__qtreewidgetitem17)
        __qtreewidgetitem18.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        __qtreewidgetitem19 = QTreeWidgetItem(__qtreewidgetitem16)
        __qtreewidgetitem19.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        __qtreewidgetitem20 = QTreeWidgetItem(self.treeWidget_3)
        __qtreewidgetitem20.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        __qtreewidgetitem21 = QTreeWidgetItem(__qtreewidgetitem20)
        __qtreewidgetitem21.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        __qtreewidgetitem22 = QTreeWidgetItem(self.treeWidget_3)
        __qtreewidgetitem23 = QTreeWidgetItem(__qtreewidgetitem22)
        __qtreewidgetitem23.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        QTreeWidgetItem(__qtreewidgetitem22)
        self.treeWidget_3.setObjectName(u"treeWidget_3")
        self.treeWidget_3.setAlternatingRowColors(False)

        self.gridLayout_51.addWidget(self.treeWidget_3, 2, 0, 1, 1)

        self.treeWidget_4 = QTreeWidget(self.page_13)
        __qtreewidgetitem24 = QTreeWidgetItem(self.treeWidget_4)
        __qtreewidgetitem25 = QTreeWidgetItem(__qtreewidgetitem24)
        __qtreewidgetitem26 = QTreeWidgetItem(__qtreewidgetitem25)
        __qtreewidgetitem26.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        __qtreewidgetitem27 = QTreeWidgetItem(__qtreewidgetitem24)
        __qtreewidgetitem27.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        __qtreewidgetitem28 = QTreeWidgetItem(self.treeWidget_4)
        __qtreewidgetitem28.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        __qtreewidgetitem29 = QTreeWidgetItem(__qtreewidgetitem28)
        __qtreewidgetitem29.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        __qtreewidgetitem30 = QTreeWidgetItem(self.treeWidget_4)
        __qtreewidgetitem31 = QTreeWidgetItem(__qtreewidgetitem30)
        __qtreewidgetitem31.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        QTreeWidgetItem(__qtreewidgetitem30)
        self.treeWidget_4.setObjectName(u"treeWidget_4")
        self.treeWidget_4.setEnabled(False)

        self.gridLayout_51.addWidget(self.treeWidget_4, 2, 1, 1, 1)

        self.label_42 = QLabel(self.page_13)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_51.addWidget(self.label_42, 0, 1, 1, 2)

        self.toolBox.addItem(self.page_13, u"Tree Widget")
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.page_16.setGeometry(QRect(0, 0, 1925, 447))
        self.gridLayout_53 = QGridLayout(self.page_16)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.listWidget_7 = QListWidget(self.page_16)
        __qlistwidgetitem = QListWidgetItem(self.listWidget_7)
        __qlistwidgetitem.setCheckState(Qt.Checked);
        __qlistwidgetitem.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget_7)
        __qlistwidgetitem1.setCheckState(Qt.Unchecked);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget_7)
        __qlistwidgetitem2.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget_7)
        __qlistwidgetitem3.setCheckState(Qt.Checked);
        __qlistwidgetitem3.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget_7)
        __qlistwidgetitem4.setCheckState(Qt.Unchecked);
        __qlistwidgetitem4.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        __qlistwidgetitem5 = QListWidgetItem(self.listWidget_7)
        __qlistwidgetitem5.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem5.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        QListWidgetItem(self.listWidget_7)
        __qlistwidgetitem6 = QListWidgetItem(self.listWidget_7)
        __qlistwidgetitem6.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        self.listWidget_7.setObjectName(u"listWidget_7")
        self.listWidget_7.setEnabled(False)

        self.gridLayout_53.addWidget(self.listWidget_7, 2, 1, 1, 2)

        self.listWidget_3 = QListWidget(self.page_16)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        QListWidgetItem(self.listWidget_3)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setEnabled(False)

        self.gridLayout_53.addWidget(self.listWidget_3, 1, 5, 2, 1)

        self.listWidget_6 = QListWidget(self.page_16)
        __qlistwidgetitem7 = QListWidgetItem(self.listWidget_6)
        __qlistwidgetitem7.setCheckState(Qt.Checked);
        __qlistwidgetitem7.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem8 = QListWidgetItem(self.listWidget_6)
        __qlistwidgetitem8.setCheckState(Qt.Unchecked);
        __qlistwidgetitem9 = QListWidgetItem(self.listWidget_6)
        __qlistwidgetitem9.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem10 = QListWidgetItem(self.listWidget_6)
        __qlistwidgetitem10.setCheckState(Qt.Checked);
        __qlistwidgetitem10.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        __qlistwidgetitem11 = QListWidgetItem(self.listWidget_6)
        __qlistwidgetitem11.setCheckState(Qt.Unchecked);
        __qlistwidgetitem11.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        __qlistwidgetitem12 = QListWidgetItem(self.listWidget_6)
        __qlistwidgetitem12.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem12.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        QListWidgetItem(self.listWidget_6)
        __qlistwidgetitem13 = QListWidgetItem(self.listWidget_6)
        __qlistwidgetitem13.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        self.listWidget_6.setObjectName(u"listWidget_6")

        self.gridLayout_53.addWidget(self.listWidget_6, 2, 0, 1, 1)

        self.label_45 = QLabel(self.page_16)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_53.addWidget(self.label_45, 0, 1, 1, 2)

        self.label_65 = QLabel(self.page_16)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_53.addWidget(self.label_65, 0, 5, 1, 1)

        self.listWidget_5 = QListWidget(self.page_16)
        __qlistwidgetitem14 = QListWidgetItem(self.listWidget_5)
        __qlistwidgetitem14.setCheckState(Qt.Checked);
        __qlistwidgetitem14.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem15 = QListWidgetItem(self.listWidget_5)
        __qlistwidgetitem15.setCheckState(Qt.Unchecked);
        __qlistwidgetitem16 = QListWidgetItem(self.listWidget_5)
        __qlistwidgetitem16.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem17 = QListWidgetItem(self.listWidget_5)
        __qlistwidgetitem17.setCheckState(Qt.Checked);
        __qlistwidgetitem17.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        __qlistwidgetitem18 = QListWidgetItem(self.listWidget_5)
        __qlistwidgetitem18.setCheckState(Qt.Unchecked);
        __qlistwidgetitem18.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        __qlistwidgetitem19 = QListWidgetItem(self.listWidget_5)
        __qlistwidgetitem19.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem19.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        QListWidgetItem(self.listWidget_5)
        __qlistwidgetitem20 = QListWidgetItem(self.listWidget_5)
        __qlistwidgetitem20.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        self.listWidget_5.setObjectName(u"listWidget_5")
        self.listWidget_5.setEnabled(False)
        self.listWidget_5.setAlternatingRowColors(True)

        self.gridLayout_53.addWidget(self.listWidget_5, 1, 1, 1, 2)

        self.label_46 = QLabel(self.page_16)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_53.addWidget(self.label_46, 0, 0, 1, 1)

        self.label_64 = QLabel(self.page_16)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_53.addWidget(self.label_64, 0, 4, 1, 1)

        self.listWidget_4 = QListWidget(self.page_16)
        __qlistwidgetitem21 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem21.setCheckState(Qt.Checked);
        __qlistwidgetitem21.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qlistwidgetitem22 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem22.setCheckState(Qt.Unchecked);
        __qlistwidgetitem23 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem23.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem24 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem24.setCheckState(Qt.Checked);
        __qlistwidgetitem24.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        __qlistwidgetitem25 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem25.setCheckState(Qt.Unchecked);
        __qlistwidgetitem25.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        __qlistwidgetitem26 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem26.setCheckState(Qt.PartiallyChecked);
        __qlistwidgetitem26.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem27 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem27.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsUserCheckable);
        self.listWidget_4.setObjectName(u"listWidget_4")
        self.listWidget_4.setAlternatingRowColors(True)

        self.gridLayout_53.addWidget(self.listWidget_4, 1, 0, 1, 1)

        self.listWidget_2 = QListWidget(self.page_16)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        QListWidgetItem(self.listWidget_2)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.gridLayout_53.addWidget(self.listWidget_2, 1, 4, 2, 1)

        self.line_2 = QFrame(self.page_16)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_53.addWidget(self.line_2, 0, 3, 3, 1)

        self.toolBox.addItem(self.page_16, u"List Widget")
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.page_14.setGeometry(QRect(0, 0, 1925, 447))
        self.gridLayout_54 = QGridLayout(self.page_14)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.tableWidget_2 = QTableWidget(self.page_14)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget_2.rowCount() < 3):
            self.tableWidget_2.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem3)
        icon5 = QIcon()
        iconThemeName = u"media-playback-start"
        if QIcon.hasThemeIcon(iconThemeName):
            icon5 = QIcon.fromTheme(iconThemeName)
        else:
            icon5.addFile(u"../../../../../../.designer/backup", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setIcon(icon5);
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setCheckState(Qt.Checked);
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setCheckState(Qt.Checked);
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setCheckState(Qt.Checked);
        __qtablewidgetitem12.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(2, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(2, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_2.setItem(2, 2, __qtablewidgetitem14)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_54.addWidget(self.tableWidget_2, 2, 0, 1, 1)

        self.tableWidget_3 = QTableWidget(self.page_14)
        if (self.tableWidget_3.columnCount() < 3):
            self.tableWidget_3.setColumnCount(3)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        if (self.tableWidget_3.rowCount() < 3):
            self.tableWidget_3.setRowCount(3)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setIcon(icon5);
        self.tableWidget_3.setVerticalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setCheckState(Qt.Checked);
        self.tableWidget_3.setItem(0, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setCheckState(Qt.Checked);
        self.tableWidget_3.setItem(1, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_3.setItem(1, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_3.setItem(1, 2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setCheckState(Qt.Checked);
        __qtablewidgetitem27.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_3.setItem(2, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_3.setItem(2, 1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_3.setItem(2, 2, __qtablewidgetitem29)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setEnabled(False)
        self.tableWidget_3.setAlternatingRowColors(True)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_54.addWidget(self.tableWidget_3, 2, 1, 1, 1)

        self.tableWidget_5 = QTableWidget(self.page_14)
        if (self.tableWidget_5.columnCount() < 3):
            self.tableWidget_5.setColumnCount(3)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem32)
        if (self.tableWidget_5.rowCount() < 3):
            self.tableWidget_5.setRowCount(3)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setIcon(icon5);
        self.tableWidget_5.setVerticalHeaderItem(1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setCheckState(Qt.Checked);
        self.tableWidget_5.setItem(0, 0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_5.setItem(0, 1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_5.setItem(0, 2, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setCheckState(Qt.Checked);
        self.tableWidget_5.setItem(1, 0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_5.setItem(1, 1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_5.setItem(1, 2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setCheckState(Qt.Checked);
        __qtablewidgetitem42.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_5.setItem(2, 0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_5.setItem(2, 1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_5.setItem(2, 2, __qtablewidgetitem44)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setAlternatingRowColors(False)
        self.tableWidget_5.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_54.addWidget(self.tableWidget_5, 3, 0, 1, 1)

        self.tableWidget_4 = QTableWidget(self.page_14)
        if (self.tableWidget_4.columnCount() < 3):
            self.tableWidget_4.setColumnCount(3)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem47)
        if (self.tableWidget_4.rowCount() < 3):
            self.tableWidget_4.setRowCount(3)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setIcon(icon5);
        self.tableWidget_4.setVerticalHeaderItem(1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(2, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setCheckState(Qt.Checked);
        self.tableWidget_4.setItem(0, 0, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget_4.setItem(0, 1, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget_4.setItem(0, 2, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setCheckState(Qt.Checked);
        self.tableWidget_4.setItem(1, 0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableWidget_4.setItem(1, 1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget_4.setItem(1, 2, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setCheckState(Qt.Checked);
        __qtablewidgetitem57.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_4.setItem(2, 0, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_4.setItem(2, 1, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable);
        self.tableWidget_4.setItem(2, 2, __qtablewidgetitem59)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setEnabled(False)
        self.tableWidget_4.setAlternatingRowColors(False)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_54.addWidget(self.tableWidget_4, 3, 1, 1, 1)

        self.label_48 = QLabel(self.page_14)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_54.addWidget(self.label_48, 0, 0, 2, 1)

        self.label_47 = QLabel(self.page_14)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_54.addWidget(self.label_47, 0, 1, 2, 1)

        self.toolBox.addItem(self.page_14, u"Table Widget")
        self.page_26 = QWidget()
        self.page_26.setObjectName(u"page_26")
        self.page_26.setGeometry(QRect(0, 0, 1925, 447))
        self.gridLayout = QGridLayout(self.page_26)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_43 = QLabel(self.page_26)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_43, 0, 1, 1, 1)

        self.plainTextEdit_2 = QPlainTextEdit(self.page_26)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setEnabled(False)

        self.gridLayout.addWidget(self.plainTextEdit_2, 2, 1, 1, 1)

        self.label_44 = QLabel(self.page_26)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_44, 0, 2, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.page_26)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout.addWidget(self.plainTextEdit, 1, 1, 1, 1)

        self.textEdit = QTextEdit(self.page_26)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 1, 2, 1, 1)

        self.textEdit_2 = QTextEdit(self.page_26)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setEnabled(False)

        self.gridLayout.addWidget(self.textEdit_2, 2, 2, 1, 1)

        self.label_49 = QLabel(self.page_26)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout.addWidget(self.label_49, 1, 0, 1, 1)

        self.label_50 = QLabel(self.page_26)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout.addWidget(self.label_50, 2, 0, 1, 1)

        self.toolBox.addItem(self.page_26, u"TextEdits")
        self.page_17 = QWidget()
        self.page_17.setObjectName(u"page_17")
        self.page_17.setGeometry(QRect(0, 0, 1925, 447))
        self.gridLayout_5 = QGridLayout(self.page_17)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.widget_12 = QWidget(self.page_17)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_2 = QGridLayout(self.widget_12)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line_8 = QFrame(self.widget_12)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_8, 0, 0, 1, 1)

        self.line_9 = QFrame(self.widget_12)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_9, 1, 0, 1, 1)

        self.line_7 = QFrame(self.widget_12)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_7, 2, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_12, 0, 0, 1, 1)

        self.widget_15 = QWidget(self.page_17)
        self.widget_15.setObjectName(u"widget_15")
        self.gridLayout_3 = QGridLayout(self.widget_15)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.line_10 = QFrame(self.widget_15)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_10, 0, 0, 1, 1)

        self.line_11 = QFrame(self.widget_15)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_11, 0, 1, 1, 1)

        self.line_12 = QFrame(self.widget_15)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.VLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_12, 0, 2, 1, 1)


        self.gridLayout_5.addWidget(self.widget_15, 0, 1, 1, 1)

        self.toolBox.addItem(self.page_17, u"Lines/Separators")
        self.page_24 = QWidget()
        self.page_24.setObjectName(u"page_24")
        self.page_24.setGeometry(QRect(0, 0, 1925, 447))
        self.gridLayout_25 = QGridLayout(self.page_24)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_file_dialog = QPushButton(self.page_24)
        self.pushButton_file_dialog.setObjectName(u"pushButton_file_dialog")

        self.horizontalLayout_3.addWidget(self.pushButton_file_dialog)

        self.pushButton_folder_dialog = QPushButton(self.page_24)
        self.pushButton_folder_dialog.setObjectName(u"pushButton_folder_dialog")

        self.horizontalLayout_3.addWidget(self.pushButton_folder_dialog)


        self.gridLayout_25.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)

        self.verticalSpacer_16 = QSpacerItem(741, 127, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_25.addItem(self.verticalSpacer_16, 0, 0, 1, 2)

        self.verticalSpacer_17 = QSpacerItem(741, 126, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_25.addItem(self.verticalSpacer_17, 2, 0, 1, 2)

        self.toolBox.addItem(self.page_24, u"Dialogs")
        self.page_25 = QWidget()
        self.page_25.setObjectName(u"page_25")
        self.page_25.setGeometry(QRect(0, 0, 1925, 447))
        self.gridLayout_7 = QGridLayout(self.page_25)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.groupBox_20 = QGroupBox(self.page_25)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setEnabled(False)
        self.groupBox_20.setFlat(True)
        self.groupBox_20.setCheckable(True)
        self.groupBox_20.setChecked(True)
        self.groupBox_20.setProperty(u"frameless", True)
        self.gridLayout_67 = QGridLayout(self.groupBox_20)
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.label_69 = QLabel(self.groupBox_20)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_67.addWidget(self.label_69, 0, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.groupBox_20)

        self.groupBox_21 = QGroupBox(self.page_25)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setEnabled(False)
        self.groupBox_21.setFlat(True)
        self.groupBox_21.setCheckable(True)
        self.groupBox_21.setChecked(False)
        self.groupBox_21.setProperty(u"frameless", True)
        self.gridLayout_68 = QGridLayout(self.groupBox_21)
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.label_70 = QLabel(self.groupBox_21)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_68.addWidget(self.label_70, 0, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.groupBox_21)

        self.groupBox_22 = QGroupBox(self.page_25)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.groupBox_22.setEnabled(False)
        self.groupBox_22.setFlat(True)
        self.groupBox_22.setProperty(u"frameless", True)
        self.gridLayout_69 = QGridLayout(self.groupBox_22)
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.label_71 = QLabel(self.groupBox_22)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_69.addWidget(self.label_71, 0, 0, 1, 1)

        self.label_52 = QLabel(self.groupBox_22)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_69.addWidget(self.label_52, 2, 0, 1, 1)

        self.line_4 = QFrame(self.groupBox_22)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_69.addWidget(self.line_4, 1, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.groupBox_22)


        self.gridLayout_7.addLayout(self.verticalLayout_10, 0, 3, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_17 = QGroupBox(self.page_25)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setEnabled(False)
        self.groupBox_17.setCheckable(True)
        self.gridLayout_64 = QGridLayout(self.groupBox_17)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.label_66 = QLabel(self.groupBox_17)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_64.addWidget(self.label_66, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.groupBox_17)

        self.groupBox_18 = QGroupBox(self.page_25)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setEnabled(False)
        self.groupBox_18.setCheckable(True)
        self.groupBox_18.setChecked(False)
        self.gridLayout_65 = QGridLayout(self.groupBox_18)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.label_67 = QLabel(self.groupBox_18)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_65.addWidget(self.label_67, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.groupBox_18)

        self.groupBox_19 = QGroupBox(self.page_25)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setEnabled(False)
        self.gridLayout_66 = QGridLayout(self.groupBox_19)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.label_68 = QLabel(self.groupBox_19)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_66.addWidget(self.label_68, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.groupBox_19)


        self.gridLayout_7.addLayout(self.verticalLayout_9, 0, 2, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_11 = QGroupBox(self.page_25)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setCheckable(True)
        self.gridLayout_34 = QGridLayout(self.groupBox_11)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.label_17 = QLabel(self.groupBox_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_34.addWidget(self.label_17, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_11)

        self.groupBox_15 = QGroupBox(self.page_25)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setCheckable(True)
        self.groupBox_15.setChecked(False)
        self.gridLayout_35 = QGridLayout(self.groupBox_15)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.label_18 = QLabel(self.groupBox_15)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_35.addWidget(self.label_18, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_15)

        self.groupBox_12 = QGroupBox(self.page_25)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.gridLayout_40 = QGridLayout(self.groupBox_12)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.label_19 = QLabel(self.groupBox_12)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_40.addWidget(self.label_19, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_12)


        self.gridLayout_7.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_16 = QGroupBox(self.page_25)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setFlat(True)
        self.groupBox_16.setCheckable(True)
        self.groupBox_16.setChecked(True)
        self.groupBox_16.setProperty(u"frameless", True)
        self.gridLayout_45 = QGridLayout(self.groupBox_16)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.label_21 = QLabel(self.groupBox_16)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_45.addWidget(self.label_21, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox_16)

        self.groupBox_14 = QGroupBox(self.page_25)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setFlat(True)
        self.groupBox_14.setCheckable(True)
        self.groupBox_14.setChecked(False)
        self.groupBox_14.setProperty(u"frameless", True)
        self.gridLayout_46 = QGridLayout(self.groupBox_14)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.label_22 = QLabel(self.groupBox_14)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_46.addWidget(self.label_22, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox_14)

        self.groupBox_13 = QGroupBox(self.page_25)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setFlat(True)
        self.groupBox_13.setProperty(u"frameless", True)
        self.gridLayout_43 = QGridLayout(self.groupBox_13)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.label_20 = QLabel(self.groupBox_13)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_43.addWidget(self.label_20, 0, 0, 1, 1)

        self.label_32 = QLabel(self.groupBox_13)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_43.addWidget(self.label_32, 2, 0, 1, 1)

        self.line_3 = QFrame(self.groupBox_13)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_43.addWidget(self.line_3, 1, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox_13)


        self.gridLayout_7.addLayout(self.verticalLayout_5, 0, 1, 1, 1)

        self.toolBox.addItem(self.page_25, u"Group Boxes")
        self.page_27 = QWidget()
        self.page_27.setObjectName(u"page_27")
        self.page_27.setGeometry(QRect(0, 0, 1925, 447))
        self.gridLayout_6 = QGridLayout(self.page_27)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame = QFrame(self.page_27)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame.setProperty(u"frameless", True)
        self.gridLayout_23 = QGridLayout(self.frame)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_23.addWidget(self.label_16, 0, 0, 1, 1)

        self.label_26 = QLabel(self.frame)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_23.addWidget(self.label_26, 2, 0, 1, 1)

        self.line_6 = QFrame(self.frame)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_23.addWidget(self.line_6, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_16 = QFrame(self.page_27)
        self.frame_16.setObjectName(u"frame_16")
        self.gridLayout_44 = QGridLayout(self.frame_16)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.label_51 = QLabel(self.frame_16)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_44.addWidget(self.label_51, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_16, 0, 1, 1, 1)

        self.frame_19 = QFrame(self.page_27)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setProperty(u"colored", True)
        self.gridLayout_57 = QGridLayout(self.frame_19)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.label_27 = QLabel(self.frame_19)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_57.addWidget(self.label_27, 2, 0, 1, 1)

        self.label_54 = QLabel(self.frame_19)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_57.addWidget(self.label_54, 0, 0, 1, 1)

        self.line_13 = QFrame(self.frame_19)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.Shape.HLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_57.addWidget(self.line_13, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_19, 0, 2, 1, 1)

        self.frame_2 = QFrame(self.page_27)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(False)
        self.frame_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame_2.setProperty(u"frameless", True)
        self.gridLayout_24 = QGridLayout(self.frame_2)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.label_25 = QLabel(self.frame_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_24.addWidget(self.label_25, 0, 0, 1, 1)

        self.label_28 = QLabel(self.frame_2)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_24.addWidget(self.label_28, 2, 0, 1, 1)

        self.line_5 = QFrame(self.frame_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_24.addWidget(self.line_5, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame_6 = QFrame(self.page_27)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setEnabled(False)
        self.gridLayout_31 = QGridLayout(self.frame_6)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.label_29 = QLabel(self.frame_6)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_31.addWidget(self.label_29, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_6, 1, 1, 1, 1)

        self.frame_8 = QFrame(self.page_27)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setEnabled(False)
        self.frame_8.setProperty(u"colored", True)
        self.gridLayout_26 = QGridLayout(self.frame_8)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.label_31 = QLabel(self.frame_8)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_26.addWidget(self.label_31, 0, 0, 1, 1)

        self.label_30 = QLabel(self.frame_8)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_26.addWidget(self.label_30, 2, 0, 1, 1)

        self.line_14 = QFrame(self.frame_8)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.Shape.HLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_26.addWidget(self.line_14, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_8, 1, 2, 1, 1)

        self.toolBox.addItem(self.page_27, u"QFrame")

        self.gridLayout_22.addWidget(self.toolBox, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_40 = QWidget()
        self.page_40.setObjectName(u"page_40")
        self.gridLayout_113 = QGridLayout(self.page_40)
        self.gridLayout_113.setObjectName(u"gridLayout_113")
        self.tabWidget_7 = QTabWidget(self.page_40)
        self.tabWidget_7.setObjectName(u"tabWidget_7")
        self.tab_38 = QWidget()
        self.tab_38.setObjectName(u"tab_38")
        self.tabWidget_7.addTab(self.tab_38, "")
        self.tab_39 = QWidget()
        self.tab_39.setObjectName(u"tab_39")
        self.tabWidget_7.addTab(self.tab_39, "")
        self.tab_40 = QWidget()
        self.tab_40.setObjectName(u"tab_40")
        self.tabWidget_7.addTab(self.tab_40, "")
        self.tab_41 = QWidget()
        self.tab_41.setObjectName(u"tab_41")
        self.gridLayout_108 = QGridLayout(self.tab_41)
        self.gridLayout_108.setObjectName(u"gridLayout_108")
        self.tabWidget_6 = QTabWidget(self.tab_41)
        self.tabWidget_6.setObjectName(u"tabWidget_6")
        self.tabWidget_6.setTabPosition(QTabWidget.TabPosition.South)
        self.tabWidget_6.setTabsClosable(True)
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
        self.gridLayout_109 = QGridLayout(self.tab_37)
        self.gridLayout_109.setObjectName(u"gridLayout_109")
        self.tabWidget_8 = QTabWidget(self.tab_37)
        self.tabWidget_8.setObjectName(u"tabWidget_8")
        self.tabWidget_8.setTabPosition(QTabWidget.TabPosition.West)
        self.tab_45 = QWidget()
        self.tab_45.setObjectName(u"tab_45")
        self.gridLayout_112 = QGridLayout(self.tab_45)
        self.gridLayout_112.setObjectName(u"gridLayout_112")
        self.tabWidget_9 = QTabWidget(self.tab_45)
        self.tabWidget_9.setObjectName(u"tabWidget_9")
        self.tabWidget_9.setTabPosition(QTabWidget.TabPosition.East)
        self.tabWidget_9.setTabsClosable(True)
        self.tab_52 = QWidget()
        self.tab_52.setObjectName(u"tab_52")
        self.tabWidget_9.addTab(self.tab_52, "")
        self.tab_53 = QWidget()
        self.tab_53.setObjectName(u"tab_53")
        self.tabWidget_9.addTab(self.tab_53, "")
        self.tab_54 = QWidget()
        self.tab_54.setObjectName(u"tab_54")
        self.tabWidget_9.addTab(self.tab_54, "")
        self.tab_55 = QWidget()
        self.tab_55.setObjectName(u"tab_55")
        self.tabWidget_9.addTab(self.tab_55, "")
        self.tab_56 = QWidget()
        self.tab_56.setObjectName(u"tab_56")
        self.tabWidget_9.addTab(self.tab_56, "")
        self.tab_57 = QWidget()
        self.tab_57.setObjectName(u"tab_57")
        self.tabWidget_9.addTab(self.tab_57, "")
        self.tab_58 = QWidget()
        self.tab_58.setObjectName(u"tab_58")
        self.tabWidget_9.addTab(self.tab_58, "")

        self.gridLayout_112.addWidget(self.tabWidget_9, 0, 0, 1, 1)

        self.tabWidget_8.addTab(self.tab_45, "")
        self.tab_46 = QWidget()
        self.tab_46.setObjectName(u"tab_46")
        self.tabWidget_8.addTab(self.tab_46, "")
        self.tab_47 = QWidget()
        self.tab_47.setObjectName(u"tab_47")
        self.tabWidget_8.addTab(self.tab_47, "")
        self.tab_48 = QWidget()
        self.tab_48.setObjectName(u"tab_48")
        self.gridLayout_110 = QGridLayout(self.tab_48)
        self.gridLayout_110.setObjectName(u"gridLayout_110")
        self.tabWidget_8.addTab(self.tab_48, "")
        self.tab_49 = QWidget()
        self.tab_49.setObjectName(u"tab_49")
        self.tabWidget_8.addTab(self.tab_49, "")
        self.tab_50 = QWidget()
        self.tab_50.setObjectName(u"tab_50")
        self.tabWidget_8.addTab(self.tab_50, "")
        self.tab_51 = QWidget()
        self.tab_51.setObjectName(u"tab_51")
        self.tabWidget_8.addTab(self.tab_51, "")

        self.gridLayout_109.addWidget(self.tabWidget_8, 0, 0, 1, 1)

        self.tabWidget_6.addTab(self.tab_37, "")

        self.gridLayout_108.addWidget(self.tabWidget_6, 0, 0, 1, 1)

        self.tabWidget_7.addTab(self.tab_41, "")
        self.tab_42 = QWidget()
        self.tab_42.setObjectName(u"tab_42")
        self.tabWidget_7.addTab(self.tab_42, "")
        self.tab_43 = QWidget()
        self.tab_43.setObjectName(u"tab_43")
        self.tabWidget_7.addTab(self.tab_43, "")
        self.tab_44 = QWidget()
        self.tab_44.setObjectName(u"tab_44")
        self.tabWidget_7.addTab(self.tab_44, "")

        self.gridLayout_113.addWidget(self.tabWidget_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_40)
        self.page_39 = QWidget()
        self.page_39.setObjectName(u"page_39")
        self.gridLayout_14 = QGridLayout(self.page_39)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.mdiArea = QMdiArea(self.page_39)
        self.mdiArea.setObjectName(u"mdiArea")
        self.subwindow = QWidget()
        self.subwindow.setObjectName(u"subwindow")
        self.gridLayout_15 = QGridLayout(self.subwindow)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.pushButton = QPushButton(self.subwindow)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_15.addWidget(self.pushButton, 2, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.subwindow)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(True)

        self.gridLayout_15.addWidget(self.pushButton_2, 2, 1, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.subwindow)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.label_2 = QLabel(self.subwindow)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.label_3 = QLabel(self.subwindow)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.label_14 = QLabel(self.subwindow)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_14)

        self.lineEdit = QLineEdit(self.subwindow)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit)

        self.spinBox = QSpinBox(self.subwindow)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setValue(27)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinBox)

        self.comboBox = QComboBox(self.subwindow)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.comboBox)

        self.radioButton = QRadioButton(self.subwindow)
        self.radioButton.setObjectName(u"radioButton")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.radioButton)

        self.radioButton_2 = QRadioButton(self.subwindow)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setChecked(True)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.subwindow)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.radioButton_3)


        self.gridLayout_15.addLayout(self.formLayout, 0, 0, 1, 2)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_11, 1, 0, 1, 2)

        self.mdiArea.addSubWindow(self.subwindow)
        self.subwindow_2 = QWidget()
        self.subwindow_2.setObjectName(u"subwindow_2")
        self.gridLayout_58 = QGridLayout(self.subwindow_2)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.tabWidget = QTabWidget(self.subwindow_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(393, 0))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_6 = QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.checkBox = QCheckBox(self.tab)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.verticalLayout_6.addWidget(self.checkBox)

        self.pushButton_5 = QPushButton(self.tab)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_6.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.tab)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setChecked(True)

        self.verticalLayout_6.addWidget(self.pushButton_6)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_58.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.mdiArea.addSubWindow(self.subwindow_2)
        self.subwindow_3 = QWidget()
        self.subwindow_3.setObjectName(u"subwindow_3")
        self.gridLayout_17 = QGridLayout(self.subwindow_3)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pushButton_7 = QPushButton(self.subwindow_3)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_8.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.subwindow_3)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_8.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.subwindow_3)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout_8.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.subwindow_3)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setChecked(True)

        self.verticalLayout_8.addWidget(self.pushButton_10)


        self.gridLayout_17.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.subwindow_3)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_59 = QGridLayout(self.groupBox)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.radioButton_4 = QRadioButton(self.groupBox)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setChecked(True)

        self.gridLayout_59.addWidget(self.radioButton_4, 0, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_59.addWidget(self.checkBox_2, 0, 1, 1, 1)

        self.checkBox_3 = QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setChecked(True)

        self.gridLayout_59.addWidget(self.checkBox_3, 1, 1, 2, 1)

        self.radioButton_9 = QRadioButton(self.groupBox)
        self.radioButton_9.setObjectName(u"radioButton_9")

        self.gridLayout_59.addWidget(self.radioButton_9, 1, 0, 2, 1)


        self.gridLayout_17.addWidget(self.groupBox, 0, 1, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_60 = QLabel(self.subwindow_3)
        self.label_60.setObjectName(u"label_60")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_60)

        self.lineEdit_3 = QLineEdit(self.subwindow_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_3)

        self.label_61 = QLabel(self.subwindow_3)
        self.label_61.setObjectName(u"label_61")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_61)

        self.spinBox_2 = QSpinBox(self.subwindow_3)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setValue(5)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinBox_2)

        self.label_62 = QLabel(self.subwindow_3)
        self.label_62.setObjectName(u"label_62")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_62)

        self.comboBox_3 = QComboBox(self.subwindow_3)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.comboBox_3)


        self.gridLayout_17.addLayout(self.formLayout_2, 1, 0, 1, 2)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_63 = QLabel(self.subwindow_3)
        self.label_63.setObjectName(u"label_63")

        self.horizontalLayout_13.addWidget(self.label_63)

        self.progressBar_5 = QProgressBar(self.subwindow_3)
        self.progressBar_5.setObjectName(u"progressBar_5")
        self.progressBar_5.setValue(40)

        self.horizontalLayout_13.addWidget(self.progressBar_5)


        self.gridLayout_17.addLayout(self.horizontalLayout_13, 2, 0, 1, 2)

        self.mdiArea.addSubWindow(self.subwindow_3)
        self.subwindow_4 = QWidget()
        self.subwindow_4.setObjectName(u"subwindow_4")
        self.gridLayout_63 = QGridLayout(self.subwindow_4)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.listWidget = QListWidget(self.subwindow_4)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QSize(115, 0))

        self.horizontalLayout_12.addWidget(self.listWidget)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_3 = QWidget(self.subwindow_4)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_61 = QGridLayout(self.widget_3)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_15 = QLabel(self.widget_3)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_4.addWidget(self.label_15)

        self.lineEdit_2 = QLineEdit(self.widget_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_4.addWidget(self.lineEdit_2)


        self.gridLayout_61.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_55 = QLabel(self.widget_3)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_8.addWidget(self.label_55)

        self.comboBox_2 = QComboBox(self.widget_3)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_8.addWidget(self.comboBox_2)


        self.gridLayout_61.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_56 = QLabel(self.widget_3)
        self.label_56.setObjectName(u"label_56")

        self.horizontalLayout_10.addWidget(self.label_56)

        self.horizontalSlider = QSlider(self.widget_3)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximum(20)
        self.horizontalSlider.setValue(6)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_10.addWidget(self.horizontalSlider)

        self.label_57 = QLabel(self.widget_3)
        self.label_57.setObjectName(u"label_57")

        self.horizontalLayout_10.addWidget(self.label_57)


        self.gridLayout_61.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.widget_3)

        self.line = QFrame(self.subwindow_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line)

        self.groupBox_2 = QGroupBox(self.subwindow_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFlat(True)
        self.gridLayout_62 = QGridLayout(self.groupBox_2)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.checkBox_4 = QCheckBox(self.groupBox_2)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setChecked(True)

        self.gridLayout_62.addWidget(self.checkBox_4, 0, 0, 1, 1)

        self.checkBox_9 = QCheckBox(self.groupBox_2)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.gridLayout_62.addWidget(self.checkBox_9, 1, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_58 = QLabel(self.subwindow_4)
        self.label_58.setObjectName(u"label_58")

        self.horizontalLayout_11.addWidget(self.label_58)

        self.horizontalSpacer_2 = QSpacerItem(300, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_2)

        self.label_59 = QLabel(self.subwindow_4)
        self.label_59.setObjectName(u"label_59")

        self.horizontalLayout_11.addWidget(self.label_59)

        self.horizontalSlider_3 = QSlider(self.subwindow_4)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(50)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontalSlider_3.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_3.setSizePolicy(sizePolicy1)
        self.horizontalSlider_3.setMaximumSize(QSize(50, 16777215))
        self.horizontalSlider_3.setMaximum(1)
        self.horizontalSlider_3.setPageStep(1)
        self.horizontalSlider_3.setValue(1)
        self.horizontalSlider_3.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_11.addWidget(self.horizontalSlider_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_12.addLayout(self.verticalLayout_7)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 3)

        self.gridLayout_63.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)

        self.mdiArea.addSubWindow(self.subwindow_4)
        self.subwindow_5 = QWidget()
        self.subwindow_5.setObjectName(u"subwindow_5")
        self.gridLayout_39 = QGridLayout(self.subwindow_5)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_76 = QLabel(self.subwindow_5)
        self.label_76.setObjectName(u"label_76")

        self.verticalLayout_23.addWidget(self.label_76)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lineEdit_4 = QLineEdit(self.subwindow_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_17.addWidget(self.lineEdit_4)

        self.pushButton_11 = QPushButton(self.subwindow_5)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_17.addWidget(self.pushButton_11)


        self.verticalLayout_23.addLayout(self.horizontalLayout_17)


        self.gridLayout_39.addLayout(self.verticalLayout_23, 0, 0, 1, 1)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_77 = QLabel(self.subwindow_5)
        self.label_77.setObjectName(u"label_77")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_77)

        self.comboBox_4 = QComboBox(self.subwindow_5)
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboBox_4)

        self.label_78 = QLabel(self.subwindow_5)
        self.label_78.setObjectName(u"label_78")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_78)

        self.comboBox_5 = QComboBox(self.subwindow_5)
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.FieldRole, self.comboBox_5)


        self.gridLayout_39.addLayout(self.formLayout_4, 1, 0, 1, 1)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_79 = QLabel(self.subwindow_5)
        self.label_79.setObjectName(u"label_79")

        self.verticalLayout_24.addWidget(self.label_79)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.checkBox_10 = QCheckBox(self.subwindow_5)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setChecked(True)

        self.horizontalLayout_21.addWidget(self.checkBox_10)

        self.checkBox_11 = QCheckBox(self.subwindow_5)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.horizontalLayout_21.addWidget(self.checkBox_11)


        self.verticalLayout_24.addLayout(self.horizontalLayout_21)

        self.verticalLayout_24.setStretch(1, 1)

        self.gridLayout_39.addLayout(self.verticalLayout_24, 2, 0, 1, 1)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_81 = QLabel(self.subwindow_5)
        self.label_81.setObjectName(u"label_81")

        self.verticalLayout_25.addWidget(self.label_81)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.radioButton_11 = QRadioButton(self.subwindow_5)
        self.radioButton_11.setObjectName(u"radioButton_11")

        self.horizontalLayout_22.addWidget(self.radioButton_11)

        self.radioButton_12 = QRadioButton(self.subwindow_5)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setChecked(True)

        self.horizontalLayout_22.addWidget(self.radioButton_12)


        self.verticalLayout_25.addLayout(self.horizontalLayout_22)

        self.verticalLayout_25.setStretch(1, 1)

        self.gridLayout_39.addLayout(self.verticalLayout_25, 3, 0, 1, 1)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.pushButton_12 = QPushButton(self.subwindow_5)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.horizontalLayout_23.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.subwindow_5)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setChecked(True)

        self.horizontalLayout_23.addWidget(self.pushButton_13)


        self.gridLayout_39.addLayout(self.horizontalLayout_23, 4, 0, 1, 1)

        self.mdiArea.addSubWindow(self.subwindow_5)
        self.subwindow_6 = QWidget()
        self.subwindow_6.setObjectName(u"subwindow_6")
        self.gridLayout_41 = QGridLayout(self.subwindow_6)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.label_80 = QLabel(self.subwindow_6)
        self.label_80.setObjectName(u"label_80")

        self.gridLayout_41.addWidget(self.label_80, 0, 0, 1, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.listWidget_8 = QListWidget(self.subwindow_6)
        QListWidgetItem(self.listWidget_8)
        QListWidgetItem(self.listWidget_8)
        QListWidgetItem(self.listWidget_8)
        QListWidgetItem(self.listWidget_8)
        self.listWidget_8.setObjectName(u"listWidget_8")

        self.horizontalLayout_20.addWidget(self.listWidget_8)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.pushButton_14 = QPushButton(self.subwindow_6)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.verticalLayout_28.addWidget(self.pushButton_14)

        self.pushButton_15 = QPushButton(self.subwindow_6)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.verticalLayout_28.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.subwindow_6)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.verticalLayout_28.addWidget(self.pushButton_16)

        self.pushButton_17 = QPushButton(self.subwindow_6)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setCheckable(True)
        self.pushButton_17.setChecked(True)

        self.verticalLayout_28.addWidget(self.pushButton_17)

        self.pushButton_34 = QPushButton(self.subwindow_6)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setCheckable(True)
        self.pushButton_34.setChecked(True)

        self.verticalLayout_28.addWidget(self.pushButton_34)


        self.horizontalLayout_20.addLayout(self.verticalLayout_28)

        self.horizontalLayout_20.setStretch(0, 1)
        self.horizontalLayout_20.setStretch(1, 2)

        self.gridLayout_41.addLayout(self.horizontalLayout_20, 1, 0, 1, 2)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_82 = QLabel(self.subwindow_6)
        self.label_82.setObjectName(u"label_82")

        self.verticalLayout_29.addWidget(self.label_82)

        self.plainTextEdit_3 = QPlainTextEdit(self.subwindow_6)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")

        self.verticalLayout_29.addWidget(self.plainTextEdit_3)


        self.gridLayout_41.addLayout(self.verticalLayout_29, 2, 0, 1, 2)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_37)

        self.pushButton_35 = QPushButton(self.subwindow_6)
        self.pushButton_35.setObjectName(u"pushButton_35")

        self.horizontalLayout_18.addWidget(self.pushButton_35)

        self.pushButton_36 = QPushButton(self.subwindow_6)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setCheckable(True)
        self.pushButton_36.setChecked(True)

        self.horizontalLayout_18.addWidget(self.pushButton_36)


        self.gridLayout_41.addLayout(self.horizontalLayout_18, 3, 1, 1, 1)

        self.mdiArea.addSubWindow(self.subwindow_6)
        self.subwindow_7 = QWidget()
        self.subwindow_7.setObjectName(u"subwindow_7")
        self.gridLayout_42 = QGridLayout(self.subwindow_7)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_83 = QLabel(self.subwindow_7)
        self.label_83.setObjectName(u"label_83")

        self.horizontalLayout_24.addWidget(self.label_83)

        self.progressBar_6 = QProgressBar(self.subwindow_7)
        self.progressBar_6.setObjectName(u"progressBar_6")
        self.progressBar_6.setValue(24)

        self.horizontalLayout_24.addWidget(self.progressBar_6)


        self.gridLayout_42.addLayout(self.horizontalLayout_24, 0, 0, 1, 1)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_84 = QLabel(self.subwindow_7)
        self.label_84.setObjectName(u"label_84")

        self.horizontalLayout_25.addWidget(self.label_84)

        self.progressBar_7 = QProgressBar(self.subwindow_7)
        self.progressBar_7.setObjectName(u"progressBar_7")
        self.progressBar_7.setValue(85)

        self.horizontalLayout_25.addWidget(self.progressBar_7)


        self.gridLayout_42.addLayout(self.horizontalLayout_25, 1, 0, 1, 1)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_85 = QLabel(self.subwindow_7)
        self.label_85.setObjectName(u"label_85")

        self.horizontalLayout_26.addWidget(self.label_85)

        self.progressBar_8 = QProgressBar(self.subwindow_7)
        self.progressBar_8.setObjectName(u"progressBar_8")
        self.progressBar_8.setValue(69)

        self.horizontalLayout_26.addWidget(self.progressBar_8)


        self.gridLayout_42.addLayout(self.horizontalLayout_26, 2, 0, 1, 1)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_86 = QLabel(self.subwindow_7)
        self.label_86.setObjectName(u"label_86")

        self.horizontalLayout_27.addWidget(self.label_86)

        self.progressBar_9 = QProgressBar(self.subwindow_7)
        self.progressBar_9.setObjectName(u"progressBar_9")
        self.progressBar_9.setValue(37)

        self.horizontalLayout_27.addWidget(self.progressBar_9)


        self.gridLayout_42.addLayout(self.horizontalLayout_27, 3, 0, 1, 1)

        self.mdiArea.addSubWindow(self.subwindow_7)
        self.subwindow_8 = QWidget()
        self.subwindow_8.setObjectName(u"subwindow_8")
        self.gridLayout_49 = QGridLayout(self.subwindow_8)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.label_87 = QLabel(self.subwindow_8)
        self.label_87.setObjectName(u"label_87")

        self.gridLayout_49.addWidget(self.label_87, 0, 0, 1, 1)

        self.calendarWidget_3 = QCalendarWidget(self.subwindow_8)
        self.calendarWidget_3.setObjectName(u"calendarWidget_3")

        self.gridLayout_49.addWidget(self.calendarWidget_3, 1, 0, 1, 1)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_88 = QLabel(self.subwindow_8)
        self.label_88.setObjectName(u"label_88")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_88)

        self.timeEdit_2 = QTimeEdit(self.subwindow_8)
        self.timeEdit_2.setObjectName(u"timeEdit_2")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.FieldRole, self.timeEdit_2)

        self.label_89 = QLabel(self.subwindow_8)
        self.label_89.setObjectName(u"label_89")

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_89)

        self.spinBox_3 = QSpinBox(self.subwindow_8)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinBox_3)

        self.label_90 = QLabel(self.subwindow_8)
        self.label_90.setObjectName(u"label_90")

        self.formLayout_5.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_90)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.radioButton_10 = QRadioButton(self.subwindow_8)
        self.radioButton_10.setObjectName(u"radioButton_10")

        self.horizontalLayout_28.addWidget(self.radioButton_10)

        self.radioButton_13 = QRadioButton(self.subwindow_8)
        self.radioButton_13.setObjectName(u"radioButton_13")
        self.radioButton_13.setChecked(True)

        self.horizontalLayout_28.addWidget(self.radioButton_13)


        self.formLayout_5.setLayout(2, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_28)

        self.label_91 = QLabel(self.subwindow_8)
        self.label_91.setObjectName(u"label_91")

        self.formLayout_5.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_91)

        self.checkBox_12 = QCheckBox(self.subwindow_8)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.formLayout_5.setWidget(3, QFormLayout.ItemRole.FieldRole, self.checkBox_12)


        self.gridLayout_49.addLayout(self.formLayout_5, 2, 0, 1, 1)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_38)

        self.pushButton_37 = QPushButton(self.subwindow_8)
        self.pushButton_37.setObjectName(u"pushButton_37")

        self.horizontalLayout_29.addWidget(self.pushButton_37)

        self.pushButton_38 = QPushButton(self.subwindow_8)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setCheckable(True)
        self.pushButton_38.setChecked(True)

        self.horizontalLayout_29.addWidget(self.pushButton_38)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_39)


        self.gridLayout_49.addLayout(self.horizontalLayout_29, 3, 0, 1, 1)

        self.mdiArea.addSubWindow(self.subwindow_8)
        self.subwindow_9 = QWidget()
        self.subwindow_9.setObjectName(u"subwindow_9")
        self.gridLayout_55 = QGridLayout(self.subwindow_9)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.pushButton_39 = QPushButton(self.subwindow_9)
        self.pushButton_39.setObjectName(u"pushButton_39")

        self.gridLayout_55.addWidget(self.pushButton_39, 0, 0, 1, 1)

        self.mdiArea.addSubWindow(self.subwindow_9)

        self.gridLayout_14.addWidget(self.mdiArea, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_39)

        self.gridLayout_11.addWidget(self.stackedWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.toolBar_vertical = QToolBar(MainWindow)
        self.toolBar_vertical.setObjectName(u"toolBar_vertical")
        MainWindow.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.toolBar_vertical)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 2080, 24))
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
        self.menuMenu3 = QMenu(self.menubar)
        self.menuMenu3.setObjectName(u"menuMenu3")
        MainWindow.setMenuBar(self.menubar)

        self.toolBar.addAction(self.actionToolbar)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_widgets)
        self.toolBar.addAction(self.action_tabs)
        self.toolBar.addAction(self.action_examples)
        self.toolBar_vertical.addAction(self.actionToolbar)
        self.toolBar_vertical.addAction(self.action_widgets)
        self.toolBar_vertical.addAction(self.action_tabs)
        self.toolBar_vertical.addAction(self.action_examples)
        self.menubar.addAction(self.menuStyles.menuAction())
        self.menubar.addAction(self.menuDensity.menuAction())
        self.menubar.addAction(self.menumenu.menuAction())
        self.menubar.addAction(self.menumenu2.menuAction())
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
        self.menuMenu3.addAction(self.actionsubmenu)
        self.menuMenu3.addAction(self.actionsubmenu_2)
        self.menuMenu3.addSeparator()
        self.menuMenu3.addAction(self.actionsubmenu_4)
        self.menuMenu3.addAction(self.actionsubmenu_3)
        self.menuMenu3.addAction(self.actionSave_all)
        self.menuMenu3.addSeparator()
        self.menuMenu3.addAction(self.actionClose)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.toolBox.setCurrentIndex(0)
        self.tabWidget_7.setCurrentIndex(3)
        self.tabWidget_6.setCurrentIndex(6)
        self.tabWidget_8.setCurrentIndex(0)
        self.tabWidget_9.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)
        self.listWidget.setCurrentRow(3)
        self.listWidget_8.setCurrentRow(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Qt Material", None))
        self.actionSubmenu_2.setText(QCoreApplication.translate("MainWindow", u"Submenu 1.2", None))
        self.actionSubmenu_3.setText(QCoreApplication.translate("MainWindow", u"Submenu 1.3", None))
        self.actionSUBSUB.setText(QCoreApplication.translate("MainWindow", u"Submenu 1.1.1", None))
        self.actionSUBSUB_2.setText(QCoreApplication.translate("MainWindow", u"Submenu 1.1.2", None))
        self.actionSUBSUB_3.setText(QCoreApplication.translate("MainWindow", u"Submenu 1.1.3", None))
        self.actiondissabled.setText(QCoreApplication.translate("MainWindow", u"Disabled Submenu 1.4", None))
        self.actionSubmenu.setText(QCoreApplication.translate("MainWindow", u"Submenu 2.1", None))
        self.actionSubmenu_4.setText(QCoreApplication.translate("MainWindow", u"Submenu 2.2", None))
        self.actionSubmenu_5.setText(QCoreApplication.translate("MainWindow", u"Disabled Submenu 2.3", None))
        self.actionToolbar.setText(QCoreApplication.translate("MainWindow", u"Qt Material Theme", None))
#if QT_CONFIG(tooltip)
        self.actionToolbar.setToolTip(QCoreApplication.translate("MainWindow", u"Qt Material Theme", None))
#endif // QT_CONFIG(tooltip)
        self.action_widgets.setText(QCoreApplication.translate("MainWindow", u"QtWidgets", None))
        self.action_tabs.setText(QCoreApplication.translate("MainWindow", u"TabWidgets", None))
        self.actionsubmenu.setText(QCoreApplication.translate("MainWindow", u"New...", None))
        self.actionsubmenu_2.setText(QCoreApplication.translate("MainWindow", u"Open...", None))
        self.actionsubmenu_3.setText(QCoreApplication.translate("MainWindow", u"Save as...", None))
        self.actionsubmenu_4.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_all.setText(QCoreApplication.translate("MainWindow", u"Save all", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.action_examples.setText(QCoreApplication.translate("MainWindow", u"GUI Examples", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Checked", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Flat disabled", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Disable checked", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Flat checkeable", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Flat", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"Flat", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"Disable checked", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"Checked", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"Flat disabled", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"Flat checkeable", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_22), QCoreApplication.translate("MainWindow", u"Buttons", None))
        self.pushButton_57.setText(QCoreApplication.translate("MainWindow", u"Warning", None))
        self.pushButton_57.setProperty(u"class", QCoreApplication.translate("MainWindow", u"warning", None))
        self.pushButton_58.setText(QCoreApplication.translate("MainWindow", u"Danger", None))
        self.pushButton_58.setProperty(u"class", QCoreApplication.translate("MainWindow", u"danger", None))
        self.pushButton_59.setText(QCoreApplication.translate("MainWindow", u"Success", None))
        self.pushButton_59.setProperty(u"class", QCoreApplication.translate("MainWindow", u"success", None))
        self.pushButton_60.setText(QCoreApplication.translate("MainWindow", u"Success", None))
        self.pushButton_60.setProperty(u"class", QCoreApplication.translate("MainWindow", u"success", None))
        self.pushButton_61.setText(QCoreApplication.translate("MainWindow", u"Warning", None))
        self.pushButton_61.setProperty(u"class", QCoreApplication.translate("MainWindow", u"warning", None))
        self.pushButton_62.setText(QCoreApplication.translate("MainWindow", u"Danger", None))
        self.pushButton_62.setProperty(u"class", QCoreApplication.translate("MainWindow", u"danger", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Warning", None))
        self.pushButton_24.setProperty(u"class", QCoreApplication.translate("MainWindow", u"warning", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Danger", None))
        self.pushButton_25.setProperty(u"class", QCoreApplication.translate("MainWindow", u"danger", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"Success", None))
        self.pushButton_27.setProperty(u"class", QCoreApplication.translate("MainWindow", u"success", None))
        self.pushButton_55.setText(QCoreApplication.translate("MainWindow", u"Success", None))
        self.pushButton_55.setProperty(u"class", QCoreApplication.translate("MainWindow", u"success", None))
        self.pushButton_56.setText(QCoreApplication.translate("MainWindow", u"Warning", None))
        self.pushButton_56.setProperty(u"class", QCoreApplication.translate("MainWindow", u"warning", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"Danger", None))
        self.pushButton_26.setProperty(u"class", QCoreApplication.translate("MainWindow", u"danger", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>The widgets are assigned the classes <span style=\" font-weight:700;\">.danger</span>, <span style=\" font-weight:700;\">.success</span>, and <span style=\" font-weight:700;\">.warning</span> for styling purposes.</p></body></html>", None))
        self.label_75.setProperty(u"class", QCoreApplication.translate("MainWindow", u"danger", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_7), QCoreApplication.translate("MainWindow", u"Colored Buttons", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"Checked and Enabled RadioButton", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Unchecked and Enabled RadioButton", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"Checked and Disabled RadioButton", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"Unchecked and Disabled RadioButton", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"Checked and Enabled CheckBox", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Unchecked and Enabled CheckBox", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"Checked and Disabled CheckBox", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"Unchecked and Disabled CheckBox", None))
        self.checkBox_13.setText(QCoreApplication.translate("MainWindow", u"Partially Checked and Enabled CheckBox", None))
        self.checkBox_14.setText(QCoreApplication.translate("MainWindow", u"Partially Checked and Disabled CheckBox", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_23), QCoreApplication.translate("MainWindow", u"Radios and Checkboxes", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Normal Label", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Bold Label", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Italic Label", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Underline Label", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Strikeout Label", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Normal Label", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Bold Label", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Italic Label", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Strikeout Label", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Underline Label", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"Labels", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Placeholder Text", None))
        self.comboBox_11.setItemText(0, QCoreApplication.translate("MainWindow", u"Combo box", None))
        self.comboBox_11.setItemText(1, QCoreApplication.translate("MainWindow", u"Normal Item", None))
        self.comboBox_11.setItemText(2, QCoreApplication.translate("MainWindow", u"Normal Item", None))
        self.comboBox_11.setItemText(3, QCoreApplication.translate("MainWindow", u"Normal Item", None))
        self.comboBox_11.setItemText(4, QCoreApplication.translate("MainWindow", u"Normal Item", None))

        self.comboBox_11.setCurrentText(QCoreApplication.translate("MainWindow", u"Combo box", None))
        self.spinBox_6.setSuffix(QCoreApplication.translate("MainWindow", u" Sufix", None))
        self.spinBox_7.setPrefix(QCoreApplication.translate("MainWindow", u"Prefix ", None))
        self.spinBox_8.setSuffix(QCoreApplication.translate("MainWindow", u" Sufix", None))
        self.spinBox_8.setPrefix(QCoreApplication.translate("MainWindow", u"Prefix ", None))
        self.doubleSpinBox_6.setPrefix(QCoreApplication.translate("MainWindow", u"Prefix ", None))
        self.doubleSpinBox_7.setSuffix(QCoreApplication.translate("MainWindow", u" Sufix", None))
        self.doubleSpinBox_8.setPrefix(QCoreApplication.translate("MainWindow", u"Prefix ", None))
        self.doubleSpinBox_8.setSuffix(QCoreApplication.translate("MainWindow", u" Sufix", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"Line Edit", None))
        self.comboBox_13.setItemText(0, QCoreApplication.translate("MainWindow", u"Combo box - No Frame", None))
        self.comboBox_13.setItemText(1, QCoreApplication.translate("MainWindow", u"Normal Item", None))
        self.comboBox_13.setItemText(2, QCoreApplication.translate("MainWindow", u"Normal Item", None))
        self.comboBox_13.setItemText(3, QCoreApplication.translate("MainWindow", u"Normal Item", None))
        self.comboBox_13.setItemText(4, QCoreApplication.translate("MainWindow", u"Normal Item", None))

        self.comboBox_13.setCurrentText(QCoreApplication.translate("MainWindow", u"Combo box - No Frame", None))
        self.comboBox_12.setItemText(0, QCoreApplication.translate("MainWindow", u"Combo box", None))
        self.comboBox_12.setItemText(1, QCoreApplication.translate("MainWindow", u"Normal Item", None))
        self.comboBox_12.setItemText(2, QCoreApplication.translate("MainWindow", u"Normal Item", None))
        self.comboBox_12.setItemText(3, QCoreApplication.translate("MainWindow", u"Normal Item", None))
        self.comboBox_12.setItemText(4, QCoreApplication.translate("MainWindow", u"Normal Item", None))

        self.comboBox_12.setCurrentText(QCoreApplication.translate("MainWindow", u"Combo box", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Placeholder Text", None))
        self.spinBox_9.setSuffix(QCoreApplication.translate("MainWindow", u" Sufix", None))
        self.spinBox_10.setPrefix(QCoreApplication.translate("MainWindow", u"Prefix ", None))
        self.spinBox_11.setSuffix(QCoreApplication.translate("MainWindow", u" Sufix", None))
        self.spinBox_11.setPrefix(QCoreApplication.translate("MainWindow", u"Prefix ", None))
        self.doubleSpinBox_9.setPrefix(QCoreApplication.translate("MainWindow", u"Prefix ", None))
        self.doubleSpinBox_10.setSuffix(QCoreApplication.translate("MainWindow", u" Sufix", None))
        self.doubleSpinBox_11.setPrefix(QCoreApplication.translate("MainWindow", u"Prefix ", None))
        self.doubleSpinBox_11.setSuffix(QCoreApplication.translate("MainWindow", u" Sufix", None))
        self.lineEdit_8.setText(QCoreApplication.translate("MainWindow", u"Line Edit", None))
        self.comboBox_14.setItemText(0, QCoreApplication.translate("MainWindow", u"Combo box - No Frame", None))
        self.comboBox_14.setItemText(1, QCoreApplication.translate("MainWindow", u"Normal Item", None))
        self.comboBox_14.setItemText(2, QCoreApplication.translate("MainWindow", u"Normal Item", None))
        self.comboBox_14.setItemText(3, QCoreApplication.translate("MainWindow", u"Normal Item", None))
        self.comboBox_14.setItemText(4, QCoreApplication.translate("MainWindow", u"Normal Item", None))

        self.comboBox_14.setCurrentText(QCoreApplication.translate("MainWindow", u"Combo box - No Frame", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Inputs", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"Other Inputs", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_10), QCoreApplication.translate("MainWindow", u"Scroll Bars", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_11), QCoreApplication.translate("MainWindow", u"Sliders", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QCoreApplication.translate("MainWindow", u"Progress Bar", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Root Tree Item 1", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Child Item 1 (Enabled)", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Grandchild Item 1.1 (Enabled)", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem2.child(0)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"Great-grandchild Item 1.1.1 (Disabled)", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"Grandchild Item 1.2 (Disabled)", None));
        ___qtreewidgetitem5 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"Child Item 2 (Disabled)", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem5.child(0)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"Grandchild Item 2.1 (Enabled)", None));
        ___qtreewidgetitem7 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"Child Item 3 (Enabled)", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem7.child(0)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"Grandchild Item 3.1 (Disabled)", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem7.child(1)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"Grandchild Item 3.2 (Enabled)", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        ___qtreewidgetitem10 = self.treeWidget_2.headerItem()
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"Root Tree Item 1", None));

        __sortingEnabled1 = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        ___qtreewidgetitem11 = self.treeWidget_2.topLevelItem(0)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"Child Item 1 (Enabled)", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem11.child(0)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"Grandchild Item 1.1 (Enabled)", None));
        ___qtreewidgetitem13 = ___qtreewidgetitem12.child(0)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MainWindow", u"Great-grandchild Item 1.1.1 (Disabled)", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem11.child(1)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MainWindow", u"Grandchild Item 1.2 (Disabled)", None));
        ___qtreewidgetitem15 = self.treeWidget_2.topLevelItem(1)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MainWindow", u"Child Item 2 (Disabled)", None));
        ___qtreewidgetitem16 = ___qtreewidgetitem15.child(0)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MainWindow", u"Grandchild Item 2.1 (Enabled)", None));
        ___qtreewidgetitem17 = self.treeWidget_2.topLevelItem(2)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MainWindow", u"Child Item 3 (Enabled)", None));
        ___qtreewidgetitem18 = ___qtreewidgetitem17.child(0)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("MainWindow", u"Grandchild Item 3.1 (Disabled)", None));
        ___qtreewidgetitem19 = ___qtreewidgetitem17.child(1)
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("MainWindow", u"Grandchild Item 3.2 (Enabled)", None));
        self.treeWidget_2.setSortingEnabled(__sortingEnabled1)

        ___qtreewidgetitem20 = self.treeWidget_3.headerItem()
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("MainWindow", u"Root Tree Item 1", None));

        __sortingEnabled2 = self.treeWidget_3.isSortingEnabled()
        self.treeWidget_3.setSortingEnabled(False)
        ___qtreewidgetitem21 = self.treeWidget_3.topLevelItem(0)
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("MainWindow", u"Child Item 1 (Enabled)", None));
        ___qtreewidgetitem22 = ___qtreewidgetitem21.child(0)
        ___qtreewidgetitem22.setText(0, QCoreApplication.translate("MainWindow", u"Grandchild Item 1.1 (Enabled)", None));
        ___qtreewidgetitem23 = ___qtreewidgetitem22.child(0)
        ___qtreewidgetitem23.setText(0, QCoreApplication.translate("MainWindow", u"Great-grandchild Item 1.1.1 (Disabled)", None));
        ___qtreewidgetitem24 = ___qtreewidgetitem21.child(1)
        ___qtreewidgetitem24.setText(0, QCoreApplication.translate("MainWindow", u"Grandchild Item 1.2 (Disabled)", None));
        ___qtreewidgetitem25 = self.treeWidget_3.topLevelItem(1)
        ___qtreewidgetitem25.setText(0, QCoreApplication.translate("MainWindow", u"Child Item 2 (Disabled)", None));
        ___qtreewidgetitem26 = ___qtreewidgetitem25.child(0)
        ___qtreewidgetitem26.setText(0, QCoreApplication.translate("MainWindow", u"Grandchild Item 2.1 (Enabled)", None));
        ___qtreewidgetitem27 = self.treeWidget_3.topLevelItem(2)
        ___qtreewidgetitem27.setText(0, QCoreApplication.translate("MainWindow", u"Child Item 3 (Enabled)", None));
        ___qtreewidgetitem28 = ___qtreewidgetitem27.child(0)
        ___qtreewidgetitem28.setText(0, QCoreApplication.translate("MainWindow", u"Grandchild Item 3.1 (Disabled)", None));
        ___qtreewidgetitem29 = ___qtreewidgetitem27.child(1)
        ___qtreewidgetitem29.setText(0, QCoreApplication.translate("MainWindow", u"Grandchild Item 3.2 (Enabled)", None));
        self.treeWidget_3.setSortingEnabled(__sortingEnabled2)

        ___qtreewidgetitem30 = self.treeWidget_4.headerItem()
        ___qtreewidgetitem30.setText(0, QCoreApplication.translate("MainWindow", u"Root Tree Item 1", None));

        __sortingEnabled3 = self.treeWidget_4.isSortingEnabled()
        self.treeWidget_4.setSortingEnabled(False)
        ___qtreewidgetitem31 = self.treeWidget_4.topLevelItem(0)
        ___qtreewidgetitem31.setText(0, QCoreApplication.translate("MainWindow", u"Child Item 1 (Enabled)", None));
        ___qtreewidgetitem32 = ___qtreewidgetitem31.child(0)
        ___qtreewidgetitem32.setText(0, QCoreApplication.translate("MainWindow", u"Grandchild Item 1.1 (Enabled)", None));
        ___qtreewidgetitem33 = ___qtreewidgetitem32.child(0)
        ___qtreewidgetitem33.setText(0, QCoreApplication.translate("MainWindow", u"Great-grandchild Item 1.1.1 (Disabled)", None));
        ___qtreewidgetitem34 = ___qtreewidgetitem31.child(1)
        ___qtreewidgetitem34.setText(0, QCoreApplication.translate("MainWindow", u"Grandchild Item 1.2 (Disabled)", None));
        ___qtreewidgetitem35 = self.treeWidget_4.topLevelItem(1)
        ___qtreewidgetitem35.setText(0, QCoreApplication.translate("MainWindow", u"Child Item 2 (Disabled)", None));
        ___qtreewidgetitem36 = ___qtreewidgetitem35.child(0)
        ___qtreewidgetitem36.setText(0, QCoreApplication.translate("MainWindow", u"Grandchild Item 2.1 (Enabled)", None));
        ___qtreewidgetitem37 = self.treeWidget_4.topLevelItem(2)
        ___qtreewidgetitem37.setText(0, QCoreApplication.translate("MainWindow", u"Child Item 3 (Enabled)", None));
        ___qtreewidgetitem38 = ___qtreewidgetitem37.child(0)
        ___qtreewidgetitem38.setText(0, QCoreApplication.translate("MainWindow", u"Grandchild Item 3.1 (Disabled)", None));
        ___qtreewidgetitem39 = ___qtreewidgetitem37.child(1)
        ___qtreewidgetitem39.setText(0, QCoreApplication.translate("MainWindow", u"Grandchild Item 3.2 (Enabled)", None));
        self.treeWidget_4.setSortingEnabled(__sortingEnabled3)

        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_13), QCoreApplication.translate("MainWindow", u"Tree Widget", None))

        __sortingEnabled4 = self.listWidget_7.isSortingEnabled()
        self.listWidget_7.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_7.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Editable Item", None));
        ___qlistwidgetitem1 = self.listWidget_7.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Normal Item", None));
        ___qlistwidgetitem2 = self.listWidget_7.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Normal Item", None));
        ___qlistwidgetitem3 = self.listWidget_7.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Disabled Item", None));
        ___qlistwidgetitem4 = self.listWidget_7.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Disabled Item", None));
        ___qlistwidgetitem5 = self.listWidget_7.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Disabled Item", None));
        ___qlistwidgetitem6 = self.listWidget_7.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Normal Item", None));
        ___qlistwidgetitem7 = self.listWidget_7.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Disabled Item", None));
        self.listWidget_7.setSortingEnabled(__sortingEnabled4)


        __sortingEnabled5 = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        ___qlistwidgetitem8 = self.listWidget_3.item(0)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Icon Item", None));
        ___qlistwidgetitem9 = self.listWidget_3.item(1)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Icon Item", None));
        ___qlistwidgetitem10 = self.listWidget_3.item(2)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Icon Item", None));
        ___qlistwidgetitem11 = self.listWidget_3.item(3)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Icon Item", None));
        self.listWidget_3.setSortingEnabled(__sortingEnabled5)


        __sortingEnabled6 = self.listWidget_6.isSortingEnabled()
        self.listWidget_6.setSortingEnabled(False)
        ___qlistwidgetitem12 = self.listWidget_6.item(0)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Editable Item", None));
        ___qlistwidgetitem13 = self.listWidget_6.item(1)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Normal Item", None));
        ___qlistwidgetitem14 = self.listWidget_6.item(2)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Normal Item", None));
        ___qlistwidgetitem15 = self.listWidget_6.item(3)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Disabled Item", None));
        ___qlistwidgetitem16 = self.listWidget_6.item(4)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Disabled Item", None));
        ___qlistwidgetitem17 = self.listWidget_6.item(5)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Disabled Item", None));
        ___qlistwidgetitem18 = self.listWidget_6.item(6)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Normal Item", None));
        ___qlistwidgetitem19 = self.listWidget_6.item(7)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Disabled Item", None));
        self.listWidget_6.setSortingEnabled(__sortingEnabled6)

        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))

        __sortingEnabled7 = self.listWidget_5.isSortingEnabled()
        self.listWidget_5.setSortingEnabled(False)
        ___qlistwidgetitem20 = self.listWidget_5.item(0)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Editable Item", None));
        ___qlistwidgetitem21 = self.listWidget_5.item(1)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Normal Item", None));
        ___qlistwidgetitem22 = self.listWidget_5.item(2)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Normal Item", None));
        ___qlistwidgetitem23 = self.listWidget_5.item(3)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Disabled Item", None));
        ___qlistwidgetitem24 = self.listWidget_5.item(4)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Disabled Item", None));
        ___qlistwidgetitem25 = self.listWidget_5.item(5)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Disabled Item", None));
        ___qlistwidgetitem26 = self.listWidget_5.item(6)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Normal Item", None));
        ___qlistwidgetitem27 = self.listWidget_5.item(7)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Disabled Item", None));
        self.listWidget_5.setSortingEnabled(__sortingEnabled7)

        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))

        __sortingEnabled8 = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)
        ___qlistwidgetitem28 = self.listWidget_4.item(0)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Editable Item", None));
        ___qlistwidgetitem29 = self.listWidget_4.item(1)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Normal Item", None));
        ___qlistwidgetitem30 = self.listWidget_4.item(2)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Normal Item", None));
        ___qlistwidgetitem31 = self.listWidget_4.item(3)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Disabled Item", None));
        ___qlistwidgetitem32 = self.listWidget_4.item(4)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Disabled Item", None));
        ___qlistwidgetitem33 = self.listWidget_4.item(5)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Disabled Item", None));
        ___qlistwidgetitem34 = self.listWidget_4.item(6)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Normal Item", None));
        ___qlistwidgetitem35 = self.listWidget_4.item(7)
        ___qlistwidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Disabled Item", None));
        self.listWidget_4.setSortingEnabled(__sortingEnabled8)


        __sortingEnabled9 = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        ___qlistwidgetitem36 = self.listWidget_2.item(0)
        ___qlistwidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Icon Item", None));
        ___qlistwidgetitem37 = self.listWidget_2.item(1)
        ___qlistwidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Icon Item", None));
        ___qlistwidgetitem38 = self.listWidget_2.item(2)
        ___qlistwidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Icon Item", None));
        ___qlistwidgetitem39 = self.listWidget_2.item(3)
        ___qlistwidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Icon Item", None));
        self.listWidget_2.setSortingEnabled(__sortingEnabled9)

        self.toolBox.setItemText(self.toolBox.indexOf(self.page_16), QCoreApplication.translate("MainWindow", u"List Widget", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Duration", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Datetime", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem3 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Row-1", None));
        ___qtablewidgetitem4 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Row-3", None));

        __sortingEnabled10 = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"00:05:02", None));
        ___qtablewidgetitem6 = self.tableWidget_2.item(0, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"2020-04-27 17:31:34", None));
        ___qtablewidgetitem7 = self.tableWidget_2.item(0, 2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Unamed-1", None));
        ___qtablewidgetitem8 = self.tableWidget_2.item(1, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"00:01:02", None));
        ___qtablewidgetitem9 = self.tableWidget_2.item(1, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"2020-04-27 17:31:34", None));
        ___qtablewidgetitem10 = self.tableWidget_2.item(1, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Unamed-2", None));
        ___qtablewidgetitem11 = self.tableWidget_2.item(2, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"00:07:02", None));
        ___qtablewidgetitem12 = self.tableWidget_2.item(2, 1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"2020-04-27 17:31:34", None));
        ___qtablewidgetitem13 = self.tableWidget_2.item(2, 2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Unamed-3", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled10)

        ___qtablewidgetitem14 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Duration", None));
        ___qtablewidgetitem15 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Datetime", None));
        ___qtablewidgetitem16 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem17 = self.tableWidget_3.verticalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Row-1", None));
        ___qtablewidgetitem18 = self.tableWidget_3.verticalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Row-3", None));

        __sortingEnabled11 = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        ___qtablewidgetitem19 = self.tableWidget_3.item(0, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"00:05:02", None));
        ___qtablewidgetitem20 = self.tableWidget_3.item(0, 1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"2020-04-27 17:31:34", None));
        ___qtablewidgetitem21 = self.tableWidget_3.item(0, 2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Unamed-1", None));
        ___qtablewidgetitem22 = self.tableWidget_3.item(1, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"00:01:02", None));
        ___qtablewidgetitem23 = self.tableWidget_3.item(1, 1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"2020-04-27 17:31:34", None));
        ___qtablewidgetitem24 = self.tableWidget_3.item(1, 2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Unamed-2", None));
        ___qtablewidgetitem25 = self.tableWidget_3.item(2, 0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"00:07:02", None));
        ___qtablewidgetitem26 = self.tableWidget_3.item(2, 1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"2020-04-27 17:31:34", None));
        ___qtablewidgetitem27 = self.tableWidget_3.item(2, 2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Unamed-3", None));
        self.tableWidget_3.setSortingEnabled(__sortingEnabled11)

        ___qtablewidgetitem28 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Duration", None));
        ___qtablewidgetitem29 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Datetime", None));
        ___qtablewidgetitem30 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem31 = self.tableWidget_5.verticalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Row-1", None));
        ___qtablewidgetitem32 = self.tableWidget_5.verticalHeaderItem(2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Row-3", None));

        __sortingEnabled12 = self.tableWidget_5.isSortingEnabled()
        self.tableWidget_5.setSortingEnabled(False)
        ___qtablewidgetitem33 = self.tableWidget_5.item(0, 0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"00:05:02", None));
        ___qtablewidgetitem34 = self.tableWidget_5.item(0, 1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"2020-04-27 17:31:34", None));
        ___qtablewidgetitem35 = self.tableWidget_5.item(0, 2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Unamed-1", None));
        ___qtablewidgetitem36 = self.tableWidget_5.item(1, 0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"00:01:02", None));
        ___qtablewidgetitem37 = self.tableWidget_5.item(1, 1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"2020-04-27 17:31:34", None));
        ___qtablewidgetitem38 = self.tableWidget_5.item(1, 2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Unamed-2", None));
        ___qtablewidgetitem39 = self.tableWidget_5.item(2, 0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"00:07:02", None));
        ___qtablewidgetitem40 = self.tableWidget_5.item(2, 1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"2020-04-27 17:31:34", None));
        ___qtablewidgetitem41 = self.tableWidget_5.item(2, 2)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Unamed-3", None));
        self.tableWidget_5.setSortingEnabled(__sortingEnabled12)

        ___qtablewidgetitem42 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Duration", None));
        ___qtablewidgetitem43 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Datetime", None));
        ___qtablewidgetitem44 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem45 = self.tableWidget_4.verticalHeaderItem(0)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Row-1", None));
        ___qtablewidgetitem46 = self.tableWidget_4.verticalHeaderItem(2)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Row-3", None));

        __sortingEnabled13 = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        ___qtablewidgetitem47 = self.tableWidget_4.item(0, 0)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"00:05:02", None));
        ___qtablewidgetitem48 = self.tableWidget_4.item(0, 1)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"2020-04-27 17:31:34", None));
        ___qtablewidgetitem49 = self.tableWidget_4.item(0, 2)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Unamed-1", None));
        ___qtablewidgetitem50 = self.tableWidget_4.item(1, 0)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"00:01:02", None));
        ___qtablewidgetitem51 = self.tableWidget_4.item(1, 1)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"2020-04-27 17:31:34", None));
        ___qtablewidgetitem52 = self.tableWidget_4.item(1, 2)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Unamed-2", None));
        ___qtablewidgetitem53 = self.tableWidget_4.item(2, 0)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"00:07:02", None));
        ___qtablewidgetitem54 = self.tableWidget_4.item(2, 1)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"2020-04-27 17:31:34", None));
        ___qtablewidgetitem55 = self.tableWidget_4.item(2, 2)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Unamed-3", None));
        self.tableWidget_4.setSortingEnabled(__sortingEnabled13)

        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_14), QCoreApplication.translate("MainWindow", u"Table Widget", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"QPlainTextEdit", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("MainWindow", u"plainTextEdit\n"
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"QTextEdit", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"plainTextEdit\n"
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", None))
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
        self.textEdit_2.setMarkdown(QCoreApplication.translate("MainWindow", u"textEdit Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do\n"
"eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim\n"
"veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo\n"
"consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse\n"
"cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non\n"
"proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n"
"\n"
"", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans';\">textEdit Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepte"
                        "ur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</span></p></body></html>", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_26), QCoreApplication.translate("MainWindow", u"TextEdits", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_17), QCoreApplication.translate("MainWindow", u"Lines/Separators", None))
        self.pushButton_file_dialog.setText(QCoreApplication.translate("MainWindow", u"QFileDialog", None))
        self.pushButton_folder_dialog.setText(QCoreApplication.translate("MainWindow", u"QFolderDialog", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_24), QCoreApplication.translate("MainWindow", u"Dialogs", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox Flat Checkeable", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox Flat Checkeable", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox Flat", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>This widget has the <span style=\" font-weight:700;\">frameless</span> property set to <span style=\" font-weight:700;\">true</span>.</p></body></html>", None))
        self.label_52.setProperty(u"class", QCoreApplication.translate("MainWindow", u"danger", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox Checkeable", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox Checkeable", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox Normal", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox Checkeable", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox Checkeable", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox Normal", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox Flat Checkeable", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox Flat Checkeable", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox Flat", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>This widget has the <span style=\" font-weight:700;\">frameless</span> property set to <span style=\" font-weight:700;\">true</span>.</p></body></html>", None))
        self.label_32.setProperty(u"class", QCoreApplication.translate("MainWindow", u"danger", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_25), QCoreApplication.translate("MainWindow", u"Group Boxes", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"QFrame - No Frame", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>This widget has the <span style=\" font-weight:700;\">frameless</span> property set to <span style=\" font-weight:700;\">true</span>.</p></body></html>", None))
        self.label_26.setProperty(u"class", QCoreApplication.translate("MainWindow", u"danger", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"QFrame", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>This widget has the <span style=\" font-weight:700;\">colored</span> property set to <span style=\" font-weight:700;\">true</span>.</p></body></html>", None))
        self.label_27.setProperty(u"class", QCoreApplication.translate("MainWindow", u"danger", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"QFrame - Border colored", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"QFrame - No Frame - Disabled", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>This widget has the <span style=\" font-weight:700;\">colored</span> property set to <span style=\" font-weight:700;\">true</span>.</p></body></html>", None))
        self.label_28.setProperty(u"class", QCoreApplication.translate("MainWindow", u"danger", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"QFrame - Disabled", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"QFrame - Border colored - Disabled", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>This widget has the <span style=\" font-weight:700;\">colored</span> property set to <span style=\" font-weight:700;\">true</span>.</p></body></html>", None))
        self.label_30.setProperty(u"class", QCoreApplication.translate("MainWindow", u"danger", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_27), QCoreApplication.translate("MainWindow", u"QFrame", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_38), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_39), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_40), QCoreApplication.translate("MainWindow", u"Tab with an unusually long name", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_31), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_32), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_33), QCoreApplication.translate("MainWindow", u"Tab with an unusually long name", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_34), QCoreApplication.translate("MainWindow", u"Tab 4", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_35), QCoreApplication.translate("MainWindow", u"Tab 5", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_36), QCoreApplication.translate("MainWindow", u"Tab 6", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_52), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_53), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_54), QCoreApplication.translate("MainWindow", u"Tab with an unusually long name*", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_55), QCoreApplication.translate("MainWindow", u"Tab 4", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_56), QCoreApplication.translate("MainWindow", u"Tab 5", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_57), QCoreApplication.translate("MainWindow", u"Tab 6", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_58), QCoreApplication.translate("MainWindow", u"Tab 7", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_45), QCoreApplication.translate("MainWindow", u"Tab 1*", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_46), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_47), QCoreApplication.translate("MainWindow", u"Tab with an unusually long name", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_48), QCoreApplication.translate("MainWindow", u"Tab 4", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_49), QCoreApplication.translate("MainWindow", u"Tab 5", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_50), QCoreApplication.translate("MainWindow", u"Tab 6", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_51), QCoreApplication.translate("MainWindow", u"Tab 7", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_37), QCoreApplication.translate("MainWindow", u"Tab 7*", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_41), QCoreApplication.translate("MainWindow", u"Tab 4*", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_42), QCoreApplication.translate("MainWindow", u"Tab 5", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_43), QCoreApplication.translate("MainWindow", u"Tab 6", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_44), QCoreApplication.translate("MainWindow", u"Tab 7", None))
        self.subwindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Education Level", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Michelle", None))
        self.spinBox.setSuffix(QCoreApplication.translate("MainWindow", u" yo", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Female", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"Female", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Undergraduate", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Bachelor\u2019s", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Postgraduate", None))
        self.subwindow_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"Features", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Enable feature", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Select folder", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Save settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"General", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Logs", None))
        self.subwindow_3.setWindowTitle(QCoreApplication.translate("MainWindow", u"Aplication Preferences", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"General", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Appearance", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Advanced", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Startup Behavior", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Restore last session", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Check for updates at startup", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Show splash screen", None))
        self.radioButton_9.setText(QCoreApplication.translate("MainWindow", u"Open default dashboard", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Default file location:", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Auto-save interval (minutes):", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Language:", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"English", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Espa\u00f1ol", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Fran\u00e7ais", None))

        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Syncing settings...", None))
        self.subwindow_4.setWindowTitle(QCoreApplication.translate("MainWindow", u"Preferences", None))

        __sortingEnabled14 = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem40 = self.listWidget.item(0)
        ___qlistwidgetitem40.setText(QCoreApplication.translate("MainWindow", u"General", None));
        ___qlistwidgetitem41 = self.listWidget.item(1)
        ___qlistwidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Editor", None));
        ___qlistwidgetitem42 = self.listWidget.item(2)
        ___qlistwidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Appearance", None));
        ___qlistwidgetitem43 = self.listWidget.item(3)
        ___qlistwidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Connections", None));
        ___qlistwidgetitem44 = self.listWidget.item(4)
        ___qlistwidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Updates", None));
        self.listWidget.setSortingEnabled(__sortingEnabled14)

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Server ID", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"df8e9128", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Network mode", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Online", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Offline", None))

        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Timeout interval", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"6 sec", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Authentication", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Enable authentication", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"Use SSH keys", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Alert", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Enable sound", None))
        self.subwindow_5.setWindowTitle(QCoreApplication.translate("MainWindow", u"Import and Analyze Data", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"File path:", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"/user/documents/data.csv", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Separator:", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"(", None))

        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Encoding:", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"UTF-8", None))

        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Columns to include:", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u"Value", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Analysis type:", None))
        self.radioButton_11.setText(QCoreApplication.translate("MainWindow", u"Statistical", None))
        self.radioButton_12.setText(QCoreApplication.translate("MainWindow", u"Time series", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Run Analysis", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.subwindow_6.setWindowTitle(QCoreApplication.translate("MainWindow", u"Manage Tasks", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Tasklist:", None))

        __sortingEnabled15 = self.listWidget_8.isSortingEnabled()
        self.listWidget_8.setSortingEnabled(False)
        ___qlistwidgetitem45 = self.listWidget_8.item(0)
        ___qlistwidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Call client", None));
        ___qlistwidgetitem46 = self.listWidget_8.item(1)
        ___qlistwidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Buy groceries", None));
        ___qlistwidgetitem47 = self.listWidget_8.item(2)
        ___qlistwidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Schedule meeting", None));
        ___qlistwidgetitem48 = self.listWidget_8.item(3)
        ___qlistwidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Clean office", None));
        self.listWidget_8.setSortingEnabled(__sortingEnabled15)

        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Up", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Details:", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.subwindow_7.setWindowTitle(QCoreApplication.translate("MainWindow", u"Activity Monitor", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Disk:", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"RAM", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"CPU:", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"GPU", None))
        self.subwindow_8.setWindowTitle(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Select a date:", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Duration:", None))
        self.spinBox_3.setSuffix(QCoreApplication.translate("MainWindow", u" minutes", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Meeting Type:", None))
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"In-person", None))
        self.radioButton_13.setText(QCoreApplication.translate("MainWindow", u"Online", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Notify participants:", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"yes", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.subwindow_9.setWindowTitle(QCoreApplication.translate("MainWindow", u"Fail", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"Success", None))
        self.pushButton_39.setProperty(u"class", QCoreApplication.translate("MainWindow", u"success", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_vertical.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
        self.menumenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu 1", None))
        self.menuSubmenu.setTitle(QCoreApplication.translate("MainWindow", u"Submenu 1.1", None))
        self.menumenu2.setTitle(QCoreApplication.translate("MainWindow", u"Menu 2", None))
        self.menumenu_disabled.setTitle(QCoreApplication.translate("MainWindow", u"Disabled Menu 3", None))
        self.menuStyles.setTitle(QCoreApplication.translate("MainWindow", u"Styles", None))
        self.menuDensity.setTitle(QCoreApplication.translate("MainWindow", u"Density", None))
        self.menuMenu3.setTitle(QCoreApplication.translate("MainWindow", u"Menu 4", None))
    # retranslateUi

