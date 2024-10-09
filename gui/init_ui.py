from PyQt5 import QtCore,QtGui,QtWidgets
import sys
import qtawesome

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 主布局
        self.setFixedSize(960, 700)
        self.setWindowTitle('My Application')
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QGridLayout()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

        # 左侧部件
        self.left_widget = QtWidgets.QWidget()
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QVBoxLayout()
        self.left_widget.setLayout(self.left_layout)

        # 右侧部件
        self.right_widget = QtWidgets.QWidget()
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QVBoxLayout()
        self.right_widget.setLayout(self.right_layout)

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)

        # 标题栏按钮
        # Initialize buttons
        self.left_close = QtWidgets.QPushButton("")
        self.left_visit = QtWidgets.QPushButton("")
        self.left_mini = QtWidgets.QPushButton("")

        # Set button sizes
        self.left_close.setFixedSize(15, 15)
        self.left_visit.setFixedSize(15, 15)
        self.left_mini.setFixedSize(15, 15)

        # Set button styles
        self.left_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        # Connect buttons to functions
        self.left_close.clicked.connect(self.close)
        self.left_visit.clicked.connect(self.showMinimized)
        self.left_mini.clicked.connect(self.showNormal)

        # 添加按钮到布局
        top_layout = QtWidgets.QHBoxLayout()
        top_layout.addWidget(self.left_mini)
        top_layout.addWidget(self.left_visit)
        top_layout.addWidget(self.left_close)
        self.left_layout.addLayout(top_layout)

        # 左侧按钮
        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.image', color='white'), "Input Image")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.eye', color='white'), "Show Result")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.envelope', color='white'), "Contact or Help")
        self.left_button_3.setObjectName('left_button')

        # 添加按钮到布局
        self.left_layout.addWidget(self.left_button_1)
        self.left_layout.addWidget(self.left_button_2)
        self.left_layout.addWidget(self.left_button_3)

        # 样式美化
        self.setStyleSheet('''
            #left_widget {
                background: #2c3e50;
                border-top-left-radius: 10px;
                border-bottom-left-radius: 10px;
            }
            QPushButton {
                border: none;
                color: white;
                font-size: 16px;
                height: 40px;
                padding-left: 5px;
                padding-right: 10px;
                text-align: left;
            }
            QPushButton#left_button:hover {
                color: #FFD700;
                background: #34495e;
            }
        ''')

        # 在右侧添加一些占位内容作为示例
        self.right_layout.addWidget(QtWidgets.QLabel("Welcome to Yolov5 Course Design"))
        self.right_layout.addStretch()

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()