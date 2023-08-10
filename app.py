from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)


# DATABASE >>
class Todo(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(300), nullable=False)
    descr=db.Column(db.String(500), nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self ) -> str:
        return f"{self.sno} - {self.title}"

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
