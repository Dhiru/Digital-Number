from generate_number_from_file import *

input_index = 0
while input_index == 0:
    print "enter 1 for story1"
    print "enter 2 for story2"
    print "enter 3 for story3"
    print "enter 0 for exit"
    print "enter 5 for print number 0 to 9 in _ and | form"
    user_input = input()
    if user_input == 1:
        output = story1(file_name)      # call story1
        for each_number in output:
            print ''.join(map(str, each_number))
    elif user_input == 0:
        input_index = 1
        print "Bye"
    elif user_input == 5:
        for each_number in number_index_list:
            print_number(each_number)
    elif user_input == 2:
        story2()
    elif user_input == 3:
        story3()
        print "result is saved in output file, use command cat to see file"
    else:
        input_index = 1
