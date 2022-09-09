from flask import Flask, request, send_file
import json
import os.path

# creating a Flask app
app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def home():
    if request.method == 'GET':
        data = "hello world"
        response = app.response_class(response=json.dumps(data),
                                      status=200,
                                      mimetype='application/json')

        # status = 200
        return response


@app.route('/tmp/ok', methods=['GET'])
def file_ok():
    if (request.method == 'GET'):

        file_exists = os.path.exists('test.txt')
        print(file_exists)
        data ='OK'

        if not file_exists:
            response = app.response_class(status=503,
                                          mimetype='application/json')
        else:
            response = app.response_class(response=json.dumps(data), status=200,
                                          mimetype='application/json')
    return response

@app.route('/img')
def get_image():
    filename = 'logo.png'
    app.logger.info('Processing default request')
    return send_file(filename, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)
