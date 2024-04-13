from card_reader.config.configuration import ConfigurationManager
from card_reader.components.data_validation import DataValidation


class ValidationPipeline:
  def __init__(self) -> None:
    pass

  def main(self):
    config_manager = ConfigurationManager()
    validation_config = config_manager.get_data_validation()

    validation = DataValidation(config=validation_config)
    is_valid = validation.validate()
    return is_valid