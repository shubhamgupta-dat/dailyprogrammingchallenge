def get_highest_missing_positive(array):
    set_values = set(array)

    for i in range(1,len(set_values)+1):
        if i not in set_values:
            return i

    return len(set_values)+1

if __name__ == '__main__':
    input1 = [3, 4, -1, 1]
    input2 = [0, 1, 0, 0, 2, 5, 6]
    input3 = [1, 2, 3, 4, 5]
    print(f"For input : {input1} the result is {get_highest_missing_positive(input1)}")
    print(f"For input : {input2} the result is {get_highest_missing_positive(input2)}")
    print(f"For input : {input3} the result is {get_highest_missing_positive(input3)}")