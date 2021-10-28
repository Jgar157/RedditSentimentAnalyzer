from flask import Flask, render_template, url_for, redirect, request
import praw_test

app = Flask(__name__)


@app.route('/')
@app.route('/index')  # multiple routes to same page
def home():
    return render_template('index.html', x=praw_test.main('python'))


if __name__ == '__main__':
    app.run()
