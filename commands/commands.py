from cryptography.fernet import Fernet

class Commands:
    def __init__(self):
        self.commands = {"gen": self.gen, "add": self.add, "get": self.get, "list": self.list_, "key-gen": self.keygen, "exit": self.exit}
    def gen(self):
        pass 
    def add(self):
        pass 
    def get(self):
        pass
    def list_(self):
        pass 
    def keygen(self):
        pass
    def listen(self):
        command = input(">")
        try:
            self.commands[command]()
        except KeyError:
            print("Sorry that is not a command...")
    def exit(self):
        pass
