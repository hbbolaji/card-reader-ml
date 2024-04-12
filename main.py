from pipeline.stage_01_layout_detection_training import TrainingPipeline

STAGE_NAME = 'Training'

if __name__ == '__main__':
  try:
    obj = TrainingPipeline()
    obj.main()
  except Exception as e:
    raise
