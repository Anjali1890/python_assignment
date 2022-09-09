# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
import numpy as np
import json
import statistics
import math

# creating a Flask app
app = Flask(__name__)


# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods=['GET', 'POST'])
def home():
    if (request.method == 'GET'):
        data = "hello world"
        return jsonify({'data': data})


# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route('/home/<int:num>', methods=['GET'])
def disp(num):
    return jsonify({'data': num ** 2})


@app.route('/min/<int:num>', methods=['GET'])
def min(num):
    l1 = [2, 8, 9, 12, 23, 45, 56, 20, 4, 6]

    return jsonify({'Minimum values': sorted(l1)[:num]})


@app.route('/max/<int:num>', methods=['GET'])
def max(num):
    l1 = [2, 8, 9, 12, 23, 45, 56, 20, 4, 6]
    # arr = np.array([2, 8, 9, 12, 23, 45, 56, 20, 4, 6])
    return jsonify({'maximum values': sorted(l1, reverse=True)[:num]})

    # return jsonify({'Minimum values': tuple(n) for n in np.where(arr == arr.max())[0][0:num]})


@app.route('/avg', methods=['GET'])
def avg():
    l1 = [2, 8, 9, 12, 23, 45, 56, 20, 4, 6]
    # arr = np.array([2, 8, 9, 12, 23, 45, 56, 20, 4, 6])
    return jsonify({'avg :': (sum(l1) / len(l1))})


@app.route('/median', methods=['GET'])
def med():
    l1 = [2, 8, 9, 12, 23, 22, 15, 20, 4, 6]
    # arr = np.array([2, 8, 9, 12, 23, 45, 56, 20, 4, 6])
    return jsonify({'med :': statistics.median(l1)})


@app.route('/percentile/<int:num>', methods=['GET'])
def percentile(num):
    l1 = [2, 8, 9, 12, 23, 22, 15, 20, 4, 6]
    len_list = len(l1)
    return jsonify({'percentile qth value': sorted(l1)[int(math.ceil((len_list * num) / 100)) - 1]})


# arr = np.array([2, 8, 9, 12, 23, 45, 56, 20, 4, 6])


# driver function
if __name__ == '__main__':
    app.run(debug=True)
