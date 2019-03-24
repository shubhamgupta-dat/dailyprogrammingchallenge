allowed_set = [str(x) for x in range(1,27)]
key_map:dict = dict(zip(allowed_set,[chr(ord('a') + x) for x in range(26)]))


def get_code(input_string,output_set:set=set(),i=0):
        # Converting input to string
        input_string = str(input_string)

        #Taking substring so length check can be done
        substring = input_string[:2]
        if len(substring)<1:
            """
            If substring length is less than 1, then no character is remaining
            """
            return output_set
        elif len(substring)==1:
            """
            Recursive Iteration to identify last mapped output
            """
            mapped:str = key_map.get(input_string[:1])
            if mapped is None:
                return output_set
            output_set = {mapped}
            return output_set
        else:
            """
            Check for both 1st Character in substring and last character as well
            """

            # For 1 length
            mapped_1: str = key_map.get(input_string[:1])
            if mapped_1 is None:
                return output_set
            output_set_1 = get_code(input_string[1:], output_set, i + 1)
            output_set_1 = {mapped_1+output for output in output_set_1}

            # For 2 length
            if input_string[:2] in key_map.keys():
                mapped_2: str = key_map.get(input_string[:2])
                if mapped_2 is None:
                    return output_set_1
                output_set_2 = get_code(input_string[2:], output_set, i + 1)
                if len(output_set_2) > 0:
                    output_set_2:set = {mapped_2 + output for output in output_set_2}
                else:
                    output_set_2 = {mapped_2}

                output_set = output_set_1.union(output_set_2)
                return output_set
            else:
                return output_set_1


if __name__ == '__main__':
    input_string = 1341
    print(get_code(input_string))

    input_string = 111
    print(get_code(input_string))

    print(get_code(0))