def check_two_sum(input_list,target):
    set_computed = set()
    for value in input_list:
        if value in set_computed:
            return True
        else:
            set_computed.add(target-value)
    return False

if __name__ == '__main__':
    input_numbers = [10, 15, 3, 7]
    target = 17
    print(f"The presence of {target} in list {input_numbers} is {check_two_sum(input_numbers,target)}")