import time

def log(func):
    def wrapper():
        print("Performing step-1 functionality......")
        print("Performing step-2 functionality......")
        func()
        print("Performed your custom function")

    return wrapper

@log
def run():
    print("Doing custom function")

run()