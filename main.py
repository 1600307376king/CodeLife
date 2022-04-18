#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 13:28
# @Author  : jjc
# @File    : main.py
# @Software: PyCharm
import sys
from PyQt6 import QtWidgets


def main():
    app = QtWidgets.QApplication(sys.argv)

    w = QtWidgets.QWidget()
    w.resize(250, 200)
    w.move(300, 300)
    w.setWindowTitle('ProgramManager')
    w.show()
    sys.exit(app.exit())


if __name__ == '__main__':
    main()
