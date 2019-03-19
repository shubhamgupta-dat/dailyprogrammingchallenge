def multiply_except_self(X):
    left_multiplications = [1]
    right_multiplications = [1]
    for i in range(1, len(X)):
        left_multiplications.append(left_multiplications[i-1]*X[i-1])
        right_multiplications.append(right_multiplications[i-1]*X[-i])
    return_list = []
    for i in range(len(X)):
        return_list.append(left_multiplications[i]*right_multiplications[-1-i])
    return return_list

if __name__ == '__main__':
    input1 = [0, 10, 30, 40, 1]
    input2 = [0, 1, 0, 0, 2, 5, 6]
    input3 = [1, 2, 3, 4, 5]
    print(f"For input : {input1} the result is {multiply_except_self(input1)}")
    print(f"For input : {input2} the result is {multiply_except_self(input2)}")
    print(f"For input : {input3} the result is {multiply_except_self(input3)}")
