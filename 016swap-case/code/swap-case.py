def swap_case(s):
    return s.swapcase() # this is the final code. Using the swapcase fuction from the String class
                        # it was easy to swap the lowers to uppers and vice versa.

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)