from os.path import exists

def main():
    print("[DAY 8]")

    puzzle_input = []

    if exists("day8/input.txt"):
        f = open("day8/input.txt", "r")
    elif exists("input.txt"):
        f = open("input.txt", "r")
    else:
        return print("An Error Has Occured")
    for line in f:
        puzzle_input.append(line.strip())

    def calculate_easy_characters():
        easy_characters = 0
        for line in puzzle_input:
            output = line.split("|",1)[1].strip().split()
            for character in output:
                if len(character) in [2,3,4,7]:
                    easy_characters += 1
        return easy_characters

    def is_scrambled(string1, string2):
        return sorted(string1) == sorted(string2)

    def calculate_top_left(four, one):
        top_left = four.replace(one[0], '')
        top_left = top_left.replace(one[1], '')
        return top_left

    def calculate_output_addition():
        total_addition = 0
        for line in puzzle_input:
            input_numbers = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
            decoded_number = ''
            input = line.split("|",1)[0].strip().split()
            output = line.split("|",1)[1].strip().split()
            for input_no in input:
                if len(input_no) == 2:
                    input_numbers[1] = input_no
                elif len(input_no) == 3:
                    input_numbers[7]= input_no
                elif len(input_no) == 4:
                    input_numbers[4] = input_no
                elif len(input_no) == 7:
                    input_numbers[8] = input_no
            
            top_left = calculate_top_left(input_numbers[4], input_numbers[1])
            for input_no in input:
                if len(input_no) not in [2,3,4,7]:
                    if top_left[0] in input_no and top_left[1] in input_no:
                        if len(input_no) == 5:
                            input_numbers[5] = input_no
                        else:
                            if input_numbers[1][0] in input_no and input_numbers[1][1] in input_no:
                                input_numbers[9] = input_no
                            else:
                                input_numbers[6] = input_no
                    else:
                        if len(input_no) == 5:
                            if input_numbers[1][0] in input_no and input_numbers[1][1] in input_no:
                                input_numbers[3] = input_no
                            else:
                                input_numbers[2] = input_no
                        else: 
                            input_numbers[0] = input_no 

            for output_no in output:
                for v in range(10):
                    if is_scrambled(output_no, input_numbers[v]):
                        decoded_number += str(v)
            
            total_addition += int(decoded_number)

        return total_addition

    print("[TASK 1]: " + str(calculate_easy_characters()))

    print("[TASK 2]: " + str(calculate_output_addition()))

if __name__ == "__main__":
    main()
