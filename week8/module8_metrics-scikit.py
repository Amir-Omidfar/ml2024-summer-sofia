import sys 
import os
#sys.path.append("/Users/ApplePro/Desktop/projects/ml2024-summer-sofia")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from week7.module7_knn_regr_scikit import Module7


import numpy as np
from sklearn.metrics import (
    precision_score,
    recall_score
)


class Module8(Module7):
    '''
    Class for getting the inputs and running precision and recall analysis
    '''
    def __init__(self) -> None:
        super().__init__()
        self.precision = None
        self.recall = None
        self.ground_truth_lables = []
        self.predictions_lables = []
        self.user_input_list = []
        
    def get_user_input_list(self):
        for count in range(int(self.N)):
            x,y = input(f"Enter your {str(count+1)}{self.find_suffix(str(count+1))} point coordinates:\n").split()
            self.user_input_list.append([int(x),int(y)])
        print(f"your numbers are: {self.user_input_list}")

    def sort_lables(self):
        self.ground_truth_lables = [x[0] for x in self.user_input_list[:]]
        self.predictions_lables = [y[1] for y in self.user_input_list[:]]
        print(f"Ground truth lables = {self.ground_truth_lables}")
        print(f"Predictions lables = {self.predictions_lables}")
        return
    
    def find_precision(self):
        self.precision = precision_score(self.ground_truth_lables,self.predictions_lables)
        return self.precision
    
    def find_recall(self):
        self.recall = recall_score(self.ground_truth_lables,self.predictions_lables)
        return self.recall
    
    def show_results(self):
        if (not self.recall) or (not self.precision):
            print("Calculate the scores first!")
            return
        print(f"Precison = {self.precision}")
        print(f"Recall = {self.recall}")
        return
    

mod8_program_class = Module8()

def run_program():
    '''
    Main Program
    '''
    mod8_program_class.get_user_input_size()
    mod8_program_class.get_user_input_list()
    mod8_program_class.sort_lables()
    mod8_program_class.find_precision()
    mod8_program_class.find_recall()
    mod8_program_class.show_results()

def run_analysis():
    '''
    For debugging and tesging purposes
    '''
    mod8_program_class.N = 5
    mod8_program_class.ground_truth_lables = [0,1,0,0,1,0,1,0,0,1]
    mod8_program_class.predictions_lables = [1,1,1,1,1,0,0,0,1,1]                   
    #mod8_program_class.sort_lables()
    mod8_program_class.find_precision()
    mod8_program_class.find_recall()
    mod8_program_class.show_results()

if __name__ == "__main__":
    run_program()
    #run_analysis()
    