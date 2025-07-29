import os # for reading and writing the data in the file
import cv2  # for image and video processing
import ultralytics #f Object detection in images and videos.
from ultralytics import YOLO
import matplotlib.pyplot as plt # to plot the image given by yolo

model_name="yolo11n-pose.pt" # storing pre-trained yolo model (.pt- storing weight and architecture also)

model=YOLO(model_name) # loading the model

img1_path="image.jpg" #storing the image

results=model(img1_path) #loading the image in results as an list it performs object detection 

type(results[0]) # it checks the type of first element in the result list

ultralytics.engine.results.Results # This class contains information about the detected objects, such as bounding boxes, labels, and confidence score

fig, ax=plt.subplots(figsize=(12,8)) # fig-creating the figure ax-subplotting the figure with the given size

ax.imshow(cv2.cvtColor(results[0].plot(),cv2.COLOR_BGR2RGB))

ax.axis("off") # to remove x and y axis

plt.show()





