#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/12 16:23
# @Author  : jjc
# @File    : md2html.py
# @Software: PyCharm
import os
import codecs
import markdown
import os.path as op
from bs4 import BeautifulSoup


def md_to_html_with_spec_path(md_name, theme_name):
    os.makedirs("src/typora_src/src_md/%s" % theme_name, exist_ok=True)
    os.makedirs("src/typora_src/src_html/%s" % theme_name, exist_ok=True)
    with codecs.open(os.path.join(os.getcwd(), "src/typora_src/src_md/%s/%s.md" % (theme_name, md_name)), mode="r",
                     encoding="utf-8") as md:
        html = markdown.markdown(md.read())
        with open(os.path.join(os.getcwd(), "src/typora_src/src_html/%s/%s.html" % (theme_name, md_name)), mode="w",
                  encoding="utf-8") as ht:
            ht.write(html)

#
# if __name__ == '__main__':
#     md_to_html_with_spec_path("111", "Flask")
