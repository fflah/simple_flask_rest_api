from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

# inisiasi object flask
app = Flask(__name__)

# inisiasi object flask_resstfull
api = Api(app)

# inisiasi object flask corst
CORS(app)

identitas = {}

# membua class resource
class Res(Resource):
    def get(self):
        response = {"mesg": "ini adalah response pertama"}
        return response
    
    def post(self):
        print(request.form)
        nama = request.form["nama"]
        umur = request.form["umur"]
        identitas['nama'] = nama
        identitas['umur'] = umur
        response = {
            "msg": "success",
            "data": identitas 
            }
        return response


# setup resourcenya
api.add_resource(Res, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=8000)

