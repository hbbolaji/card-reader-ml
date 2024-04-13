from src.components.layoutdetection import LayoutDetection
from src.config.configuration import ConfigurationManager


class DetectionPipeline:
  def __init__(self) -> None:
    pass

  def main(self, img):
    classes = [
      'address',
      'flag',
      'gender',
      'heading',
      'ic_number',
      'level',
      'mykad',
      'mykad_icon',
      'mykid',
      'mykid_icon',
      'name',
      'religion'
    ]
    config_manager = ConfigurationManager()
    detection_config = config_manager.get_detection_config()

    detection = LayoutDetection(config=detection_config)
    result = detection.detect(img)
    print(result)
    return detection.detect(img)


