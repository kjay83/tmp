from flask import Flask, request
from flask.json import jsonify
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

videos = {
    1:{"name":"toto1", "likes":1, "views":1000},
    10:{"name":"toto10", "likes":10, "views":10000},
    "11":{"name":"toto11", "likes":11, "views": 11000},
    12:{"name":"toto12", "likes":12, "views":12000}
    }

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name",type=str, help="Name of the video", required=True)
video_put_args.add_argument("views",type=int, help="Views of the video")
video_put_args.add_argument("likes",type=int, help="Likes of the video")


class Video(Resource):
    def get(self, video_id):
        return videos[video_id]
    
    def post(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

api.add_resource(Video,"/videos/<int:video_id>")

# names = {
#     "tim": {"age":19, "genre": "male"},
#     "timora": {"age":15, "genre": "female"},
#     "glasstale": {"age":25, "genre": "male"},
# }

# class Pple(Resource):
#     def get(self, name):
#         return names[name]

# class HelloWorld(Resource):
#     def get(self):
#         return {"data":"hello world!!"}
#     def post(self):
#         return {"data": "posted"}
#     def put(self):
#         return {"data": "put"}
#     def delete(self):
#         return {"data": "deleted"}

# class HelloWorld2(Resource):
#     def get(self,name,numbr):
#         return {"name":name, "numbr":numbr}

# api.add_resource(HelloWorld, "/hello")
# api.add_resource(HelloWorld2, "/hello2/<string:name>/<int:numbr>")
# api.add_resource(Pple, "/pple/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)

