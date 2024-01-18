if __name__ == "__main__":
    def decotitle(f):
        def ret(*args):
            print("Now this function is executed " + str(f))
            f(*args)

        return ret


    # Option 1:
    # def square(num):
    #     print(num * num)
    # square = decotitle(square)
    # square(5)

    # Option 2: With Decorator
    @decotitle
    def square(num):
        print(num * num)


    square(5)
