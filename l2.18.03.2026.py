'''
1
input number from the user --  88949
print the number in reverse -- 94988
print the biggest digit -- 9
print how many times the biggest digit appears? -- 2
print the min digit -- 4
print the sum of digits -- 38
print the avg of digits -- 8+8+9+4+9 / 5
'''
from itertools import count
from random import choice

user_number = input("enter the number: ")
print(user_number)
print(user_number[::-1])
print(max(user_number))
print(user_number.count(max(user_number)))
print(min(user_number))
_sum: int = int(0)
_count = 0
for num in user_number:
    _sum += int(num)
    _count += 1
print(_sum)
print(_sum/_count)

def sorted_fun(list) -> bool:
    return list == sorted(list)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sorted_fun(list1))

"""2
write a function that gets a list of numbers and returns if the list is sorted or not

3
write a function that gets a list of numbers (with duplication), n-th biggest and returns it
i.e. [88, 100, 90, 95, 95, 97, 97, 99, 97, 99] , 4 --> will return 95 (because it is the 4-th biggest after 100, 99, 97, 95)
"""

def func(list2: list, user_choice1) -> int:
    list2.sort(reverse=True)
    while True:
        if user_choice1 != 0:
            list3 = list1.pop(0)
            while list3 in list1:
                list1.remove(list3)
            else:
                user_choice1 -=1
        else:
            return list[0]


list2 = [88, 100, 90, 95, 95, 97, 97, 99, 97, 99]
user_choice1 = int(input("enter the number: "))
count = func(list2, user_choice1)
print(count)