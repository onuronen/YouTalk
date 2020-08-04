import os
import sys
sys.path.append(os.getcwd())
from src.main import make_app

if __name__ == '__main__':
    app = make_app()
    app.run()