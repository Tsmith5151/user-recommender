from flask import Flask

app = Flask(__name__)
import server.flask_app.views
