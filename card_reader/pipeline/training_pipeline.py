from card_reader.components.model_training import ModelTraining
from card_reader.config.configuration import ConfigurationManager


class TrainingPipeline:
  def __init__(self) -> None:
    pass

  def main(self):
    config_manager = ConfigurationManager()
    training_config = config_manager.get_model_training_config()

    model_training = ModelTraining(config=training_config)
    model_training.download_model()