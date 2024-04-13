import sys, os
from entity.entity_config import DataIngestionConfig
from config.configuration import ConfigurationManager
from components.data_ingestion import DataIngestion

class TrainingPipeline:
  def __init__(self) -> None:
    pass

  def main(self):
    config_manager = ConfigurationManager()
    data_ingestion_config = config_manager.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_data()