from .filesystem import Filesystem

DELIMETR = "/"

def create_app():
    fs = mount_fs()

    while True:
        try:
            command = input(f"{fs.name}> ")
            terminal(fs, command)
        except KeyboardInterrupt:
            print("End of session")
        except Exception as exc:
            print(exc)


def mount_fs() -> Filesystem:
    return Filesystem()


def terminal(filesystem: Filesystem, command: str) -> None:
    commands = ["mkdir", "rmdir", "cat"]
    splitted_command = command.split()

    if splitted_command[0] not in commands:
        print("Inconsistent using of command")
        return 
    
    dir_name = splitted_command[1]

    if (splitted_command[0] in ["mkdir", "rmdir"] 
        and len(dir_name.split(DELIMETR)) != 1):
        print("Invalid dir name")
        return
    
    if "mkdir" in splitted_command:
        filesystem.create_dir(dir_name)
    elif "rmdir" in splitted_command:
        filesystem.remove_dir(dir_name)
    elif "cat" in splitted_command:
        filesystem.cat_file(dir_name)
    