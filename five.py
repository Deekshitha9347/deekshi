def outer():
    print("outer function started")
    def inner():
        print("inner function")
    def login():
        print("login function")
    return inner
inner=outer()
inner()     