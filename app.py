from flask import Flask, render_template, request
import json
app = Flask("SE2018")


@app.route('/')
def index():
    with open("people.json") as people:
        text = people.read();
    names = json.loads(text);
    print names
    return render_template('index.html', names=names.keys())

@app.route('/profile/<int:user_id>')
def test(user_id):
    # TODO: Change user id to an actual name
    return render_template('profile.html', name=str(user_id))

@app.route('/data')
def data(data):
    print data

@app.errorhandler(404)
def error_404(error):
    return render_template('error_404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
