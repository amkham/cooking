from flask import Flask, render_template
from DB import query

app = Flask(__name__)


@app.route('/')
def hello_world():
    result = query.select_all()
    structure = query.select_structure()

    return render_template('index.html', result=result, str=structure)


if __name__ == '__main__':
    app.run()
