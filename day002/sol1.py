import operator

def multiply_except_self(X):
    """
    Multiply all values and then divide by number itself. If zero is present check the flag
    """
    multiple = 1
    zero_index = []
    for i, value in enumerate(X):
        if value != 0:
            multiple *=value
        else:
            zero_index.append(i)

    if len(zero_index)>1:
        return [0]*len(X)
    elif len(zero_index)==1:
        return_list = [0]*(zero_index[0]-1)
        return_list.append(multiple)
        return_list.extend([0]*(len(X)-(zero_index[0]+1)))
    else:
        return_list = []
        for value in X:
            return_list.append(int(multiple/value))
    return return_list

if __name__ == '__main__':
    input1 = [0,10,30,40,1]
    input2 = [0,1,0,0,2,5,6]
    input3 = [1, 2, 3, 4, 5]
    print(f"For input : {input1} the result is {multiply_except_self(input1)}")
    print(f"For input : {input2} the result is {multiply_except_self(input2)}")
    print(f"For input : {input3} the result is {multiply_except_self(input3)}")