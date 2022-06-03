# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_note_dialog.py'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from signal_manager import SignalManager


class AddNoteDialog(QMainWindow):

    def __init__(self):
        super(AddNoteDialog, self).__init__()
        self.setObjectName("add_note_dialog")
        self.resize(801, 455)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.setFont(font)
        self.send = SignalManager()
        self.title_set = set()

    def show_dialog(self, theme_name):
        if theme_name:
            self.show()
        else:
            msg_box = QMessageBox(QMessageBox.Warning, "警告", "主题不存在，请先创建")
            msg_box.exec_()

    def _init_title_name_label(self):
        self.title_name_label = QtWidgets.QLabel(self)
        self.title_name_label.setGeometry(QtCore.QRect(13, 31, 81, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.title_name_label.setFont(font)
        self.title_name_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.title_name_label.setObjectName("title_name_label")

    def _init_title_edit(self):
        self.title_line_edit = QtWidgets.QLineEdit(self)
        self.title_line_edit.setGeometry(QtCore.QRect(110, 30, 141, 31))
        self.title_line_edit.setObjectName("title_line_edit")

    def _init_preview_note(self):
        self.preview_note = QtWidgets.QTextBrowser(self)
        self.preview_note.setGeometry(QtCore.QRect(485, 90, 281, 261))
        self.preview_note.setObjectName("preview_note")

    def _init_note_text_edit(self):
        self.note_text_edit = QtWidgets.QTextEdit(self)
        self.note_text_edit.setGeometry(QtCore.QRect(110, 90, 271, 261))
        self.note_text_edit.setObjectName("note_text_edit")
        self.note_text_edit.textChanged.connect(self.fresh_text_edit)

    def _init_note_content_label(self):
        self.note_content_label = QtWidgets.QLabel(self)
        self.note_content_label.setGeometry(QtCore.QRect(13, 91, 81, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.note_content_label.setFont(font)
        self.note_content_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.note_content_label.setObjectName("note_content_label")

    def _init_preview_note_label(self):
        self.preview_note_label = QtWidgets.QLabel(self)
        self.preview_note_label.setGeometry(QtCore.QRect(410, 90, 71, 31))
        self.preview_note_label.setObjectName("preview_note_label")

    def _save_btn(self):
        self.save_note_btn = QtWidgets.QPushButton(self)
        self.save_note_btn.setGeometry(QtCore.QRect(210, 380, 141, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.save_note_btn.setFont(font)
        self.save_note_btn.setObjectName("save_note_btn")
        self.save_note_btn.clicked.connect(self.save_title_content)

    def _cancel_btn(self):
        self.cancel_note_btn = QtWidgets.QPushButton(self)
        self.cancel_note_btn.setGeometry(QtCore.QRect(430, 380, 141, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.cancel_note_btn.setFont(font)
        self.cancel_note_btn.setObjectName("cancel_note_btn")
        self.cancel_note_btn.clicked.connect(self.close_dialog)

    def setup_ui(self):
        self._init_title_name_label()
        self._init_title_edit()
        self._init_preview_note()
        self._init_note_text_edit()
        self._init_note_content_label()
        self._init_preview_note_label()
        self._save_btn()
        self._cancel_btn()
        self.re_translate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def re_translate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("add_note_dialog", "Dialog"))
        self.title_name_label.setText(_translate("add_note_dialog", "标题名："))
        self.note_content_label.setText(_translate("add_note_dialog", "内容："))
        self.preview_note_label.setText(_translate("add_note_dialog", "预览："))
        self.save_note_btn.setText(_translate("add_note_dialog", "保存"))
        self.cancel_note_btn.setText(_translate("add_note_dialog", "取消"))

    def save_title_content(self):
        title_name = self.title_line_edit.text()
        content_txt = self.note_text_edit.toPlainText()
        if title_name in self.title_set:
            msg_box = QMessageBox(QMessageBox.Warning, "警告", "标题已存在请重新输入")
            msg_box.exec_()
        elif len(title_name) > 20:
            msg_box = QMessageBox(QMessageBox.Warning, "警告", "标题长度不能大于20个字符")
            msg_box.exec_()
        elif title_name and content_txt:
            self.title_set.add(title_name)
            self.send.send_signal((self.title_line_edit.text(), content_txt))
            self.title_line_edit.clear()
            self.note_text_edit.clear()
            self.close()
        else:
            msg_box = QMessageBox(QMessageBox.Warning, "警告", "文章标题和内容不能为空")
            msg_box.exec_()

    def close_dialog(self):
        self.close()

    def fresh_text_edit(self):
        self.preview_note.setMarkdown(self.note_text_edit.toPlainText())
