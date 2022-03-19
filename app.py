from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/create', methods=['POST'])
def say_name2():
    first = request.form['first_name']
    last = request.form['last_name']
    gender = request.form['gender']

    print(first)
    print(last)
    print(gender)
    return jsonify(first_name=first)


if __name__ == '__main__':
    app.debug = True
    app.run()
