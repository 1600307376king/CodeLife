#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/22 18:35
# @Author  : jjc
# @File    : themeNote.py
# @Software: PyCharm
from baseDb import BaseDbManager


class ThemeNote(BaseDbManager):

    def create_theme_table(self):
        try:
            cur = self.conn.cursor()
            cur.execute('''
                CREATE TABLE IF NOT EXISTS 'THEME'(
                ID INTEGER PRIMARY KEY,
                THEME_NAME CHAR(20) NOT NULL,
                )
            ''')
            self.conn.commit()
        except Exception as e:
            print("create theme table: %s" % e)

    def insert_theme(self, name):
        cur = self.conn.cursor()
        cur.execute("INSERT INFO THEME (ID, THEME_NAME) VALUES (NULL, '%s')" % name)
        self.conn.commit()
