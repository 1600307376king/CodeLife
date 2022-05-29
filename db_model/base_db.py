#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/22 17:26
# @Author  : jjc
# @File    : base_db.py
# @Software: PyCharm
import os
import sqlite3


class BaseDbManager:
    def __init__(self):
        self.db_name = "study.db"
        self.db_path = os.path.join(os.getcwd(), "src/db_file/%s" % self.db_name)
        self.conn = sqlite3.connect(self.db_path)

    def close_conn(self):
        self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_conn()
