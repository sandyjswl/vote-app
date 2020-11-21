from flask import Flask,request, jsonify
import redis
import os
import json
import operator
import sys
import ctypes
app = Flask(__name__)


candidates = redis.Redis(
host=os.getenv("REDIS_HOST"),
port=int(os.getenv("REDIS_PORT")),
charset="utf-8", decode_responses=True)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/check')
def check():
    return 'Checking In if everything is fine'


@app.route('/vote/<candidate>')
def vote(candidate):
    current_candidate = candidates.get(candidate.upper())
    if current_candidate is not None:
        candidates.set(candidate.upper(), int(candidates.get(candidate.upper())) + 1 )
        return jsonify(success=True)
    return jsonify(success=False)

@app.route('/register', methods = ['POST'])
def register():
    try:
        data =request.get_json()
        candidates.set(data['name'].upper(),0)
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/candidates', methods = ['GET'])
def get_candidates():
    keys = candidates.keys('*')
    return jsonify(keys)

@app.route('/winner', methods = ['GET'])
def get_winner():
    candidates_dict = {}
    keys = candidates.keys('*')
    for key in keys:
        val = candidates.get(key)
        candidates_dict[key] = int(val)
    try:
        print(candidates_dict)
        return jsonify(max(candidates_dict, key=candidates_dict.get))
       
    except:
        return jsonify(success=False)

@app.route('/crash', methods = ['GET'])
def crash_app():
    os._exit(0)

@app.route('/version', methods = ['GET'])
def get_version():
    version = os.getenv("VERSION")
    if version is not None:
        return jsonify(version)
    return jsonify(success=False)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')