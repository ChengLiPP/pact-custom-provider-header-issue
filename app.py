from flask import Flask, request, Response
app = Flask(__name__)

@app.route('/endpoint', methods = ['GET'])
def hello_world():
    print(request.headers)
    return Response(status=200)