from flask import Flask

app = Flask(__name__)

from isitbusy import routes
