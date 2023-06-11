def average(array):
    uniqueHts = set(array)
    # here I turn the list of heights into a unique one using set()

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)