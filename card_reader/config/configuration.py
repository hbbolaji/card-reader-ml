from utils.common import read_yaml
from constant import *
from entity.entity_config import DetectionTrainingConfig, DetectionConfig, DataIngestionConfig

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
      data_download_url= config.data_download_url
    )
    return data_ingestion_config


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