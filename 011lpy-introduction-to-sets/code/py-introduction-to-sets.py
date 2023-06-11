def average(array):
    uniqueHts = set(array)
    # here I turn the list of heights into a unique one using set()
    
    numOfDistHts = len(uniqueHts)
    # the above line obtains the number of distinct heights in the set
    # using len() allows me to obtain this data.
    
    avg = sum(uniqueHts,0) / numOfDistHts
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)