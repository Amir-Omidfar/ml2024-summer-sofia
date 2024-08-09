class Module5:
    def __init__(self) -> None:
        self.N = 0
        self.user_input_list = []
        self.x = 0

    def get_user_input_size(self):
        self.N = int(input("Enter input N (positive integer):\n"))
    
    def find_suffix(self, num):
        num_suffix = {
        "1":"st",
        "2":"nd",
        "3":"rd"}
        if num in num_suffix:
            return num_suffix[num]
        return "th"
    
    def get_user_input_list(self):
        for count in range(int(self.N)):
            self.user_input_list.append(int(input(f"Enter your {str(count+1)}{self.find_suffix(str(count+1))} number:\n")))
        print(f"your numbers are: {self.user_input_list}")
    
    def get_user_x_input(self):
        self.x = int(input("Enter input X:\n"))
        ans = -1
        if self.x in self.user_input_list:
            ans = self.user_input_list.index(self.x)
        print(f"The answer is {ans}")
        return ans
    
