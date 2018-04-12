def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1
    return 0

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,19,20,58,99]


print('Please input a integar:')
item = int(input())

aDdress = binary_search(my_list, item)

if aDdress == 0:
    print('The number ' + str(item) +  ' is not in the list')
else:
    print ('The number ' + str(item) + ' is in the list, and the location is ' + str(binary_search(my_list, item)))
#print (binary_search(my_list, -1))
#print (binary_search(my_list, 21))
