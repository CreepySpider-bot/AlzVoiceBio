
from flask import Flask, request, jsonify
from model import speaker_identifier
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# from interface import unauthorized
from model import speaker_identifier

@app.route('/authorize', methods=['POST'])
def authorize():
    # Assuming you receive audio data in the request

    # Perform speaker identification
    pred = speaker_identifier()

    if pred == 1:
        response = {'status': 'authorized'}
    else:
        response = {'status': 'unauthorized'}

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
    
    # ##############################################
    # from interface import unauthorized
# from model import speaker_identifier

# if __name__ == "__main__":

#     pred = speaker_identifier()

#     if pred == 1:
#         print("You are authorized!")
#     else:
#         print("Unauthorized !!")