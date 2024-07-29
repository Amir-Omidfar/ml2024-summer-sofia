"""
1. Create your account on https://github.com (if you still do not have it)
2. Create the public repository with the name "ml2024-summer-sofia"
3. Create a very simple python program:
The program asks the user for input N (positive integer) and reads it
Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, 
or the index (from 1 to N) of this X if the user inputed it before.
Hint: use input() function
4. Name this program "module4.py" and upload to the above mentioned repo.
5. Provide the link to your repo as the answer to this assignment.
******
I have made some additional assumptions:
a. N<=10
b. user always input integres and proper values
c. values input are not repeatative

"""

def find_suffix(num):
    num_suffix = {
    "1":"st",
    "2":"nd",
    "3":"rd"}
    if num in num_suffix:
        return num_suffix[num]
    return "th"

def module_4_program():
    user_input_size = input("Enter input N (positive integer):\n")
    user_input_list = []
    for count in range(int(user_input_size)):
        user_input_list.append(int(input(f"Enter your {str(count+1)}{find_suffix(str(count+1))} number:\n")))
    print(f"your numbers are: {user_input_list}")
    X = int(input("Enter input X:\n"))
    if X in user_input_list:
        ans = user_input_list.index(X)
        return ans+1
    return -1


if __name__ == '__main__':
    res = module_4_program()
    print(f"Result: {res}")
    


