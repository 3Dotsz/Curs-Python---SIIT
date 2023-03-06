my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
#print(my_list)



print(my_list[::1]) #my_list asc unsorted

print(my_list[::-1]) #my_list desc unsorted

my_list.sort()
print(my_list) #my_list asc sorted
print(my_list[::-1]) #my_list desc sorted

my_sliced_list = my_list[1::2]
print(my_sliced_list) #even numbers from my_list

my_sliced_list = my_list[::2]
print(my_sliced_list) #odd numbers from my_list

my_sliced_list = my_list[2::3]
print(my_sliced_list) #numbers multiple of 3 from my_list