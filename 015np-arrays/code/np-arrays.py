import numpy

def arrays(arr):
    my_array = numpy.array(arr, float) #this creates an array from the list created in input
    sorted_array = numpy.flip(my_array) #uses the flip function in numpy to obtain the array we want
    return sorted_array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)