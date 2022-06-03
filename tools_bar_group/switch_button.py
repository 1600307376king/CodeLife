#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/3 12:09
# @Author  : jjc
# @File    : switch_button.py
# @Software: PyCharm
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QFont, QBrush, QColor, QPen


class SwitchButton(QWidget):
    def __init__(self, parent=None):
        super(SwitchButton, self).__init__(parent)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(55, 20)
        self.state = False
        self.move(2, 3)

    def mousePressEvent(self, event):
        super(SwitchButton, self).mousePressEvent(event)
        self.state = False if self.state else True
        self.update()

    def paintEvent(self, event):
        super(SwitchButton, self).paintEvent(event)

        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

        font = QFont("Microsoft YaHei")
        font.setPixelSize(12)
        painter.setFont(font)

        if self.state:
            # 绘制背景
            painter.setPen(Qt.NoPen)
            brush = QBrush(QColor("#FF475D"))
            painter.setBrush(brush)
            painter.drawRoundedRect(0, 0, self.width(), self.height(), self.height() // 2, self.height() // 2)

            # 绘制圆圈
            painter.setPen(Qt.NoPen)
            brush.setColor(QColor("#ffffff"))
            painter.setBrush(brush)
            painter.drawRoundedRect(38, 2, 16, 16, 16, 16)

            # 绘制文本
            painter.setPen(QPen(QColor("#ffffff")))
            painter.setBrush(Qt.NoBrush)
            painter.drawText(QRect(8, 2, 22, 20), Qt.AlignLeft, "开")

        else:
            # 绘制背景
            painter.setPen(Qt.NoPen)
            brush = QBrush(QColor("#FFFFFF"))
            painter.setBrush(brush)
            painter.drawRoundedRect(0, 0, self.width(), self.height(), self.height() // 2, self.height() // 2)

            # 绘制圆圈
            pen = QPen(QColor("#999999"))
            pen.setWidth(1)
            painter.setPen(pen)
            painter.drawRoundedRect(2, 2, 16, 16, 8, 8)

            # 绘制文本
            painter.setBrush(Qt.NoBrush)
            painter.drawText(QRect(36, 2, 45, 20), Qt.AlignLeft, "关")
