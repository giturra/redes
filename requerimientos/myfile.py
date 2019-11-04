def myargs(*args, **kwargs):
    return args

context = {'hola' : 1}

print(myargs(context))