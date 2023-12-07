import os
import logging
from flask import Blueprint, render_template, send_file, abort
from flask_login import login_required
from google.cloud import storage

from db import db

main = Blueprint('main', __name__)


@main.route('/')
@login_required
def index():
    return render_template('index.html')

@main.route('/download/<blob_name>')
@login_required
def download_csv(blob_name):
    bucket_name = 'ketul_q1_coivd_data'
    try:
        key_file_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS', '/app/q1-key-file.json')
        # client = storage.Client()
        client = storage.Client.from_service_account_json(key_file_path)

        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)

        temp_file_path = f'/tmp/{blob_name}'
        blob.download_to_filename(temp_file_path)

        return send_file(temp_file_path, as_attachment=True, download_name=f'{blob_name}')
    except Exception as err:
        logging.error(f'Error while downloading file: {err}')
        abort(500)

    
