# read data source from source example api or datalake or aws things of that nature
import sys
import os
from src.exception import CustomException
from logger import logging
import pandas as pd 

from sklearn.model_selection import train_test_split # ML libary
from dataclasses import dataclass

# inputs are required where you will recieve raw data or train data


@dataclass # be able to directly define class variable
class DataIngestionConfig:
    #there are inputs to dataingestion component -- there are used to know where to save ingested data
    train_data_path = str=os.path.join('artifacs', "train.csv")
    test_data_path = str=os.path.join('artifacs', "test.csv")
    raw_data_path = str=os.path.join('artifacs', "data.csv")


class DataIngestion:

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()        

    def initiate_data_ingestion(self):
        logging.info("entered the data ingestion method or component")
        try:
            ###path could also be anything from mongodb or other data source area
            df = pd.read_csv('notebook/stud.csv')
            logging.info('Reading dataset from csv file - read it as a dataframe with pandas----------')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated after making file csv file")
            # splits total df into two sections one for testing and the other for training in this case the .2 is 20% of the total df to be tested
            train_set, test_set = train_test_split(df, test_size=.20,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("ingestion is done now ---------")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__name__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()