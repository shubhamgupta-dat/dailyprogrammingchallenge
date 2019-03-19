def is_sum_present(input_list,target):
    for i, value1 in enumerate(input_list):
        for value2 in input_list[i+1:]:
            if (value1 + value2) == target:
                return True
    return False

if __name__ == '__main__':
    input_numbers = [10, 15, 3, 7]
    target = 17
    print(f"The presence of {target} in list {input_numbers} is {is_sum_present(input_numbers,target)}")