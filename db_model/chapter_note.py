#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/22 18:43
# @Author  : jjc
# @File    : chapter_note.py
# @Software: PyCharm
import os
from base_db import BaseDbManager


class ChapterNote(BaseDbManager):

    def create_chapter_note(self):
        cur = self.conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS CHAPTER
            (ID INTEGER PRIMARY KEY,
            THEME_NAME CHAR(20) NOT NULL,
            CHAPTER CHAR(20) NOT NULL,
            CONTENT TEXT NOT NULL
            )
        ''')
        self.conn.commit()


if __name__ == '__main__':
    cn = ChapterNote()
    cn.create_chapter_note()
