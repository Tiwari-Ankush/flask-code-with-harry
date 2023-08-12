# FLASK-COH

for activating venv
.\venv\Scripts\activate.ps1

for setting up database;
pip install flask-sqlalchemy


sqlalchemy-
    Flask-SQLAlchemy is an extension for the Flask web framework that simplifies the integration of SQLAlchemy, a popular Object-Relational Mapping (ORM) library, into Flask applications. SQLAlchemy provides a powerful and flexible way to interact with databases using Python code, and Flask-SQLAlchemy enhances this by providing a convenient way to use SQLAlchemy within Flask projects.

flask-sqlalchemy documentation>> https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/

https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#check-the-sqlalchemy-documentation

Key features of Flask-SQLAlchemy include:
>>>>>
Database Models: Define database tables as Python classes, and SQLAlchemy will automatically generate SQL statements to create and manipulate the tables.

Querying: Perform database queries using SQLAlchemy's query API, allowing you to use Python methods and expressions instead of raw SQL.

Sessions and Transactions: Flask-SQLAlchemy handles the lifecycle of database sessions and transactions within the context of Flask's request-response cycle. This helps manage the database connection efficiently and avoids common issues like connection leaks.

Migrations: Flask-SQLAlchemy can work in tandem with migration libraries like Alembic to help manage database schema changes over time.



    SQLALCHEMY_DATABASE_URI >>
    https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
    sqlite:////tmp/test.db


creating a database>>
   python in cmd (in currently activated virtual venv)
       >> then

    >>>from app import db
    >>>db.create_all() 
    if above two lines are not working then, use below lines>>

    >>> from app import app, db
    >>> with app.app_context():
    ...    db.create_all() 
    "it will create a database in instance directory"
    >>> exit()
    
    remember>>
        In this format, you're entering the with block using the ... continuation prompt, and you can press Enter to continue entering the code.

        Remember to replace 'app' with the actual name of your Flask application instance, and ensure that you have imported the necessary modules (app and db) correctly in your code.


next>>
sqlite viewer.>> https://inloop.github.io/sqlite-viewer/
add a database file into it >> initialyy database is empty, so we need to add a database in it
we use following like cmds.
 >>> db.session.add(admin)
 >>> db.session.addd(guest)
 >>> db.sessio.commit()

in our main app.py, there is homepage route ('/')
   in that we will add, instance >> by which we can understand and database interact..
       > first we add todo instance (todo=Todo(title="First todo",  descr="ankush tiwari")  # this is a todo ka instance)
       >then write a add instance and commit instance of that session

       run the app.py
       and add db file again into a https://inloop.github.io/sqlite-viewer/

       output looks like >> 
       


install extension call jinja2 temlpate >> 
   In Flask, Jinja2 is a popular and widely used templating engine. A templating engine is a tool that allows you to separate your HTML markup from your Python code. This separation makes your code more organized and maintainable, especially for web applications that generate dynamic content.

   Jinja2 templates in Flask serve as placeholders for dynamic data. They allow you to embed Python code within HTML templates. This is particularly useful for rendering data from your Flask application into HTML pages, generating dynamic content, and maintaining a clear separation between the presentation layer (HTML) and the application logic (Python).

jfor >> jinja for loop
variables dexlaration in jinja template>>
    In Jinja2 templates, you can write variables by enclosing them within double curly braces: {{ variable_name }}.

for getting and posting a request in app.route()
we use >> @app.route('/', methods=['GET','POST'])


Template inheritance>>
    emplate inheritance, also known as template hierarchy or template inheritance hierarchy, is a concept commonly used in web development, especially in the context of content management systems (CMS) and templating engines. It refers to the organization and relationship between different templates used to generate a website's pages


CRUD operations >>
    create,read, update, delete

for adding css and js in static way via jinja template
    css >
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css')}}">

    js >
    <script src="{{ url_for('static', filename='js/script.js') }}"></script>

for deploying on heroku
   install heroku CLI
   then pip install gunicorn
   then pip freeze > requirements.txt
  
   make Procfile for Heroku deplyment

run heroku in CLI/CMD
    if its not working then chck environment variables
run heroku login
    
then commit all the changes

next we will create a project by CLI
   heroku create todo-app
   you need add a payment method

   push code to heroku github
    >> git push heroku master
 and finally our app is deployed.