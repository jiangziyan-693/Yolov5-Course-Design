from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys
import qtawesome
from detect import run, parse_opt
import os

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.selected_image_path = None
        self.result_dir = None
        self.class_counts = None
        self.init_ui()

    def init_ui(self):
        # 主布局
        self.setFixedSize(1400, 1000)
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
        self.left_close.setFixedSize(20, 20)  # Larger button size
        self.left_visit.setFixedSize(20, 20)
        self.left_mini.setFixedSize(20, 20)

        # Set button styles
        self.left_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.left_mini.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')

        # 设置按钮的工具提示
        self.left_close.setToolTip("关闭")
        self.left_visit.setToolTip("对选定的图像进行检测")
        self.left_mini.setToolTip("最小化")

        # Connect buttons to functions
        self.left_close.clicked.connect(self.close)
        self.left_visit.clicked.connect(self.run_detection)
        self.left_mini.clicked.connect(self.showMinimized)

        # 添加按钮到布局
        top_layout = QtWidgets.QHBoxLayout()
        top_layout.addWidget(self.left_visit)
        top_layout.addWidget(self.left_mini)
        top_layout.addWidget(self.left_close)
        self.left_layout.addLayout(top_layout)

        # 左侧按钮
        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.image', color='white'), " Input Image")
        self.left_button_1.setObjectName('left_button')
        self.left_button_1.setStyleSheet("font-size: 30px; font-family: Calibri;")  # 设置字体大小和字体

        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.eye', color='white'), " Show Result")
        self.left_button_2.setObjectName('left_button')
        self.left_button_2.setStyleSheet("font-size: 30px; font-family: Calibri;")  # 设置字体大小和字体

        self.left_button_clear = QtWidgets.QPushButton(qtawesome.icon('fa.trash', color='white'), " Clear Image")
        self.left_button_clear.setObjectName('left_button')
        self.left_button_clear.setStyleSheet("font-size: 30px; font-family: Calibri;")  # 设置字体大小和字体

        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.envelope', color='white'), " Contact or Help")
        self.left_button_3.setObjectName('left_button')
        self.left_button_3.setStyleSheet("font-size: 30px; font-family: Calibri;")  # 设置字体大小和字体

        # 将输入图像按钮连接到函数
        self.left_button_1.clicked.connect(self.open_image)

        # 将显示结果按钮连接到函数
        self.left_button_2.clicked.connect(self.show_result)

        # 将清除结果按钮连接到函数
        self.left_button_clear.clicked.connect(self.clear_image)

        # 添加按钮到布局
        self.left_layout.addWidget(self.left_button_1)
        self.left_layout.addWidget(self.left_button_2)
        self.left_layout.addWidget(self.left_button_clear)
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
        right_label = QtWidgets.QLabel("Welcome to Yolov5 Course Design")
        right_label.setStyleSheet("font-family: Calibri; font-size: 30px;")
        self.right_layout.addWidget(right_label)

        # 添加用于显示图片的 QLabel
        self.image_label = QtWidgets.QLabel(self.right_widget)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setFixedSize(800, 600)  # 设置 QLabel 的固定大小（可以根据需要调整）
        self.right_layout.addWidget(self.image_label)
        self.right_layout.addStretch()

        self.detected_classes_label = QtWidgets.QLabel(self.right_widget)
        self.detected_classes_label.setAlignment(QtCore.Qt.AlignCenter)
        self.detected_classes_label.setStyleSheet("font-family: Calibri; font-size: 28px; color: black;")
        self.right_layout.addWidget(self.detected_classes_label)
        self.right_layout.addStretch()

        # 设置布局间距
        self.right_layout.setSpacing(10)  # 可以调整这个值以改变间距

    def open_image(self):
        # 打开文件对话框选择图片
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "选择图片", "", "Image Files (*.png *.jpg *.bmp);;All Files (*)", options=options)
        if file_name:
            print(f"Selected file: {file_name}")
            self.selected_image_path = file_name
            self.display_image(file_name)

    def display_image(self, file_path):
        # 在 QLabel 中显示图片
        pixmap = QtGui.QPixmap(file_path)
        if pixmap.isNull():
            print("Failed to load image.")
            return
        self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

    def clear_image(self):
        # 清除 QLabel 上的图片
        self.image_label.clear()
        self.detected_classes_label.clear()

    def resizeEvent(self, event):
        # 当窗口大小改变时，保持图片适应 QLabel 尺寸
        if self.selected_image_path:
            self.display_image(self.selected_image_path)

    def run_detection(self):
        if not self.selected_image_path:
            print("No image selected.")
            return
        opt = parse_opt()  # 调用 parse_opt 获取默认参数
        # 修改参数
        opt.weights = 'runs/train/exp/weights/best.pt'
        opt.source = self.selected_image_path
        opt.conf_thres = 0.5  # 修改置信度阈值
        opt.iou_thres = 0.4  # 修改IoU阈值
        self.class_counts = run(**vars(opt))  # Assume run returns detected classes

    def get_latest_exp_directory(self, base_dir='runs/detect'):
        """Get the latest experiment directory based on the highest numbered exp folder."""
        exp_dirs = [d for d in os.listdir(base_dir) if d.startswith('exp') and os.path.isdir(os.path.join(base_dir, d))]
        # 过滤掉没有数字后缀的目录
        exp_dirs = [d for d in exp_dirs if d[3:].isdigit()]
        print(exp_dirs)
        if not exp_dirs:
            return None
        latest_exp_dir = max(exp_dirs, key=lambda x: int(x[3:]))  # Sort by number after 'exp'
        return f"{base_dir}/{latest_exp_dir}"

    def show_result(self):
        # 获取最新的结果目录
        self.result_dir = self.get_latest_exp_directory()
        print(self.result_dir)
        if not self.result_dir:
            print("No results directory found.")
            return

        # 获取目录中的图片文件
        if not os.listdir(self.result_dir):
            print("No list direction found.")
            return
        images = [f for f in os.listdir(self.result_dir) if f.endswith(('.png', '.JPG', '.jpeg'))]

        if images:
            # 选择第一张图片作为示例
            image_path = os.path.join(self.result_dir, images[0])

            # 加载并显示图片
            pixmap = QtGui.QPixmap(image_path)
            if pixmap.isNull():
                print("Failed to load result image.")
                return
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        else:
            # 如果没有找到图片，显示提示
            QtWidgets.QMessageBox.information(self, "No Image", "No images found in the specified directory.")

        print(self.class_counts)
        # 打印类别计数
        if self.class_counts:
            # 使用换行符格式化输出
            detected_text_lines = [f"{cls}: {count}" for cls, count in self.class_counts.items()]
            detected_text = "Detected Classes:\n" + "\n".join(detected_text_lines)
        else:
            detected_text = "No classes detected."

        # Update the QLabel with detected classes
        self.detected_classes_label.setText(detected_text)

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()