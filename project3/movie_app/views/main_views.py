from flask import Blueprint
from flask import Blueprint, render_template
from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')


# /로 들어오면 welcom index page 리턴해줌
@app.route('/')
def index():
    return 'Welcome index page'

#/movie/<page>로 들어오면 movie.html 리턴해주고 list에 정보가 담겨 넘어감
@app.route('/movie/<page>')
def movie(page):
    print(page)
    list = getMovie(page)
    return render_template('movie.html', list=list)

