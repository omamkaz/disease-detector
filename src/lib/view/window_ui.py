# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QSizePolicy, QStackedWidget, QToolButton,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(729, 451)
        MainWindow.setDocumentMode(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.app_bar = QWidget(self.centralwidget)
        self.app_bar.setObjectName(u"app_bar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_bar.sizePolicy().hasHeightForWidth())
        self.app_bar.setSizePolicy(sizePolicy)
        self.app_bar.setMouseTracking(True)
        self.app_bar.setTabletTracking(True)
        self.horizontalLayout = QHBoxLayout(self.app_bar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.app_icon = QLabel(self.app_bar)
        self.app_icon.setObjectName(u"app_icon")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.app_icon.sizePolicy().hasHeightForWidth())
        self.app_icon.setSizePolicy(sizePolicy1)
        self.app_icon.setMaximumSize(QSize(40, 40))
        self.app_icon.setMouseTracking(True)
        self.app_icon.setTabletTracking(True)
        self.app_icon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.app_icon)

        self.app_title = QLabel(self.app_bar)
        self.app_title.setObjectName(u"app_title")
        self.app_title.setMouseTracking(True)
        self.app_title.setTabletTracking(True)
        self.app_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.app_title)

        self.go_btn = QToolButton(self.app_bar)
        self.go_btn.setObjectName(u"go_btn")
        self.go_btn.setMouseTracking(True)
        self.go_btn.setTabletTracking(True)
        self.go_btn.setAutoRaise(True)

        self.horizontalLayout.addWidget(self.go_btn)

        self.theme_btn = QToolButton(self.app_bar)
        self.theme_btn.setObjectName(u"theme_btn")
        self.theme_btn.setAutoRaise(True)

        self.horizontalLayout.addWidget(self.theme_btn)

        self.min_btn = QToolButton(self.app_bar)
        self.min_btn.setObjectName(u"min_btn")
        self.min_btn.setAutoRaise(True)

        self.horizontalLayout.addWidget(self.min_btn)

        self.max_btn = QToolButton(self.app_bar)
        self.max_btn.setObjectName(u"max_btn")
        self.max_btn.setAutoRaise(True)

        self.horizontalLayout.addWidget(self.max_btn)

        self.close_btn = QToolButton(self.app_bar)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setAutoRaise(True)

        self.horizontalLayout.addWidget(self.close_btn)


        self.gridLayout_5.addWidget(self.app_bar, 0, 0, 1, 2)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_7 = QGridLayout(self.page)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.list_symptoms = QListWidget(self.page)
        self.list_symptoms.setObjectName(u"list_symptoms")
        self.list_symptoms.setMouseTracking(True)
        self.list_symptoms.setTabletTracking(True)
        self.list_symptoms.setFrameShape(QFrame.NoFrame)
        self.list_symptoms.setFrameShadow(QFrame.Plain)
        self.list_symptoms.setAlternatingRowColors(True)

        self.gridLayout_7.addWidget(self.list_symptoms, 0, 2, 1, 1)

        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.list_symptoms_all = QListWidget(self.widget)
        self.list_symptoms_all.setObjectName(u"list_symptoms_all")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.list_symptoms_all.sizePolicy().hasHeightForWidth())
        self.list_symptoms_all.setSizePolicy(sizePolicy2)
        self.list_symptoms_all.setFrameShape(QFrame.NoFrame)
        self.list_symptoms_all.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.list_symptoms_all, 1, 0, 1, 1)

        self.line_search = QLineEdit(self.widget)
        self.line_search.setObjectName(u"line_search")
        sizePolicy.setHeightForWidth(self.line_search.sizePolicy().hasHeightForWidth())
        self.line_search.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.line_search, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.widget, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_2 = QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.result_title = QLabel(self.page_2)
        self.result_title.setObjectName(u"result_title")
        self.result_title.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.result_title, 0, 0, 1, 1)

        self.list_result = QListWidget(self.page_2)
        self.list_result.setObjectName(u"list_result")
        self.list_result.setMouseTracking(True)
        self.list_result.setTabletTracking(True)
        self.list_result.setFrameShape(QFrame.NoFrame)
        self.list_result.setFrameShadow(QFrame.Plain)

        self.gridLayout_2.addWidget(self.list_result, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_5.addWidget(self.stackedWidget, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.app_icon.setText("")
        self.app_title.setText("")
        self.go_btn.setText("")
        self.theme_btn.setText("")
        self.min_btn.setText("")
        self.max_btn.setText("")
        self.close_btn.setText("")
        self.line_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0627\u0644\u0628\u062d\u062b", None))
        self.result_title.setText("")
    # retranslateUi

