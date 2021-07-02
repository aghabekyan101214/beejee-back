from flask import Flask
from flask_cors import CORS

from settings import settings

app = Flask(__name__)
CORS(app)

if __name__ == "__main__":
    app.run(debug=settings.DEBUG)
