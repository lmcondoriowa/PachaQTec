from flask import Flask
from dotenv import load_dotenv
from pathlib import Path
from routes import route, route_error

app = Flask(__name__)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

route.routes(app)
route_error.error_handler(app)

if __name__ == '__main__':
    app.run()

