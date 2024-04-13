from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class DataIngestionConfig:
  root_dir: str
  feature_store_dir: str
  data_download_url: str

@dataclass(frozen=True)
class DetectionTrainingConfig:
  root_dir: Path
  model: str
  mode: str
  task: str
  epoch: int

@dataclass(frozen=True)
class DetectionConfig:
  root_dir: Path