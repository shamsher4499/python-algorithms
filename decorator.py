def first_function(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        return data.lower()
    return wrapper


@first_function
def second_function():
    return 'PYTHON IS A GOOD LANGUAGE'

print(second_function())