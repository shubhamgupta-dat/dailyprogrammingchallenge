import operator
from functools import reduce


def mulitply_list(X):
    if len(X) <= 0:
        return 1
    return reduce(lambda a, b: a * b, X)


def multiply_except_self(X):
    return_list = []
    zero_count = 0
    for i in range(len(X)):
        if X[i] == 0:
            zero_count += 1
        if zero_count == 1:
            left_multiplication = mulitply_list(X[:i])
            right_multiplication = mulitply_list(X[i+1:])
            return_list = [0]*len(X)
            return_list[i] = left_multiplication*right_multiplication
            return return_list
        elif zero_count > 1:
            return [0] * len(X)
        left_multiplication = mulitply_list(X[:i])
        right_multiplication = mulitply_list(X[i+1:])
        return_list.append(left_multiplication * right_multiplication)

    return return_list


if __name__ == '__main__':
    input1 = [0, 10, 30, 40, 1]
    input2 = [0, 1, 0, 0, 2, 5, 6]
    input3 = [1, 2, 3, 4, 5]
    print(f"For input : {input1} the result is {multiply_except_self(input1)}")
    print(f"For input : {input2} the result is {multiply_except_self(input2)}")
    print(f"For input : {input3} the result is {multiply_except_self(input3)}")
