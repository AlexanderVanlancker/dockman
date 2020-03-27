from flask import Flask, render_template
from colorama import Fore, Back, Style
import os
from classes.container import Container 
import functions.docker_manager as manager

app = Flask(__name__)
containers = []

@app.route('/')
def index():
    for container in containers:
        print(container.name)
        print(container.ctype)
    return render_template('index.html')

def init():
    for path in manager.get_docker_files():
        name = (str(path).rsplit('/', 1)[0]).rsplit('/', 1)[1]
        containers.append(Container(name,"dockerfile"))
    for path in manager.get_docker_compose_files():
        name = (str(path).rsplit('/', 1)[0]).rsplit('/', 1)[1]
        containers.append(Container(name,"composefile"))
    
    #manager.get_docker_containers()
    print(Fore.GREEN + ' * Initialized containers'+Style.RESET_ALL)

init()

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)

#FLASK_APP=app.py FLASK_ENV=development flask run