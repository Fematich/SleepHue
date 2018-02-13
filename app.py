#!/usr/bin/python3
from flask import Flask
from hue import sleepsequence
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(1)
app = Flask(__name__)

@app.route('/')
def home():
    return 'Active'

@app.route('/sleepsequence')
def run_sleepsequence():
    executor.submit(sleepsequence)
    return 'Sleepsequence started'


if __name__ == '__main__':
    app.run(port=80)