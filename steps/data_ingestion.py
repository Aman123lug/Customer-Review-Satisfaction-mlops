import logging
import pandas as pd
from zenml import step

class DataIngestion:
    def __init__(self, dataPath: str) -> None:
        self.dataPath = dataPath
        
    def get_data(self) -> pd.DataFrame:
        data = pd.read_csv(self.dataPath)
        logging.info("Data Loaded Successfully")
        
        return data
    
@step
def ingest_df(dataPath: str) -> pd.DataFrame:
    """
    data Ingestion Stage
    Args:
        dataPath: CSV Data path
    Returns:
        pd.Dataframe: Pandas DataFrame
    """
    try:
        ingest_data = DataIngestion(dataPath)
        df = ingest_data.get_data()
        return df
    
    except Exception as e:
        logging.error(f"error in data ingestion {e}")
        raise e
                
    
    
