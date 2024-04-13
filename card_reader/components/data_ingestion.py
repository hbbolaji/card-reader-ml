import os
import zipfile
import gdown
from card_reader.entity.entity_config import DataIngestionConfig
from card_reader.logger import logger


class DataIngestion:
  def __init__(self, config: DataIngestionConfig) -> None:
    self.config = config
    os.makedirs(self.config.root_dir, exist_ok=True)

  def download_data(self):
    try:
      if not os.path.exists(self.config.download_path):
        logger.info('downloading')
        file_id: str = self.config.data_download_url.split('/')[-2]
        download_prefix = 'https://drive.google.com/uc?/export=download&id='
        gdown.download(url=download_prefix+file_id, output=self.config.download_path)
      else:
        logger.info('Dataset downloaded')
    except Exception as e:
      raise e

  def unzip_data(self):
    if not os.path.exists(self.config.feature_store_dir):
      try:
        logger.info('Unzipping')
        os.makedirs(self.config.feature_store_dir)
        with zipfile.ZipFile(self.config.download_path, 'r') as zip_file:
          zip_file.extractall(self.config.feature_store_dir)
      except Exception as e:
        raise e
    else:
      logger.info('Unzipping done')

