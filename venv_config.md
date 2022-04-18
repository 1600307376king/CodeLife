## 1、进入虚拟环境
    . venv/bin/activate(linux)
    venv\Scripts\activate(windows)

##### 1.1windows 可能报错
    # .\venv\Scripts\activate : 无法加载文件
    # 管理员身份进入WindowsPowerShell 
    # 输入Set-ExecutionPolicy PemoteSigned
    # 输入y
    # 重新进入虚拟环境即可

## 2、安装命令
    # pip3 install PyQt6

##### 2.2 程序启动报错
    Traceback (most recent call last):
    from PyQt6.QtWidgets import QApplication
    ImportError: DLL load failed: 找不到指定的程序。
    # 因为可能存在包的版本冲突，所以卸载所有pyqt6相关包，重新安装，