import os 
import urllib.request as request
from src.datascience import logger
import zipfile

from src.datascience.entity.config_entity import (dataIngestionConfig)

#component - Data ingestion
class DataIngestion:
    def __init__(self,config:dataIngestionConfig):
        self.config = config

    # downloading zip file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers=request.urlretrieve(
                url = self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download with following info: \n{headers}")
        else:
            logger.info(f"File already exists")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)