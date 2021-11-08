from flask import Flask,request, jsonify
import os
app = Flask(__name__)


candidates = {}

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/health')
def check():
    return 'Application is Up'


@app.route('/vote/<candidate>')
def vote(candidate):
    if candidate.upper() in candidates:
        candidates[candidate.upper()] = candidates[candidate.upper()]  + 1
        return jsonify(success=True)
    return jsonify(success=False)

@app.route('/register')
def register():
    try:
        candidates[request.args.get('name').upper()] = 0
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/candidates', methods = ['GET'])
def get_candidates():
    keys = candidates.keys()
    return jsonify({"response":list(keys)})

@app.route('/winner', methods = ['GET'])
def get_winner():
    candidates_dict = {}
    keys = candidates.keys()
    for key in keys:
        val = candidates[key]
        candidates_dict[key] = int(val)
    try:
        print(candidates_dict)
        return jsonify(max(candidates_dict, key=candidates_dict.get))
       
    except:
        return jsonify(success=False)

@app.route('/crash', methods = ['GET'])
def crash_app():
    os._exit(0)

# @app.route('/version', methods = ['GET'])
# def get_version():
#     version = os.getenv("VERSION")
#     if version is not None:
#         return jsonify(version)
#     return jsonify(success=False)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')