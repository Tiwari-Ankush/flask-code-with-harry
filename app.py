from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
    # return 'Hello, Ankush!'

# @app.route()

@app.route('/about')
def about():
    return 'Ankush Tiwari\nemail: ankushtiwari@gmail.com'

if __name__ == '__main__':
    app.run(debug=True, port=8000)
