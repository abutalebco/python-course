class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating new instance...")
            cls._instance = super().__new__(cls)
        else:
            print("Using exisiting instance...")
        return cls._instance
    
obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)

# logging system 

class Logger:
    _instance = None
    logs: list[str]

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, "logs"):
            self.logs = []

    def print_object(self):
        print(Logger._instance)
    
    def log(self, message: str):
        self.logs.append(message)

    def show_logs(self) -> list[str]:
        return self.logs
    

logger1 = Logger()
logger2 = Logger()

logger1.log("First Log")
logger2.log("Second Log")

print(logger1)
print(logger2)

logger1.print_object()
logger2.print_object()

print(logger1.show_logs())
print(logger1 is logger2)