## 1、安装虚拟环境包
    pip3 install virtualenv

## 2、创建虚拟环境
    virtualenv venv
## 3、进入虚拟环境
    . venv/bin/activate(linux)
    venv\Scripts\activate(windows)

##### 3.1windows 可能报错
    # .\venv\Scripts\activate : 无法加载文件
    # 管理员身份进入WindowsPowerShell 
    # 输入Set-ExecutionPolicy PemoteSigned
    # 输入y
    # 重新进入虚拟环境即可

## 4、安装命令
    # 不建议安装pyqt6 会有很多版本冲突问题 或者安装6.0.1.3.2版本的pyqt6-tools
    # pip3 install PyQt6

##### 4.2 程序启动报错
    Traceback (most recent call last):
    from PyQt6.QtWidgets import QApplication
    ImportError: DLL load failed: 找不到指定的程序。
    # 因为可能存在包的版本冲突，所以卸载所有PyQt6相关包，重新安装，

## 5、Qdesinger 安装
    pip3 install PyQt6-tools
## 6、pycharm qdesigner 配置
    Program site-packages/qt5_applications/Qt/bin/designer.exe
    Arguments 空
    working directory $FileDir$

## 7、pyuic将ui文件转换为py文件
    pyuic5 -o xxx.py xxx.ui
