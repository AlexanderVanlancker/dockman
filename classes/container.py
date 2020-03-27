class Container:
    def __init__(self, name, ctype="compose", envariables=[], path="", status=False):
        self.name = name
        #self.containerid = "test"
        self.ctype = ctype
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