from threading import Thread
from random import uniform
from time import sleep

from .consts import DEVIATION_FROM_POINT, BASE_LINE_VOLTAGE_POS, LINE_VOLTAGE_DELTA
from .filesystem import Filesystem

DELIMETR = "/"

def create_app():
    fs = mount_fs()

    terminal_proc = Thread(target=run_fs, args=(fs,))
    voltage_updater_proc = Thread(target=update_line_voltage, args=(fs,))
    
    terminal_proc.start()
    voltage_updater_proc.start()
    
    terminal_proc.join()
    voltage_updater_proc.join()
    


def run_fs(filesystem: Filesystem):
    while True:
        try:
            command = input(f"{filesystem.name}> ")
            terminal(filesystem, command)
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


def update_line_voltage(filesystem: Filesystem):
    while True:
        for dir in filesystem.dirs:
            for file in dir.files:
                if file.name.startswith("line"):
                    file.content = uniform(
                        BASE_LINE_VOLTAGE_POS - LINE_VOLTAGE_DELTA, 
                        BASE_LINE_VOLTAGE_POS + LINE_VOLTAGE_DELTA
                    ) * DEVIATION_FROM_POINT
                    
        sleep(1)