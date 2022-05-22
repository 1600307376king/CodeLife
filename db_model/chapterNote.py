#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/22 18:43
# @Author  : jjc
# @File    : chapterNote.py
# @Software: PyCharm
from baseDb import BaseDbManager


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
