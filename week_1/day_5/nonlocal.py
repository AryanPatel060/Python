def outer():
    x = 10

    def inner():
        x += 5   # ❌ Error happens here
        print(x)

    inner()

outer()
