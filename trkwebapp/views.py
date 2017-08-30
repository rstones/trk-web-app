from flask import Blueprint, render_template, request, send_file
from flask import current_app # current_app is only accessible within a request

trkwebapp = Blueprint('trkwebapp', __name__)

@trkwebapp.route('/')
def index():
    return render_template('index.html')

@trkwebapp.route('/get_trk')
def get_trk():
    return send_file('../data/BRCATLASB088_MNI_AF_long.trk', as_attachment=True, attachment_filename='test.trk', conditional=True, add_etags=True)