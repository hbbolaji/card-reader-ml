import os
from card_reader.logger import logger
from card_reader.entity.entity_config import DataValidationConfig


class DataValidation:
  def __init__(self, config:DataValidationConfig) -> None:
    self.config = config
    os.makedirs(self.config.root_dir, exist_ok=True)
    pass

  def validate(self) -> bool:
    try:
      validation_status = None
      required_files = self.config.all_required_files
      directory = os.listdir('artifacts/data_ingestion/feature_store')
      for file in required_files:
        if file not in directory:
          logger.info(f'{file} not found!')
          validation_status = False
          os.makedirs(self.config.root_dir, exist_ok=True)
          with open(self.config.status_file, 'w') as f:
            f.write(f'Validation Status: {validation_status}')
        else:
          logger.info(f'{file} found!')
          validation_status = True
          os.makedirs(self.config.root_dir, exist_ok=True)
          with open(self.config.status_file, 'w') as f:
            f.write(f'Validation Status: {validation_status}')
      return validation_status
    except Exception as e:
      raise e