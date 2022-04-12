from read_file import read_file 
from commands import Commands 

# var
file_config = "config"

def get_classes():
    read_file_class = read_file("passwords", "config")
    commands_class = Commands()

    return read_file_class, commands_class

def startup():
    read_file_class, commands = get_classes()

    if read_file_class.check_first_time(file_config):
        first_boot(read_file_class, commands)
    else:
        main(read_file_class, commands)

def main(read_file_class, commands):
    while True:
        command = input('>')
        try:
            commands.commands[command]()
        except KeyError:
            print("Sorry that is not a command..")


def first_boot(read_file_class, commands):
    read_file_class.create_def_config()

    print("Hello! Welcome to JobbetsPasswordManager!\nTry using the 'help' command to get a list of all the commands.\nYou can use 'setup' for a simple setup routine")
    main(read_file_class, commands)
       

   

if __name__ == "__main__":
    startup()