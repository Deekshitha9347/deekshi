def outer():
    print("outer function started")
    def inner():
        print("inner function")
    def login():
        print("login function")
    inner()
    login()
outer()        