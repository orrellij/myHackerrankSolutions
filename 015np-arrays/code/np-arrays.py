import numpy

def arrays(arr):
    my_array = numpy.array(arr, float) #this creates an array from the list created in input

arr = input().strip().split(' ')
result = arrays(arr)
print(result)