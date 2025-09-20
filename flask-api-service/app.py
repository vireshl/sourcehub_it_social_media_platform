from flask import Flask
from src.main import main_bp
from src.logger import setup_logger

app = Flask(__name__)

# Set up logger
logger = setup_logger()

if __name__ == '__main__':
    app.run(debug=True)
