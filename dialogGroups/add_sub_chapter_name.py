# -*- coding: utf-8 -*-
"""
add chapter name dialog
"""
import os
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtCore import QMetaObject
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMessageBox
from com_manager.add_chapter_name_com import ADD_CHAPTER_NAME_DIALOG_SIZE
from com_manager.add_chapter_name_com import CHAPTER_NAME_EDIT_MAX_WIDTH
from com_manager.add_chapter_name_com import CHAPTER_NAME_LABEL_MAX_WIDTH
from com_manager.add_chapter_name_com import SAVE_BTN_MAX_WIDTH
from com_manager.add_chapter_name_com import CANCEL_BTN_MAX_WIDTH
from com_manager.add_chapter_name_com import CHAPTER_FIND_BTN_MAX_WIDTH
from com_manager.add_chapter_name_com import CHAPTER_FIND_LABEL_MAX_WIDTH
from config import MAX_SIZE_NUM
from dialogGroups.base_dialog import BaseDialog


class AddChapterName(BaseDialog):
    """
    add chapter name dialog class
    """
    def __init__(self, chapter_set):
        super().__init__()
        self.resize(*ADD_CHAPTER_NAME_DIALOG_SIZE)
        self.central_widget = QWidget(self)

        self.vertical_layout = QVBoxLayout(self.central_widget)

        self.chapter_name_frame = QFrame(self.central_widget)
        self.horizontalLayout = QHBoxLayout(self.chapter_name_frame)
        self.chapter_name_label = QLabel(self.chapter_name_frame)
        self.horizontalLayout.addWidget(self.chapter_name_label)
        self.lineEdit = QLineEdit(self.chapter_name_frame)
        self.horizontalLayout.addWidget(self.lineEdit)
        self.vertical_layout.addWidget(self.chapter_name_frame)

        self.chapter_content_frame = QFrame(self.central_widget)
        self.chapter_content_h_layout = QHBoxLayout(self.chapter_content_frame)
        self.find_src_btn = QPushButton(self.chapter_content_frame)
        self.src_path_label = QLabel(self.chapter_content_frame)
        self.chapter_content_h_layout.addWidget(self.find_src_btn)
        self.chapter_content_h_layout.addWidget(self.src_path_label)
        self.vertical_layout.addWidget(self.chapter_content_frame)

        self.btn_frame = QFrame(self.central_widget)
        self.btn_horizontal_layout = QHBoxLayout(self.btn_frame)
        self.save_btn = QPushButton(self.btn_frame)
        self.cancel_btn = QPushButton(self.btn_frame)
        self.vertical_layout.addWidget(self.btn_frame)

        self.setCentralWidget(self.central_widget)
        self.chapter_set = chapter_set

    def _close_dialog(self):
        self.lineEdit.clear()
        self.src_path_label.setText("资源路径")
        self.close_dialog()

    def _add_chapter(self):
        title_name = self.lineEdit.text()
        if title_name in self.chapter_set:
            msg_box = QMessageBox(QMessageBox.Warning, "警告", "标题已存在请重新输入")
            msg_box.exec_()
        else:
            self.send.send_signal((self.lineEdit.text(), self.src_path_label.text()))
            self.src_path_label.setText("资源路径")
            self.lineEdit.clear()
            self.close()

    def _find_typora_files(self):
        """
        查找tpora文件并添加到章节列表显示
        :return:
        """
        opened_file = QFileDialog.getOpenFileName(self, "open file", "/", filter="Html (*.html)")
        if opened_file:
            if os.path.exists(opened_file[0]):
                self.src_path_label.setText(opened_file[0])

    def _init_central_widget(self):
        """
        set widget
        :return:
        """
        self.central_widget.setObjectName("central_widget")

    def _init_vertical_layout(self):
        """
        set two frame vertical layout
        :return:
        """
        self.vertical_layout.setObjectName(u"verticalLayout")

    def _init_chapter_name_frame(self):
        """
        set chapter name frame
        :return:
        """
        self.chapter_name_frame.setObjectName(u"chapter_name_frame")
        self.chapter_name_frame.setFrameShape(QFrame.StyledPanel)
        self.chapter_name_frame.setFrameShadow(QFrame.Raised)
        # self.chapter_name_frame.setStyleSheet("background-color: rgb(138, 255, 167);")

    def _init_chapter_name_horizontal_layout(self):
        """
        set chapter name horizontal layout
        :return:
        """
        self.horizontalLayout.setObjectName(u"horizontalLayout")

    def _init_chapter_name_label(self):
        """
        set chapter name label
        :return:
        """
        self.chapter_name_label.setObjectName(u"chapter_name_label")
        self.chapter_name_label.setMaximumSize(QSize(CHAPTER_NAME_LABEL_MAX_WIDTH, MAX_SIZE_NUM))
        self.chapter_name_label.setStyleSheet("background-color: rgb(135, 163, 255);")

    def _init_chapter_name_edit(self):
        """
        set chapter name input edit
        :return: 
        """
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(CHAPTER_NAME_EDIT_MAX_WIDTH, MAX_SIZE_NUM))
        self.lineEdit.setStyleSheet("background-color: rgb(135, 163, 255);")

    def _init_chapter_add_frame(self):
        """
        set chapter add btn and src file path label frame
        :return:
        """
        self.chapter_content_frame.setObjectName("chapter_content_frame")
        self.chapter_content_frame.setFrameShape(QFrame.StyledPanel)
        self.chapter_content_frame.setFrameShadow(QFrame.Raised)

    def _init_chapter_layout(self):
        self.chapter_content_h_layout.setObjectName("chapter_content_h_layout")

    def _init_chapter_add_btn(self):
        self.find_src_btn.setObjectName("find_src_btn")
        self.find_src_btn.setMaximumSize(QSize(CHAPTER_FIND_BTN_MAX_WIDTH, MAX_SIZE_NUM))
        self.find_src_btn.clicked.connect(self._find_typora_files)

    def _init_chapter_add_label(self):
        self.src_path_label.setObjectName("src_path_label")
        self.src_path_label.setMaximumSize(QSize(CHAPTER_FIND_LABEL_MAX_WIDTH, MAX_SIZE_NUM))

    def _init_btn_frame(self):
        """
        set double button frame
        :return:
        """
        self.btn_frame.setObjectName(u"btn_frame")
        self.btn_frame.setFrameShape(QFrame.StyledPanel)
        self.btn_frame.setFrameShadow(QFrame.Raised)

    def _init_btn_horizontal_layout(self):
        """
        set button layout
        :return:
        """
        self.btn_horizontal_layout.setObjectName(u"btn_horizontal_layout")
        self.btn_horizontal_layout.addWidget(self.save_btn)
        self.btn_horizontal_layout.addWidget(self.cancel_btn)

    def _init_btn(self):
        """
        set double button
        :return:
        """
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMaximumSize(QSize(SAVE_BTN_MAX_WIDTH, MAX_SIZE_NUM))
        self.save_btn.clicked.connect(self._add_chapter)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMaximumSize(QSize(CANCEL_BTN_MAX_WIDTH, MAX_SIZE_NUM))
        self.cancel_btn.clicked.connect(self._close_dialog)

    def setup_ui(self):
        self._init_central_widget()
        self._init_vertical_layout()
        self._init_chapter_name_frame()
        self._init_chapter_name_horizontal_layout()
        self._init_chapter_name_label()
        self._init_chapter_name_edit()
        self._init_chapter_add_frame()
        self._init_chapter_layout()
        self._init_chapter_add_btn()
        self._init_chapter_add_label()

        self._init_btn_frame()
        self._init_btn_horizontal_layout()
        self._init_btn()

        self.re_translate_ui()
        QMetaObject.connectSlotsByName(self)

    def re_translate_ui(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"创建章节名称"))
        self.chapter_name_label.setText(QCoreApplication.translate("MainWindow", u"章节名称"))
        self.find_src_btn.setText(QCoreApplication.translate("MainWindow", "打开资源"))
        self.src_path_label.setText(QCoreApplication.translate("MainWindow", "资源路径"))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"保存"))
        self.cancel_btn.setText(QCoreApplication.translate("MainWindow", u"取消"))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    add_dialog = AddChapterName(set())
    add_dialog.setup_ui()
    add_dialog.show()
    sys.exit(app.exec())
