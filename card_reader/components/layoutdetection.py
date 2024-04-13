from ultralytics import YOLO
from src.entity.entity_config import DetectionConfig

class LayoutDetection:
  def __init__(self, config: DetectionConfig) -> None:
    self.config = config

  def detect(self, img):
    layouts = []
    model = YOLO(self.config.root_dir)
    result = model.predict(img)
    for res in result:
      boxes = res.boxes
      for box in boxes:
        layouts.append({'cls': int(box.cls.item()), 'xyxy': box.xyxy, 'conf':round( box.conf.item(), 3)})
    
    return layouts