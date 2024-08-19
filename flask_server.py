from flask import Flask, request, jsonify
import numpy as np
# from main import main  
from subprocess import run
from flask_cors import CORS, cross_origin
import time
from od_matrix import read_od
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS']= 'Content-Type'


@app.route('/')
@cross_origin()
def od_matrix():
    # Get the array from the request
    #  main(['station1_in.mp4', 'station2_in.mp4','station3_in.mp4', 'station6_in.mp4', 'station1_out.mp4', 'station2_out.mp4','station3_out.mp4', 'station4_out.mp4'])
    #  od_matrix_6 = [[1,0,0,0,0,0],[0,2,0,0,0,0],[0,0,3,0,0,0], [0,0,0,1,0,0], [0,0,0,0,1,0],[0,0,0,0,0,0]]
    #  od_matrix_5 = [[0,0,0,0,0,0],[1,0,0,0,0,0],[2,0,0,0,0,0], [0,2,2,0,0,0],[0,0,0,0,0,0],[0,0,0,0,1,0]]
    #  od_matrix_4 = [[0,0,0,0],[1,0,0,0],[2,0,0,0], [0,2,2,0]]
     response  = jsonify(read_od())
     response.headers.add("Access-Control-Allow-Origin", "*")
     time.sleep(10)
     return response
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



