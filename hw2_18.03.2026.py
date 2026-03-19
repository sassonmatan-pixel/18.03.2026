"""
🔐 Question 1 – Safe Code
You are given a secret code:

[77, 12, 43, 100, 51]

Goal: the user must enter the numbers exactly in the correct sequence

Rules:

Go through the secret code in order
Each time, the user enters one number
If the number is correct → move to the next number
If the user makes even ONE mistake → reset progress and start again from the beginning
The loop only ends when the full sequence is entered correctly
Example:

4, 10, 77, 12, 43, 77

Explanation:

4 → wrong
10 → wrong
77 → correct (start)
12 → correct
43 → correct
77 → wrong → reset to start
Hint:

Use an index variable to track your position in the code
Reset the index to 0 when there is a mistake
"""
def secret_safe_code() -> None:
    """
    This function is used to safely enter the numbers exactly in the correct sequence
    :return: None
    """
    secret_code: list = [77, 12, 43, 100, 51]
    index: int = 0
    while True:
        if index != len(secret_code):
            try:
                user_choice: int = int(input("enter the number of scrat code: "))
            except ValueError:
                user_choice: int = int(input("ValueError try again only number: "))
            if user_choice == secret_code[index]:
                index = index + 1
                print("correct")
                continue
            else:
                print("wrong \nreset to start")
                index = 0
                continue
        else:
            print("good work")
            break

if __name__ == '__main__':
    secret_safe_code()