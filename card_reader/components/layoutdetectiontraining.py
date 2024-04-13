from ultralytics import YOLO
from entity.entity_config import DetectionTrainingConfig

class LayoutDetectionTraining:
  def __init__(self, config: DetectionTrainingConfig) -> None:
    self.config = config

  def train_model(self):
    model = YOLO(self.config.model)
    model.train()