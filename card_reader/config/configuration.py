from pathlib import Path

from card_reader.utils.common import read_yaml
from card_reader.constant import *
from card_reader.entity.entity_config import DetectionTrainingConfig, DetectionConfig, ModelTrainingConfig, DataIngestionConfig, DataValidationConfig

class ConfigurationManager:
  def __init__(self,
               config = CONFIG_FILE_PATH,
               params= PARAMS_FILE_PATH) -> None:
    self.config = read_yaml(config)
    self.params = read_yaml(params)

  def get_data_ingestion_config(self) -> DataIngestionConfig:
    config = self.config.data_ingestion
    data_ingestion_config = DataIngestionConfig(
      root_dir=config.root_dir,
      feature_store_dir= config.feature_store_dir,
      data_download_url= config.data_download_url,
      download_path=config.download_path
    )
    return data_ingestion_config
  
  def get_data_validation(self) -> DataValidationConfig:
    config = self.config.data_validation
    data_validation_config = DataValidationConfig(
      root_dir=config.root_dir,
      status_file=config.status_file,
      all_required_files=config.all_required_files
    )
    return data_validation_config
  
  def get_model_training_config(self) -> ModelTrainingConfig:
    config = self.config.model_training
    params = self.params
    model_training_config = ModelTrainingConfig(
      root_dir=config.root_dir,
      model_path=config.model_path,
      trained_model_url= config.trained_model_url,
      model_name=params.MODEL_NAME,
      epoch=params.EPOCH
    )
    return model_training_config

  def get_layout_detection_config(self) -> DetectionTrainingConfig:
    config = self.config.detection_training
    params = self.params
    return DetectionTrainingConfig(
      root_dir=config.root_dir,
      model= params.MODEL,
      mode = params.MODE,
      task = params.TASK,
      epoch = params.EPOCH
    )
  
  def get_detection_config(self) -> DetectionConfig:
    config = self.config.detection
    return DetectionConfig(
      root_dir = config.root_dir
    )