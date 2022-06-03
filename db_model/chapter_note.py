#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/22 18:43
# @Author  : jjc
# @File    : chapter_note.py
# @Software: PyCharm
import os
from db_model.base_db import BaseDbManager


class ChapterNote(BaseDbManager):

    def create_chapter_note(self):
        cur = self.conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS CHAPTER
            (ID INTEGER PRIMARY KEY,
            THEME_NAME CHAR(20) NOT NULL,
            CHAPTER_NAME CHAR(20) NOT NULL,
            CONTENT TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def select_note(self, theme_name):
        sql = "select CHAPTER_NAME, CONTENT from CHAPTER where THEME_NAME = %s" % theme_name
        cur = self.conn.cursor()
        return cur.execute(sql).fetchall()

    def insert_note(self, theme_name, chapter, content):
        sql = "INSERT INTO CHAPTER (ID, THEME_NAME, CHAPTER_NAME, CONTENT)" \
              " VALUES (NULL, '%s', '%s', '%s')" % (theme_name, chapter, content)
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def del_note(self, theme_name):
        sql = "delete from CHAPTER where THEME_NAME='%s'" % theme_name
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def del_chapter(self, chapter_name):
        sql = "delete from CHAPTER where CHAPTER_NAME='%s'" % chapter_name
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()


if __name__ == '__main__':
    cn = ChapterNote()
    cn.create_chapter_note()
