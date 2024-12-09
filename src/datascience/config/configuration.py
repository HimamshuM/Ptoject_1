from src.datascience.constants import *
from src.datascience.utils.common import create_directories
from src.datascience.utils.common import read_yaml

from src.datascience.entity.config_entity import (dataIngestionConfig,DataValidationConfig)

# update the configuration manager in src conf 
class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH,
                 schema_filepath=SCHEMA_FILE_PATH):
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)
        self.schema=read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->dataIngestionConfig:
        config= self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = dataIngestionConfig(
            root_dir= config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config

    def get_data_validation_config(self)->DataValidationConfig:
        config= self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir= config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=config.unzip_data_dir,
            all_schema=schema
        )
        return data_validation_config