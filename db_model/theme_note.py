#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/22 18:35
# @Author  : jjc
# @File    : theme_note.py
# @Software: PyCharm
from db_model.base_db import BaseDbManager


class ThemeNote(BaseDbManager):

    def create_theme_table(self):
        try:
            cur = self.conn.cursor()
            cur.execute('''
                CREATE TABLE IF NOT EXISTS THEME
                (ID INTEGER PRIMARY KEY,
                THEME_NAME CHAR(20) NOT NULL
                )
            ''')
            self.conn.commit()
        except Exception as e:
            print("create theme table: %s" % e)

    def insert_theme(self, name):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO THEME (ID, THEME_NAME) VALUES (NULL, '%s')" % name)
        self.conn.commit()

    def select_all_theme(self):
        sql = "select THEME_NAME FROM THEME"
        cur = self.conn.cursor()
        query_result = cur.execute(sql)
        return query_result.fetchall()

    def del_theme(self, theme_name):
        sql = "delete FROM THEME where THEME_NAME='%s'" % theme_name
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()


if __name__ == '__main__':
    # tn = ThemeNote()
    # tn.create_theme_table()
    with ThemeNote() as tn:
        print(tn.select_all_theme())
