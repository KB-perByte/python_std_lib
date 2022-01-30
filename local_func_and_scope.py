# day - 3
# LEGB Rule for python -
# BuiltIn <- Global <- Enclosing <- Local
# inner function is to hide section logic
# functions are first class citizen in python


def normal_function(arg1, arg2):
    print(var) #points global var

def normal_mod_function(arg1, arg2):
    global var
    var = var + "S"
    print(var) #points as local var

var = "a"
some_var = "global_var"

def normal_scope():

    print("nomal scope")
    some_var = "enclosing_scope"
    def local_scope():
        some_var = "local_val"
        print(some_var)
        print("local scope func")
    local_scope()
