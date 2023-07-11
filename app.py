from flask import Flask, request
from upload import upload_data
from batch_insert import insert_batch

app = Flask(__name__)

@app.route('/upload_deps', methods=['POST'])
def upload_deps():

    # Check if a file was uploaded
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']

    return upload_data(file,"departments","other")


@app.route('/upload_jobs', methods=['POST'])
def upload_jobs():

    # Check if a file was uploaded
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']

    return upload_data(file,"jobs","other")


@app.route('/upload_emp', methods=['POST'])
def upload_emp():

    # Check if a file was uploaded
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']

    return upload_data(file,"employees","emp")


@app.route('/batch-insert-deps', methods=['POST'])
def batch_insert_deps():
    # Check if the request has a valid JSON payload
    if not request.is_json:
        return 'Invalid request payload', 400

    try:
        data = request.get_json()
        return insert_batch(data,"departments","other")

    except Exception as e:
        return str(e), 500


@app.route('/batch-insert-jobs', methods=['POST'])
def batch_insert_jobs():
    # Check if the request has a valid JSON payload
    if not request.is_json:
        return 'Invalid request payload', 400

    try:
        data = request.get_json()
        return insert_batch(data,"jobs","other")

    except Exception as e:
        return str(e), 500


@app.route('/batch-insert-emp', methods=['POST'])
def batch_insert_emp():
    # Check if the request has a valid JSON payload
    if not request.is_json:
        return 'Invalid request payload', 400

    try:
        data = request.get_json()
        return insert_batch(data,"employees","emp")

    except Exception as e:
        return str(e), 500


@app.route('/')
def hello():
    return "Hello World!"



if __name__ == '__main__':
    app.run()
