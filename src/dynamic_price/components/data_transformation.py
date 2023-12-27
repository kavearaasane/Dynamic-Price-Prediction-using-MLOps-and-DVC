import os
from dynamic_price import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import preprocessing
from dynamic_price.entity.config_entity import DataTransformationConfig



class DataTransformationConfig:
    def __init__(self, data_path, root_dir):
        self.data_path = data_path
        self.root_dir = root_dir

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def label_encode_columns(self, data, columns):
        label_encoder = preprocessing.LabelEncoder()

        for column in columns:
            data[column] = label_encoder.fit_transform(data[column])

        return data

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        # Label encode specific columns
        columns_to_encode = ['Location_Category', 'Time_of_Booking', 'Vehicle_Type', 'Customer_Loyalty_Status']
        data = self.label_encode_columns(data, columns_to_encode)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)


        print(train.shape)
        print(test.shape)
      

    
        