import os 
from pathlib import Path 
import logging 

logging.basicConfig(level=logging.INFO)

project_name = "mlproject"

list_of_file = [
    "github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/componemts/__init__.py",
    f"src/{project_name}/componemts/data_ingestion.py",
    f"src/{project_name}/componemts/data_transformation.py",
    f"src/{project_name}/componemts/model.trainer.py",
    f"src/{project_name}/componemts/model_monitoring.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utlis.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"





]