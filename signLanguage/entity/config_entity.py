import os
from dataclasses import dataclass
from datetime import datetime
from signLanguage.constant.training_pipeline import *

# Generate a unique timestamp for directories
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

@dataclass
class TrainingPipelineConfig:
    # Base directory for all training artifacts
    artifacts_dir: str = os.path.join(ARTIFACTS_DIR, TIMESTAMP)

# Initialize the training pipeline configuration
training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    # Directory for data ingestion artifacts
    data_ingestion_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir, DATA_INGESTION_DIR_NAME
    )

    # Path to store extracted features
    feature_store_file_path: str = os.path.join(
        data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR
    )

    # URL for downloading the data
    data_download_url: str = DATA_DOWNLOAD_URL
