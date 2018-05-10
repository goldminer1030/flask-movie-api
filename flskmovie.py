from flask import Flask, jsonify, abort
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flskmovies:greenpeace2018@localhost/flskmovies_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Movies(db.Model):
    movie_title = db.Column(db.String(128))
    id = db.Column(db.Integer, primary_key=True)
    recommended_movie_id_0 = db.Column(db.String(128))
    recommended_movie_id_1 = db.Column(db.String(128))
    recommended_movie_id_2 = db.Column(db.String(128))
    recommended_movie_id_3 = db.Column(db.String(128))
    recommended_movie_id_4 = db.Column(db.String(128))
    recommended_movie_title_0 = db.Column(db.String(128))
    recommended_movie_title_1 = db.Column(db.String(128))
    recommended_movie_title_2 = db.Column(db.String(128))
    recommended_movie_title_3 = db.Column(db.String(128))
    recommended_movie_title_4 = db.Column(db.String(128))


class MovieSchema(ma.Schema):
    class Meta:
        model = Movies
        fields = ('movie_title', 'recommended_movie_id_0', 'recommended_movie_id_1', 'recommended_movie_id_2',
                  'recommended_movie_id_3', 'recommended_movie_id_4', 'recommended_movie_title_0',
                  'recommended_movie_title_1', 'recommended_movie_title_2', 'recommended_movie_title_2',
                  'recommended_movie_title_3', 'recommended_movie_title_4')


movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class MovieID(Resource):
    def get(self, id):
        movie = Movies.query.get(id)

        if movie:
            return movie_schema.jsonify(movie)
        else:
            abort(400)


class MovieTitle(Resource):
    def get(self, movie_title):
        movie = Movies.query.filter(Movies.movie_title.like(movie_title + '%')).first()
        if movie:
            return movie_schema.jsonify(movie)
        else:
            abort(400)


api.add_resource(HelloWorld, '/')
api.add_resource(MovieID, '/id/<id>')
api.add_resource(MovieTitle, '/title/<movie_title>')

if __name__ == '__main__':
    app.run()
