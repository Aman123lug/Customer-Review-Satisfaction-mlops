import logging 
import numpy as np
import pandas as pd

from abc import ABC, abstractmethod
from typing import Union
from sklearn.model_selection import train_test_split

class DataStrategy(ABC):
    """
    abstract method
    """
    @abstractmethod
    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
        
        pass
    
class DataPreprocessingStrategy:
    """
    actual class that contains abstract method
    """
    
    def handle_data(self, data: pd.DataFrame) -> pd.DataFrame:
        
        try:
            data = data.drop(
                ["order_approved_at",
                 "order_delivered_carrier_date",
                 "order_delivered_customer_date",
                 "order_estimated_delivery_date",
                 "order_purchase_timestamp"
            
                 ], axis=1
            )
            
            data["product_weight_g"].fillna(data["product_weight_g"].median(), inplace=True)
            data["product_length_cm"].fillna(data["product_length_cm"].median(), inplace=True)
            data["product_height_cm"].fillna(data["product_height_cm"].median(), inplace=True)
            data["product_width_cm"].fillna(data["product_width_cm"].median(), inplace=True)
            data["review_comment_message"].fillna("No Review", inplace=True)
            
            data = data.select_dtypes(include=[np.number])
            data = data.drop(columns=["customer_zip_code_prefix", "order_item_id"], axis=1)
            
            return data
        
        except Exception as e:
            logging.error("Error in Preprocessing data : {}".format(e))
            raise e
            
            
    
class DataDivideStrategy(DataStrategy):
    
    def handle_data(self, data: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
        
        try:
            X = data.drop("review_score", axis=1)
            y = data["review_score"]
            
            X_train, y_train, X_test, y_test = train_test_split(X, y, random_state=42, test_size=0.30)
            
            return X_train, y_train, X_test, y_test
        
        except Exception as e:
            logging.error("SOme thing wrong in train test split")
            raise e
        
class DataCleaning:
    def __init__(self, data: pd.DataFrame, strategy: DataStrategy):
        self.data = data
        self.strategy = strategy
        
        
    def handle_data(self) -> Union[pd.DataFrame, pd.Series]:
        
        try: 
            return self.strategy.handle_data(self.data)
        except Exception as e:
            logging.error("Error in Handing Data")
            raise e

if __name__ == "__main__":
            
    data = pd.read_csv("data\olist_customers_dataset.csv")
    data_cleaning = DataCleaning(data, DataPreprocessingStrategy())
    data_cleaning.handle_data()

    