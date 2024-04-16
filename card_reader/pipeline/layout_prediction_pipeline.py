from ultralytics import YOLO
import numpy as np
from pathlib import Path
from easyocr import Reader

from card_reader.utils.common import read_yaml
from card_reader.logger import logger

# image = cv.imread('data/8.jpg')
# image = cv.cvtColor(image, cv.COLOR_BGR2RGB)


class LayoutPredictionPipeline:
  def __init__(self) -> None:
    self.model = YOLO('model/best.pt')
    self.classes = read_yaml(Path('model/data.yaml')).names
    self.reader = Reader(['en'], detector="DB", gpu=False)

  def layout_extraction(self, image, box):
      x1, y1, x2, y2 = box.xyxy[0]
      x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
      return image[y1:y2, x1:x2]
  
  def text_extraction(self, output):
    text = []
    for item in output:
      text.append(item[1])
    return text
  
  def get_class(self, id):
    return self.classes[int(id)]
  
  def is_excluded(self, class_name):
    exclude = ['mykad', 'mykid', 'mykad_icon', 'mykid_icon', 'flag', 'heading']
    return class_name in exclude

  
  def get_card(self, image):
    image = np.array(image)
    result = self.model.predict(image)
    for res in result:
      boxes = res.boxes
      for box in boxes:
        if self.get_class(box.cls) == 'mykad':
          self.card = self.layout_extraction(image, box)
  
  def predict(self):
    try:
      response = {}
      result = self.model(self.card)
      for res in result:
        boxes = res.boxes
        logger.info('Cropping IC from image')
        for box in boxes:
          class_name = self.get_class(box.cls)
          if not self.is_excluded(class_name):
            layout = self.layout_extraction(self.card, box)
            output = self.reader.readtext(layout)
            text = self.text_extraction(output=output)
            if class_name not in response.keys():
              response[class_name] = text
      logger.info('Text Extracted')
      return response
    except Exception as e:
      logger.error(e)
      raise e
