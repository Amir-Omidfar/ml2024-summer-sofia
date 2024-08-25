import sys 
sys.path.append("/Users/ApplePro/Desktop/projects/ml2024-summer-sofia")
from week6.module6_knn_regr import Module6
import numpy as np

class Module7(Module6):
    def __init__(self) -> None:
        super().__init__()
        self.traininig_var = 0
    
    def find_training_var(self):
        x_var,y_var = np.var(self.user_input_list,axis=1)
        return (x_var,y_var)


mod7_program_class = Module7()

def run_program():
    mod7_program_class.get_user_input_size()
    mod7_program_class.get_user_k_size()
    mod7_program_class.get_user_input_list()
    mod7_program_class.get_user_x_input()
    res=mod7_program_class.find_k_points()
    print(f"Result: {res}")
    x_var,y_var = mod7_program_class.find_training_var()
    print(f"Training Labels Variance: {y_var}")
    return res