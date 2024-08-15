#errors and exceptions

class myexc(Exception):
    def __init__(self, message = "text"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"My exception: {self.message}"
    
class ValueTooHighError(Exception):
    pass

a = 5

#assert(a < 0), 'x is not negative'

if a > 1: 
    raise ValueTooHighError("too high")

try:
    c = a / 1
    dd = a + 6
except ZeroDivisionError as e: 
    print(e)
except TypeError as e:
    print(e)
else:
    print("All good") # runs if no exceptions
finally: 
    print("cleaning up") # runs always