import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "tripPlanner"

list_of_files = [
    ".github/workflows/.gitkeep",
    ".streamlit/config.toml",
    ".env",
    f"{project_name}/__init__.py",
    f"{project_name}/agent/__init__.py",
    f"{project_name}/agent/workflow.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/config.yaml",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/prompt_library/__init__.py",
    f"{project_name}/prompt_library/prompt.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    f"{project_name}/tools/__init__.py",
    "research/trials.ipynb", 
    "main.py",
    "agent.py",
    "streamlit_app.py",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    
    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filename}")    
    else:
        logging.info(f"File already exists: {filename}")