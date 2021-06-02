
import functools
class ClassDecorator:
    def __init__(self, func):
        functools.wraps(self, func)
        self.func = func
        self.n_count = 0
    def __call__(self, *args, **kwargs):
        self.n_count += 1
        print(f"You have called {self.func.__name__} {self.n_count} time(s).")
        return self.func(*args, **kwargs)
@ClassDecorator
def hello():
    print("Hello World")
hello()
hello()