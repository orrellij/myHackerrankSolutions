#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    subString1 = 'Hello ' + first
    subString2 = ' ' + last
    subString3 = '! You just delved into python.'
    outputString = subString1
    print(subString1 + subString2 + subString3) 


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)