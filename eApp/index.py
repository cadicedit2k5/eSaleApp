from flask import render_template, request

from eApp import app, dao

@app.route('/')
def index():
    return render_template('index.html', categories=dao.get_categories(), products=dao.get_products())


if __name__ == '__main__':
    app.run(debug=True)
