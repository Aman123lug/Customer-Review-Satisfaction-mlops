import logging
import zenml
from zenml import pipeline
from steps.data_ingestion import ingest_df
from steps.data_preprocessing import clean_data
from steps.model_trainer import model_training
from steps.evaluation import model_evaluation


@pipeline
def train_pipelines(dataPath: str):
    ingest_data = ingest_df(dataPath)
    clean_data(ingest_data)
    model_training(clean_data)
    model_evaluation(clean_data)
    
    
    
    
    
    
    