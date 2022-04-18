#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/18 22:06
# @Author  : jjc
# @File    : config.py
# @Software: PyCharm
from win32api import GetSystemMetrics

window_width = 1600
window_height = 960
window_title = "Program Manager"
screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)
window_init_position = ((screen_width - window_width) // 2, (screen_height - window_height) // 2)

