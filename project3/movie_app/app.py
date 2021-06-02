from flask import Flask
from flask import render_template
from jsonProcess import getMovie

app = Flask(__name__)


# /로 들어오면 welcom index page 리턴해줌
@app.route('/')
def index():
    return 'Welcome movie recommendation'

#/movie/<page>로 들어오면 movie.html 리턴해주고 list에 정보가 담겨 넘어감
@app.route('/movie/<page>')
def movie(page):
    print(page)
    list = getMovie(page)
    return render_template('movie.html', list=list)


if __name__=="__main__":
    app.run(host='0.0.0.0', port=9000, debug=True)