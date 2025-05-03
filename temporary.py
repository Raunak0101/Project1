import os ##finds the generic folder path
from pathlib import Path 
import logging 

logging.basicConfig(level=logging.INFO)

project_name = "mlproject"

list_of_file = [
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
    "main.py
    "Dockerfile",
    "requirements.txt",
    "setup.py"





]

for file_path in list_of_file:
    filepath = Path(file_path)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok= True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass 
            logging.info(f"Creating empty file:{filepath}")

    else:
        logging.info(f"{filename} is already exists")