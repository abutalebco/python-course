from abc import ABC, abstractmethod

# File System 

class FileSystemItem(ABC):
    @abstractmethod
    def show(self, indent=0) -> str:
        pass

class File(FileSystemItem):
    def __init__(self, name):
        self.name = name

    def show(self, indent=0):
        return " " * indent + f"File: {self.name}"
    
class Folder(FileSystemItem):
    def __init__(self, name):
        self.name = name
        self.items: list[FileSystemItem] = []

    def add(self, item: FileSystemItem):
        self.items.append(item)

    def show(self, indent=0):
        result = " " * indent + f"Folder: {self.name}\n"
        for item in self.items:
            result += item.show(indent + 2) + "\n"
        return result 

    
file1 = File("a.txt")
file2 = File("b.txt")
file3 = File("c.txt")

root = Folder("root")
sub_folder = Folder("sub")

sub_folder.add(file2)
sub_folder.add(file3)

root.add(file1)
root.add(sub_folder)

print(root.show())