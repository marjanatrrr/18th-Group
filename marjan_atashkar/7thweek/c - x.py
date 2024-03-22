def print_letters_step_two(start_letter, end_letter):
    start_letter = start_letter.lower()
    end_letter = end_letter.lower()

    if not ('a' <= start_letter <= 'z' and 'a' <= end_letter <= 'z'):
        print("Please enter valid letters from a to z.")
        return

    start_ord = ord(start_letter)
    end_ord = ord(end_letter)
    for i in range(start_ord, end_ord + 1, 2):
        print(chr(i))


print_letters_step_two('c', 'x')
