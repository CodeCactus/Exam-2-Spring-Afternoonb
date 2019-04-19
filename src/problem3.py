"""
Exam 3, problem 1.

Authors: CSSE Faculty, Dr. Brackin, and 
         PUT_YOUR_NAME_HERE.  
         April, 2019.

"""  #me: 1. PUT YOUR NAME IN THE ABOVE LINE. (-1 if you do not)
####################################################################
# getting there: 2. Commit and push this file- NOW.
#          You will be penalized severely if you do NOT follow instructions
# 1 Points
####################################################################

import time


def main():

    """
    Prompts the user for a string using the phrase "Input String 1, Input String 2 etc.
    until the sentinel value of '-1' is encountered.
    Input strings are placed into a sequence until the
    sentinel value is encountered.
    After the sentinel value is encountered, the following information
    should be printed:
    The sequence that was input,
    The length of each string in the sequence,
    The number of times that the letter 'e' occurs in each sequences,
    Find the letter 'o' and replace it with the numeral '6',
    Descriptive labels should be provided for each answer that is printed.
    You may assume that there is at least one element in the sequence.

No input validation is required.  Nothing else should be printed.

Here is a sample run, where the user input is to the right
of the colons:
    Please input string 1:  'Hello'
    Please input string 2:  'my name'
    Please input string 3: 'is Patsy.'
    Please input string 4:  'I wish'
    Please input string 5:  'you Good Luck'
    Please input string 6:  -1
    The sequence that you input is:
    [Hello, my name, is Patsy, I wish, you Good Luck]
    The length of string 1 is: 5
    The length of string 2 is: 7
    The length of string 3 is: 9
    The length of string 4 is: 6
    The length of string 5 is 13
    The letter 'e' occurs 2 times.
    The new sequence is:
    [Hell6, my name, is Patsy, I wish, y6u G66d Luck]
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #          A test has been written for you (above).
    #
    #14 Points
    # -------------------------------------------------------------------------
    sequence = []
    y = 1
    while True:

        print('Input string',y, end='')
        x = str(input(':'))
        if x != '-1':
            sequence = sequence + [x]
            y = y+1
        else:
            break
    total_e = 0
    old_sequence = ''
    new_sequence = ''
    for k in range(len(sequence)):
        for j in range(len(sequence[k])):
            old_sequence =old_sequence + str(sequence[k][j])
            if sequence[k][j] == 'e':
                total_e = total_e + 1
            if sequence[k][j] == 'o':
                new_sequence = new_sequence + str(6)
            else:
                new_sequence = new_sequence + str(sequence[k][j])
        new_sequence = new_sequence + ' '
        old_sequence = old_sequence + ' '
    print("The sequence that you input is:")
    print('[',old_sequence,']')
    for k in range(len(sequence)):
        print('The length of string', k+1, 'is: ',len(sequence[k]))

    print("The letter 'e' occurs ",total_e,"times")
    print('The new sequence is: ')
    print(new_sequence)

    # -------------------------------------------------------------------------
    # TODO: 4. Be sure to commit and push your work.
    #
    # -------------------------------------------------------------------------


main()

