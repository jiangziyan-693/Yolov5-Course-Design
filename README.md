# Yolov5-Course-Design

> Author:Ziyan Jiang(ziy.jiang@outlook.com), Ying Zhu, Jiayi Jin

Yolov5(You Only Look Once Version 5) is an advanced object detection model, . YOLOv5 builds on the YOLO (You Only Look Once) series of models and is capable of performing object detection tasks in a single forward pass, simultaneously predicting multiple objects in an image along with their bounding boxes and classes.

Here are the steps to run the task.

## Resize the Origin Images

First, we resize the images that we take to 640*640, to make it sutiable for the following task, you could see the code in script `resize_images.py`. You could use it by just changing the data location.

## Use LabelImg to label the data

To change the origin images to annotations, we use the tool `LabelImg` to mark the data, the code is in the folder `labelimg`.

## Use Yolov5 to train the model

We use yolov5 to train the model, the image in folder `yolo/course_design/images`, the labels in folder `yolo/course_design/labels`, you can change training set, validation set, number of classes, class names in `info.yaml`.

To train the model, adjust the config in  `run_course_design.sh`, and input following code in terminal:

```py
sh run_course_design.sh
```

After training, you will get the result in folder `yolo/runs/train`.

## Visualizing results with PyQt5

We use PyQt5 to visualize the detecting results. You can read the detailed code in the folder `yolo/init_ui.py`.

We realize the following functions:

1. Input image: by clicking the "Input Image" button, you can choose a image from your computer, and at the same time show the image in the right layout.
2. Run detection: by clicking the green button on the top of the left layout, you can start detecting the image you input.
3. Show result: by clicking the "Show Result" button, you can see the detection image as well as all the categories in the right layout.
4. Clear image: by clicking the "Show Result" button, you can clear the result.
5. Show minimized: by clicking the yellow button on the top of the left layout, you can minimize the window.
6. Close: by clicking the yellow button on the top of the left layout, you can close the window.