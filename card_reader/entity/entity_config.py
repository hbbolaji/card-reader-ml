from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
  root_dir: str
  feature_store_dir: str
  data_download_url: str
  download_path: str

@dataclass(frozen=True)
class DataValidationConfig:
  root_dir: str
  status_file: Path
  all_required_files: list

@dataclass(frozen=True)
class ModelTrainingConfig:
  root_dir: str
  model_name: str
  model_path: str
  epoch: int
  trained_model_url: str
