#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/18 14:36
# @Author  : jjc
# @File    : md_to_html.py
# @Software: PyCharm
head_str = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- <link href="src/edit.css" rel="stylesheet" /> -->
</head>
<style>
    /* 标题一样式 */
    .title1 {
        font-size: 36px;
        font-weight: 700;
    }

    /* 标题二样式 */
    .title2 {
        font-size: 30px;
        font-weight: 700;
    }

    /* 代码块 */
    .codeBlock {
        background-color: #F8F8F8;
        margin: 10px;
        padding: 10px;
        white-space:nowrap;
        
    }

    /* 代码缩进样式 */
    .codeLine {
        white-space: pre-wrap;
        /* background-color:greenyellow; */
        font-family: "Lucida Console", "Courier New", monospace;
        margin: 3px;
    }

    /* 表格样式 */
    table {
        border-collapse: collapse;
        border-spacing: 0;
    }
    
    td,th {
        padding: 0;
    }
    
    .pure-table {
        border-collapse: collapse;
        border-spacing: 0;
        empty-cells: show;
        border: 1px solid #cbcbcb;
    }
    
    .pure-table caption {
        color: #000;
        font: italic 85%/1 arial,sans-serif;
        padding: 1em 0;
        text-align: center;
    }
    
    .pure-table td,.pure-table th {
        border-left: 1px solid #cbcbcb;
        border-width: 0 0 0 1px;
        font-size: inherit;
        margin: 0;
        overflow: visible;
        padding: .5em 1em;
    }
    
    .pure-table thead {
        background-color: #e0e0e0;
        color: #000;
        text-align: left;
        vertical-align: bottom;
    }
    
    .pure-table td {
        background-color: transparent;
    }
    
    hr {
        border: 1px solid #EEEEEE;
    }

</style>
<body>"""

tail_str = """</body>
</html>"""


class MdToHtml:
    def __init__(self):
        self.template_html_head = head_str
        self.template_html_tail = tail_str

    def refresh_line(self, input_text):
        div_block = ""
        disordered_list = ['''<ul class="disorderedList">''', '''</ul>''']
        text_list = input_text.split("\n")
        for index, line in enumerate(text_list):
            if line.lstrip().startswith("# "):
                line_text = line.lstrip("# ")
                # 标题一
                div_block += '''<div class="title1">%s</div>\n<hr>''' % line_text
            elif line.lstrip().startswith("## "):
                # 标题二
                line_text = line.lstrip("# ")
                div_block += '''<div class="title2">%s</div>\n<hr>''' % line_text
            elif line == "":
                # 换行
                div_block += '''<br>'''
            elif line.lstrip().startswith("- "):
                # 无序列表
                if index > 0 and not text_list[index-1].lstrip().startswith("- "):
                    div_block += '''<ul class="disorderedList">'''
                else:
                    div_block += '''<ul class="disorderedList">'''
                line_text = line.lstrip("- ")
                div_block += '''<li>%s</li>''' % line_text
                if index+1 < len(text_list) and not text_list[index+1].lstrip().startswith("- "):
                    div_block += '''</ul>'''
                else:
                    div_block += '''</ul>'''
            else:
                div_block += '''<div>%s</div>\n''' % line
        new_html = self.template_html_head + div_block + self.template_html_tail
        return new_html
