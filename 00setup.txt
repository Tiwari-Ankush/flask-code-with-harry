

Install Python:
Download and install Python from the official website: https://www.python.org/downloads/

Install Visual Studio Code:
Download and install VS Code from: https://code.visualstudio.com/

Open Terminal:
Open your system's terminal or command prompt.

Create Project Directory:
Choose a directory where you want to create your Flask project and navigate to it using the terminal:

bash
Copy code
cd path/to/your/project/directory
Create Virtual Environment:
Create and activate a virtual environment (recommended for isolating dependencies):

On macOS/Linux:

bash
Copy code
python3 -m venv venv
source venv/bin/activate

On Windows:
bash
Copy code
pip install virtualenv
python -m venv venv
.\venv\Scripts\activate
Install Flask:
Install Flask within the activated virtual environment:

bash
Copy code
pip install Flask
Create Flask Application:
Create a Python file named app.py in your project directory and add the following code:

python
Copy code
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, Ankush!'
if __name__ == '__main__':
    app.run(debug=True)

Install VS Code Python Extension:
Open VS Code, go to the Extensions tab on the left sidebar, search for "Python" by Microsoft, and install it.

Configure Debugger (Optional):
Create a .vscode directory in your project directory if it doesn't exist. Inside it, create a launch.json file and add the following configuration:

json
Copy code
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/app.py",
            "cwd": "${workspaceFolder}",
            "env": {
                "FLASK_APP": "app.py",
                "FLASK_ENV": "development"
            },
            "args": ["run"]
        }
    ]
}

Run Flask App:
In the terminal (with your virtual environment activated), run your Flask app:

bash
Copy code
flask run
Access the App:
Open your web browser and visit http://127.0.0.1:5000/ to see your Flask app in action.
