import cv2 as cv
from src.pipeline.stage_02_detection import DetectionPipeline

img = cv.imread('data/1.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

obj = DetectionPipeline()
obj.main(img)