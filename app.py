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
        container.log_container_info()
    return render_template('index.html', containers=containers)

def init():
    for path in manager.get_docker_files():
        name = (str(path).rsplit('/', 1)[0]).rsplit('/', 1)[1]
        container = Container(name=name,type="dockerfile",path=str(path))
        containers.append(container)

    for path in manager.get_docker_compose_files():
        name = (str(path).rsplit('/', 1)[0]).rsplit('/', 1)[1]
        container = Container(name=name,type="composefile",path=str(path))
        containers.append(container)

    for container in manager.get_docker_containers():
        name = container.name
        containerid = container.id
        container = Container(name=name,type="dockerpulled",id=containerid)
        containers.append(container)
    
    print(Fore.GREEN + ' * Initialized containers'+Style.RESET_ALL)

init()

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)



#FLASK_APP=app.py FLASK_ENV=development TEMPLATES_AUTO_RELOAD=True flask run