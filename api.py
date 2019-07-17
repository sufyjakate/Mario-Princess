from flask_restful import Resource, Api
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from princess_save import PrincessPath

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Inputgame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    N = db.Column(db.Integer)
    grid = db.Column(db.String(80))

    def __init__(self, N, grid):
        self.N = N
        self.grid = grid


class game_input(ma.Schema):
    class Meta:
        fields = ("N", "grid")

g_input = game_input()

@app.route('/game', methods=['POST'])
def get_input():
    N = request.json['N']
    grid = request.json['grid']

    g_input = Inputgame(N, grid)

    db.session.add(g_input)
    db.session.commit()

    return jsonify(g_input)

@app.route('/game', methods=['GET'])
def get_output():
    N = request.json['N']
    grid = request.json['grid']

    N = int(N)
    grid = [grid.strip() for _ in range(n)]

    final = PrincessPath(N, grid)

    return jsonify(final)


if __name__ == '__main__':
    app.run(debug=True)
