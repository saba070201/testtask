from dotenv import load_dotenv
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(str(BASE_DIR) + "/.env")
POSTGRES_URL=os.getenv('POSTGRES_URL')
