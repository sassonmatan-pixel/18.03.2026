"""Question 3 – N-th Biggest Number
Write a function that gets:

A list of numbers (with duplicates)
A number n
The function should return the n-th biggest unique number in the list

Example:

[88, 100, 90, 95, 95, 97, 97, 99, 97, 99] , n = 4

Result:

95

Explanation:

Unique sorted values (descending):

100, 99, 97, 95, 90, 88

The 4th biggest number is 95

Rules:

Ignore duplicates when counting
Assume is valid (you don’t need to handle errors)n
Good luck"""

def check_what_is_big(list1, n) -> int:
    list2 = list1.copy()
    list2 = set(list2)
    list2 = list(list2)
    list2.sort(reverse=True)
    return list2[n]


n = 4
list1 = [88, 100, 90, 95, 95, 97, 97, 99, 97, 99]
print(check_what_is_big(list1, n - 1))

# דרך שניה
def check_what_is_big(list1, n) -> int:
    list2 = []
    for num in list1:
        if num not in list2:
            list2.append(num)
    list2.sort(reverse=True)
    return list2[n]


n = 4
list1 = [88, 100, 90, 95, 95, 97, 97, 99, 97, 99]
print(check_what_is_big(list1, n - 1))
