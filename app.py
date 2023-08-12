from flask import Flask, render_template, request, redirect
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

@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method== "POST":
        # print('post')
        # print(request.form['title'])
        title=request.form['title']
        descr=request.form['descr']
        todo=Todo(title=title, descr=descr)  # this is a todo ka instance
        db.session.add(todo)
        db.session.commit()

    # for jinja template
    allTodo = Todo.query.all()
    # passed a variable alltodo
    return render_template('index.html',allTodo=allTodo)

@app.route('/show')
def products():
    allTodo = Todo.query.all()
    print(allTodo)

@app.route('/update/<int:sno>',methods=['GET','POST'])
def update(sno):
    if request.method=="POST":
        title=request.form['title']
        descr=request.form['descr']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title=title
        todo.descr=descr
        db.session.add(todo)
        db.session.commit()
        return redirect('/')

    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html',todo=todo)
    print(todo)

    # print(allTodo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")
    # print(allTodo)

@app.route('/about')
def about():
    return 'Ankush Tiwari\nemail: ankushtiwari@gmail.com'

if __name__ == '__main__':
    app.run(debug=True, port=8000)
