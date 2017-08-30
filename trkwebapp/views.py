from flask import Blueprint, render_template, request, send_file
from flask import current_app # current_app is only accessible within a request

trkwebapp = Blueprint('trkwebapp', __name__)

@trkwebapp.route('/')
def index():
    return render_template('index.html')