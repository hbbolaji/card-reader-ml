from src.utils.common import read_yaml
from src.constants import *
from src.entity.entity_config import DetectionTrainingConfig, DetectionConfig

class ConfigurationManager:
  def __init__(self,
               config = CONFIG_FILE_PATH,
               params= PARAMS_FILE_PATH) -> None:
    self.config = read_yaml(config)
    self.params = read_yaml(params)

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