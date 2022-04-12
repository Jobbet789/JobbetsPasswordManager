from cryptography.fernet import Fernet
import os, json


class read_file:
    def __init__(self, name, config):
        # self.key = key
        self.name = name
        self.config = config

    def import_file(self, file): # import a file, and return the content
        with open(file) as f:
            return f.read()

    def decrypt_variable(self, var): # decrypt something encrypted, using a key
        return Fernet(self.key).decrypt(bytes(var, 
                            encoding="utf8")).decode("utf8")

    def decrypt_import_file(self, name): # combine the two functions above
        return self.decrypt_variable(self.import_file(name))

    def change_config(self): # change the config file
        config = open(self.config, 'r')

    def create_def_config(self):
        def_dict = {"passwordFile": "passwords", "key": "NULL", "access": "access", "attempts": 3} # default settings

        with open(self.config, 'w') as config: # create a new file and dump the default settings into it
            json.dump(def_dict, config)

        config.close() # close the new file

    
    def check_first_time(self, file): # check if there is a config file
        try: # try to check the file size
            os.stat(file) 
            return False
        except FileNotFoundError: # if there is no file, its the firt time starting
            return True