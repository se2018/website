from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile/<int:user_id>')
def test(user_id):
    # TODO: Change user id to an actual name
    return render_template('profile.html', name=str(user_id))

@app.errorhandler(404)
def error_404(error):
    return render_template('error_404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
