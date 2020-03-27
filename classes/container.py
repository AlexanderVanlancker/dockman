class Container:
    def __init__(self, name, type, id="null", envariables=[], path="", status=False):
        self.name = name
        self.id = id
        self.type = type
        self.envariables  = envariables
        self.path = path
        self.status = status
    
    def run(self):
        #only in case of Dockerfile

        #client = docker.from_env()
        #client.container.run(self.containerid)
        return "test"
    
    def build(self):
        #commands differ for Dockerfile and docker-compose

        #os.exec("docker-compose up",cwd=path)
        return "test"
        
    def logs(self):
        #client = docker.from_env()
        #return client.container.(self.containerid).logs()
        return "test"

    def log_container_info(self):
        print('container name = ' + self.name)
        print('container type = ' + self.type)
        print('container id = ' + self.id)
        for var in self.envariables:
            print('container env = ' + var)
        print('container path = ' + self.path)
        print('container status = ' + str(self.status))
        print('\n')