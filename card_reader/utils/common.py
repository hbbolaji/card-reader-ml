import os
import yaml
from box import ConfigBox
from ensure import ensure_annotations
from pathlib import Path

@ensure_annotations
def read_yaml(path:Path):
  try:
    with open(path) as f:
      content = yaml.safe_load(f)
      return ConfigBox(content)
  except ValueError:
    raise ValueError('yaml file is empty')
  except Exception as e:
    raise e

@ensure_annotations
def create_directories(path:str):
  if not path.exists():
    os.makedirs(path, exist_ok=True)

print(yaml.__version__)