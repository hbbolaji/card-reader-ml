import os
import gdown
from card_reader.entity.entity_config import ModelTrainingConfig
from card_reader.logger import logger

class ModelTraining:
  def __init__(self, config: ModelTrainingConfig) -> None:
    self.config = config
    os.makedirs(self.config.root_dir, exist_ok=True)
    os.makedirs('model', exist_ok=True)

  def download_model(self):
    try:
      if not os.path.exists(self.config.model_path):
        logger.info('Model not found, downloading model')
        model_id = self.config.trained_model_url.split('/')[-2]
        download_prefix = 'https://drive.google.com/uc?/export=download&id='
        gdown.download(download_prefix+model_id, output=self.config.model_path)
        gdown.download(download_prefix+model_id, output='model/best.pt')
      else:
        logger.info('Model already downloaded')
    except Exception as e:
      raise e