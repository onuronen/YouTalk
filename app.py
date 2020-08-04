import os
import sys
sys.path.append(os.getcwd())
from src.main import make_app

app = make_app()
app.run()