from card_reader.pipeline.training_pipeline import TrainingPipeline
from card_reader.pipeline.validation_pipeline import ValidationPipeline


obj = TrainingPipeline()
obj.main()

obj = ValidationPipeline()
obj.main()