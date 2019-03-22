def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


def cdr(cons):
    def return_last(*args):
        return args[-1]

    return cons(return_last)


def car(cons):
    def return_first(*args):
        return args[0]

    return cons(return_first)


if __name__ == '__main__':
    print(cdr(cons(4, 5)))
    print(car(cons(3, 4)))
