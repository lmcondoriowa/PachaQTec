from dotenv import load_dotenv
from pathlib import Path
from flask import Flask
from routes import route, route_error

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)

route.routes(app)
route_error.error_handler(app)

if __name__ == '__main__':
    app.run()
