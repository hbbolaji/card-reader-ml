from components.layoutdetectiontraining import LayoutDetectionTraining
from config.configuration import ConfigurationManager


class TrainingPipeline:
  def __init__(self) -> None:
    pass

  def main(self):
    config_manager = ConfigurationManager()
    training_config = config_manager.get_layout_detection_config()

    training = LayoutDetectionTraining(config=training_config)
    training.train_model()


if __name__ == '__main__':
  try:
    obj = TrainingPipeline()
    obj.main()
  except Exception as e:
    raise