def title_decorator(function):
    def wrapper():
        result = function()
        make_title = result.title()
        print(make_title + " -Data is converted to title case")
        return make_title
    return wrapper

def split_string_decorator(function):
    def wrapper():
        result = function()
        splitted_string = result.split()
        print(str(splitted_string) + " -Then Data is splitted")
        return splitted_string
    return wrapper

@split_string_decorator
@title_decorator
def say_hi():
    return 'hello there'

result = say_hi()
print(result)
