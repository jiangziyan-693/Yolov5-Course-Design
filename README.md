# Yolov5-Course-Design

> Author:Ziyan Jiang(ziy.jiang@outlook.com), Ying Zhu, Jiayi Jin

Yolov5(You Only Look Once Version 5) is an advanced object detection model, . YOLOv5 builds on the YOLO (You Only Look Once) series of models and is capable of performing object detection tasks in a single forward pass, simultaneously predicting multiple objects in an image along with their bounding boxes and classes.

Here are the steps to run the task.

## Resize the Origin Images

First, we resize the images that we take to 640*640, to make it sutiable for the following task, you could see the code in script `resize_images.py`. You could use it by just changing the data location.
