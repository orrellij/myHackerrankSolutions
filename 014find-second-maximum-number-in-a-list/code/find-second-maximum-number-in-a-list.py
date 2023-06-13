# this was the code stub provided by hackerrank
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # first I turn the inputted numbers that were made into a list
    # into a set so it has no repeating numbers. This makes my work
    # easier
    no_repeats = set(arr)
    
    # Next I turn that set back into a list so I can use list operations.
    # I sort the list in increasing order then delete the rightmost entry.
    new_list = list(no_repeats)
    ordered = sorted(new_list)
    del ordered[-1]
    print(ordered[-1])
           
    