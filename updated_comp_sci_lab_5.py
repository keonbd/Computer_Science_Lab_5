#Comp sci lab 5
# Katie O'Connor
# Comp Sci Lab 5
# 9/28/2022
def get_school(sample):
    while len(sample) == 10:
        if sample[5] == '1':
            return 'School of Computing and Engineering SCE'
        if sample[5] == '2':
            return 'School of Law'
        if sample[5] == '3':
            return 'School of Arts and Sciences'
        else:
            return 'Invalid School'


def get_grade(sample):
    while len(sample) == 10:
        if sample[6] == '1':
            return 'Freshman'
        if sample[6] == '2':
            return 'Sophmore'
        if sample[6] == '3':
            return 'Junior'
        if sample[6] == '4':
            return 'Senior'
        else:
            return 'Invalid Grade'


def get_check_digit(sample):
    count = 0
    for i, v in enumerate(sample[0:5]):
        for x in range(0,5):
            count = (i+1)*x
        continue
    for d, e in enumerate(sample[5:10]):
        for y in range(1,5):
            count += (d+1)*y
        count = count % 10
    return count


def verify_check_digit(sample):
    get_check_digit(sample)
    get_grade(sample)
    get_school(sample)
    if len(sample) != 10:
        return False, "The length of the ID must be 10"
    for i, v in enumerate(sample[0:4]):
        if not v.isalpha():
             return False, "The first 5 characters must be A - Z"
    while get_school(sample) == 'Invalid School':
        return False, "The sixth character must be 1 2 or 3"
    while get_grade(sample) == 'Invalid Grade':
        return False, "The seventh character must be 1, 2, 3, or 4"
    while sample[7].isdigit() == False:
        return False, "The eigth character needs to be a digit"
    while sample[8].isdigit() == False:
        return False, "The ninth character needs to be a digit"
    while sample[9].isdigit() == False:
        return False, "The tenth character should be a digit matching the count"
    else:
        return True

def character_value(sample):
    for j in sample:
        j = ord(j)
        return j
    '''char2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
    i = 0
    for i, v in enumerate(char2[i]):
        if v in sample:
            return i'''
sample = input('Enter the Library card. Hit enter to Exit.')
while sample != ' ':
    get_check = get_check_digit(sample)
    ifit = verify_check_digit(sample)
    while ifit == True:
        if int(sample[9]) != int(get_check):
            print(False)
            print("Check digit does not match the calculated value 0")
            sample = input('Enter the Library card. Hit enter to Exit')
        else:
            print(get_school(sample))
            print(get_grade(sample))
            sample = input('Enter the Library card. Hit enter to Exit')
    else:
        print(ifit[0])
        print(ifit[1])
        sample = input('Enter the Library card. Hit Enter to Exit')

'''while sample != '':
    while booli == False:
        print(booli)
        print(statement)
        sample = input('Enter the Library card. Hit Enter to Exit')
        get_check_digit(sample)
    else:
        print(get_school(sample))
        print(get_grade(sample))
print(sample[9])
print(get_check_digit(sample'''
