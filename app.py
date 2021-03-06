# -*- coding: utf-8 -*-
#
#

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/something')
def something():
    return render_template('something.html')


@app.route('/something-else', methods=['GET', 'POST'])
def something_else():
    return render_template('index.html')
    # if request.method == 'POST':
    #    # do_something()
    # else:
    #    # do_something_else()


if __name__ == '__main__':
    app.debug = False  # Use true for local development
    app.run()
