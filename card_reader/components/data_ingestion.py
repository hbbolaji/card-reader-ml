import os
from entity.entity_config import DataIngestionConfig
from pathlib import Path


class DataIngestion:
  def __init__(self, config: DataIngestionConfig) -> None:
    self.config = config
    os.makedirs(self.config.root_dir, exist_ok=True)

  def download_data(self):
    pass

  def unzip_data(self):
    pass
