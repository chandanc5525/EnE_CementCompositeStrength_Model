import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "Ml_Model"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/data_loader.py",
    f"src/{project_name}/preprocessing.py",
    f"src/{project_name}/model.py",
    f"src/{project_name}/train.py",
    f"src/{project_name}/evaluate.py",
    f"src/{project_name}/predict.py",
    f"src/{project_name}/utils.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/config.yaml",

    "tests/__init__.py",
    "tests/test_data_loader.py",
    "tests/test_model.py",

    "notebooks/EDA.ipynb",
    "experiments/",

    "deployment/app.py",
    "deployment/Dockerfile",
    "deployment/requirements.txt",
    "deployment/gunicorn_config.py",

    ".github/workflows/ci.yaml",

    "logs/",
    ".gitignore",
    "README.md",
    "LICENSE",
    "setup.py",
    "pyproject.toml",
    "requirements.txt"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    if filepath.suffix or filepath.name.endswith('.gitignore'):
        # Create parent directories
        filedir = filepath.parent
        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory: {filedir} for the file: {filepath.name}")

        # Create file if it doesn't exist or is empty
        if not filepath.exists() or filepath.stat().st_size == 0:
            with open(filepath, "w") as f:
                pass
            logging.info(f"Creating empty file: {filepath}")
        else:
            logging.info(f"File already exists: {filepath}")
    else:
        # If it's a directory like "logs/" or "experiments/"
        os.makedirs(filepath, exist_ok=True)
        logging.info(f"Creating directory: {filepath}")
