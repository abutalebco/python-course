def mydecorator(function):
    
    def wrapper(*args, **kwargs):
        print("==== START ====")
        return_value = function(*args, **kwargs)
        print("==== END ====")
        return return_value

    return wrapper

@mydecorator
def hello(person):
    print(f"hello, {person}")
    return f"hello, {person}"

print(hello("Mohamed"))