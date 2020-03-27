from pathlib import Path
import docker, glob

client = docker.from_env()

def get_docker_files():
    dockerfile = []
    directory = "/docker"
    
    for path in Path(directory).rglob('Dockerfile'):
        s = str(path).rsplit('/', 1)[0]+"/docker-compose.yml"
        dockerfileOnly = True
        for file in glob.glob(s):
            dockerfileOnly = False
        
        if dockerfileOnly == True:
            dockerfile.append(path)
            
    return dockerfile


def get_docker_compose_files():
    compose_yml = []
    directory = "/docker"

    for path in Path(directory).rglob('docker-compose.yml'):
        compose_yml.append(path)

    return compose_yml


def get_docker_containers():
    containers = client.containers.list()
    return containers


def get_docker_running_containers():
    print("test")