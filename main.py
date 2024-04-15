from card_reader.pipeline.ingestion_pipeline import DataIngestionPipeline
from card_reader.pipeline.validation_pipeline import ValidationPipeline
from card_reader.pipeline.training_pipeline import TrainingPipeline 


obj = DataIngestionPipeline()
obj.main()

obj = ValidationPipeline()
obj.main()

obj = TrainingPipeline()
obj.main()

