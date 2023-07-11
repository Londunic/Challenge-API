from flask import Flask, request
from upload import upload_data

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
def batch_insert():
    # Check if the request has a valid JSON payload
    if not request.is_json:
        return 'Invalid request payload', 400

    try:
        data = request.get_json()
        ##

    except Exception as e:
        return str(e), 500

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
