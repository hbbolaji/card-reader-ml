import sys, os
from card_reader.entity.entity_config import DataIngestionConfig
from card_reader.config.configuration import ConfigurationManager
from card_reader.components.data_ingestion import DataIngestion

class DataIngestionPipeline:
  def __init__(self) -> None:
    pass

  def main(self):
    config_manager = ConfigurationManager()
    data_ingestion_config = config_manager.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_data()
    data_ingestion.unzip_data()