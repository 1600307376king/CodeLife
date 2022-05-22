#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/22 17:26
# @Author  : jjc
# @File    : baseDb.py
# @Software: PyCharm
import sqlite3


class BaseDbManager:
    def __init__(self):
        self.conn = sqlite3.connect("./src/db_file/study.db")

    def close_conn(self):
        self.conn.close()
