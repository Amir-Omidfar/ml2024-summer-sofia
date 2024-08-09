import sys 
sys.path.append("/Users/ApplePro/Desktop/projects/ml2024-summer-sofia")
from week5.module5_oop import *
import numpy as np
class Module6(Module5):
    def __init__(self) -> None:
        super().__init__()
        self.k = 0
        self.user_input_list = None
    def get_user_k_size(self):
        self.k = int(input("Enter input k (positive integer):\n"))
        self.user_input_list = np.array([[(0,0)]*self.N])

    def get_user_input_list(self):
        for count in range(int(self.N)):
            x,y = input(f"Enter your {str(count+1)}{self.find_suffix(str(count+1))} point coordinates:\n").split()
            self.user_input_list[0][count] = (float(x),float(y))
        print(f"your numbers are: {self.user_input_list}")
    
    def get_user_x_input(self):
        x,y = input("for X input enter X and Y coordiantes:\n").split()
        self.x = np.array([float(x),float(y)])
        if self.k > self.N:
            raise Exception("K can't be greater than N")
        
    def find_distance_to_x(self,given_point):
        return np.linalg.norm(np.array([self.x,given_point]))
    
    def find_k_points(self):
        print("Run k-nn")
        self.points_list = []
        self.k_points = np.array([(0)*self.k])
        points = self.user_input_list[0]
        for point in points:
            distance = self.find_distance_to_x(point)
            self.points_list.append([distance,point])
        self.points_list.sort()
        y_sum=0
        for i in range(self.k):
            y_sum+=self.points_list[i][1][1]
        return y_sum/self.k

    """
    1. Calculate the distance from point x to all the points
    2. Keep finding the point with min distance to x k times
    3. calculate the k-nn regression for x using the points

    """
    


mod6_program_class = Module6()
def run_program():
    mod6_program_class.get_user_input_size()
    mod6_program_class.get_user_k_size()
    mod6_program_class.get_user_input_list()
    mod6_program_class.get_user_x_input()
    res=mod6_program_class.find_k_points()

    return res

if __name__ =="__main__":
    run_program()