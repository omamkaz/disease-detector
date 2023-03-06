# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QToolButton, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(464, 40)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.title = QLabel(Form)
        self.title.setObjectName(u"title")
        self.title.setMouseTracking(True)
        self.title.setTabletTracking(True)

        self.gridLayout.addWidget(self.title, 0, 1, 1, 1)

        self.remove_btn = QToolButton(Form)
        self.remove_btn.setObjectName(u"remove_btn")
        self.remove_btn.setMouseTracking(True)
        self.remove_btn.setTabletTracking(True)
        self.remove_btn.setAutoRaise(True)

        self.gridLayout.addWidget(self.remove_btn, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText("")
        self.remove_btn.setText("")
    # retranslateUi

