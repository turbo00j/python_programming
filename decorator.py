def decorator_fun(function):
    def wish(name):
        if name=='jai':
            print("name is jai")
        else:
            fun(name)
    return wish
