user_choice = int(input('Please enter your choice: '))
for i in range(1,user_choice+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
for k in range(user_choice,1,-1):
    for l in range(1,k):
        print(l,end=' ')
    print()


x = " "
for i in range(1,user_choice+1,2):
    print((" " * (user_choice - i)),end= '')
    for j in range(1,i+1):
        print("*",end=' ')
    print()

for i in range(1, user_choice + 1, 2):
    print((" " * (user_choice - i)) +"* " * i + (" " * (user_choice - i)))
