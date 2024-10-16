import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
import cv2
import numpy as np
from ultralytics import YOLO

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'YOLOv8 Object Detection'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # 创建按钮
        button = QPushButton('Select Image', self)
        button.clicked.connect(self.on_button_click)

        # 创建显示图像的标签
        self.image_label = QLabel(self)
        self.image_label.setFixedSize(640, 480)

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(self.image_label)
        self.setLayout(layout)

        # 加载模型
        self.model = YOLO('last.pt')

    def on_button_click(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "Images (*.png *.jpg *.jpeg)", options=options)
        if filename:
            # 读取图像
            img = cv2.imread(filename)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # 进行预测
            results = self.model.predict(source=img)[0]
            boxes = results.boxes.xyxy.cpu().numpy().astype(int)
            class_ids = results.boxes.cls.cpu().numpy().astype(int)
            labels = [results.names[class_id] for class_id in class_ids]


            # 绘制边界框
            for box, label in zip(boxes, labels):
                x1, y1, x2, y2 = box
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # 保存结果图像
            result_img = results.plot()
            save_filename = 'detection_result.jpg'
            cv2.imwrite(save_filename, cv2.cvtColor(result_img, cv2.COLOR_RGB2BGR))
            print(f"Result saved as {save_filename}")

            # 显示结果
            h, w, ch = result_img.shape
            bytesPerLine = ch * w
            qImg = QImage(result_img.data, w, h, bytesPerLine, QImage.Format_RGB888)
            qPixmap = QPixmap.fromImage(qImg).scaled(self.image_label.width(), self.image_label.height())
            self.image_label.setPixmap(qPixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
