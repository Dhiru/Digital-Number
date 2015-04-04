file_name = "data"
c1 = [5,8]  #1
c2 = [1, 4, 5, 6, 7] #2
c3 = [1,4,5,7,8] #3
c4 = [3,4,5,8] #4
c5 = [1,3,4,7,8] #5
c6 = [1,3,4,6,7,8] #6
c7 = [1,5,8] #7
c8 = [1,3,4,5,6,7,8] #8
c9 = [1,3,4,5,7,8] #9
c0 = [1,3,5,6,7,8] #0
number_index_list = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9]
number_format = [' ','_',' ','|','_','|','|','_','|']


def story1(file_name):
    found_numbers = []
    numbers = []
    line = []
    minus_index = 0
    with open(file_name) as f:
        for index, file_line in enumerate(f):  # read line by line
            if (index + 1) % 4 == 0:
                minus_index += 1
                numbers.append(zip(line[index - 2 - minus_index], line[index - 1 - minus_index], line[index - 0 - minus_index])) # combine three lines
            else:
                line.append(file_line)
    for each_number in numbers:  # loop for each lines
        found_number = []
        for each_range in range(0, 27):
            blank_list = []
            if (each_range + 1) % 3 == 0:
                # combining 3 column of 3 lines
                zip_blank_list = zip(each_number[each_range - 2], each_number[each_range - 1], each_number[each_range]) 
                blank_list = zip_blank_list[0] + zip_blank_list[1] + zip_blank_list[2]
                found_number.append(identify_number(blank_list))
        found_numbers.append(found_number)
    return found_numbers
                
def identify_number(number_list):
    '''
    function for convert number in _ and | format to decimal number
    Args:
        number_list: contains single of number in _ and | format
    Returns:
        return_number: which will return number in decimal form, if failed then return '?'
    '''
    actual_number_list = []
    return_number = ""
    for each_number in range(0, 9):
        if number_list[each_number] == number_format[each_number] and number_list[each_number] in ['_', '|']:
            actual_number_list.append(each_number)
    for each_number_index in range(0, 10):
        if list(actual_number_list) == number_index_list[each_number_index]:
            return_number = each_number_index
    return return_number if return_number else "?"

def story2():
    output = story1(file_name)      # call story1
    for each_number in output:
        if '?' in each_number:
            print ''.join(map(str, each_number)), "Error"
        else :
            if check_sum(each_number):
                print ''.join(map(str, each_number)), "Valid number"
            else :
                print ''.join(map(str, each_number)), "Invalid number"

def check_sum(number_list):
    '''
    check whether number is valid or according to check sum.
    Args:
        number_list: contains single of number decimal format
    Returns:
        return_number: boolean True or False
    '''
    number_list.reverse()
    sum_number = 0
    for each_number in range(1, 10):
        sum_number += number_list[each_number - 1] * each_number
    return sum_number % 11 == 0

def story3():
    output = story1(file_name)      # call story1
    with open("output",'w') as f:
        for each_number in output:
            if '?' in each_number:
                f.writelines(''.join(map(str, each_number)) + ' ILL\n')
            else :
                if check_sum(each_number):
                    f.writelines(''.join(map(str, each_number)) + '\n')
                else :
                    f.writelines(''.join(map(str, each_number)) + ' ERR\n')
                    
    
def print_number(number):
    '''
        print a number according to pass number input
    '''
    a = [' ','_',' ','|','_','|','|','_','|']
    i=0
    b=[]
    space = ' '
    for index, each in enumerate(a):
        if index in number:
            b.append(each.ljust(1))
        else:
            b.append(space.ljust(1))
        i += 1
        if i == 3:
            i = 0
            print "".join(b)
            b = []
      
