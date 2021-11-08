from .dir import Dir

class Filesystem:
    def __init__(self, name: str = "default") -> None:
        self.name = name
        self.dirs = []

    def create_dir(self, name: str) -> None:
        checked_dirs = filter(lambda el: el.name == name, self.dirs)

        if next(checked_dirs, None):
            print(f"Directory with such name \"{name}\" already exists")
            return 

        created_dir = Dir(name)
        self.dirs.append(created_dir)

    def remove_dir(self, name: str) -> None:
        self.dirs = list(filter(lambda el: el.name != name, self.dirs))
        
    def cat_file(self, path: str, delimetr: str = "/") -> None:
        path_elements = path.split(delimetr)
        dirs = path_elements[:-1]
        file = path_elements[-1]

        target_dir = self.dirs

        for dir in dirs:
            target_dir = next(filter(
                lambda el: el.name == dir, 
                target_dir
            ), None)

            if not target_dir:
                print(f"Invalid path")
                return 

        target_file = next(filter(
            lambda el: el.name == file, 
            target_dir.files
        ), None)

        print(target_file.content)