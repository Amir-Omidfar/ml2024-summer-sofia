from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
import sys 
import os
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from week7.module7_knn_regr_scikit import Module7

'''
knn_pipe = Pipeline([('mms', MinMaxScaler()),('knn', KNeighborsClassifier())])
params = [{'knn__n_neighbors': [1:10],'knn__weights': ['uniform', 'distance'],'knn__leaf_size': [15, 20]}]
gs_knn = GridSearchCV(knn_pipe,
                      param_grid=params,
                      scoring='accuracy',
                      cv=5)
gs_knn.fit(X_train, y_train)
gs_knn.best_params_
gs_knn.score(X_train, y_train)
'''

class Module9(Module7):
    def __init__(self) -> None:
        super().__init__()
        self.M = 0
        self.TrainS = []
        self.TestS = []
        self.knn_pipe = Pipeline([('mms', MinMaxScaler()),
                                  ('knn', KNeighborsClassifier())])
        self.params = [{'knn__n_neighbors': [1,2,3,4,5,6,7,8,9,10],
                        'knn__weights': ['uniform', 'distance'],
                        'knn__leaf_size': [15, 20]}]
        self.gs_knn = GridSearchCV(self.knn_pipe,
                      param_grid=self.params,
                      scoring='accuracy',
                      cv=5)
        
    def get_TrainS(self):
        for count in range(int(self.N)):
            x,y = input(f"Enter your {str(count+1)}{self.find_suffix(str(count+1))} point coordinates:\n").split()
            self.TrainS.append([float(x),int(y)])
        print(f"your numbers are: {self.TrainS}")

    def get_user_input_M(self):
        self.M = int(input("Enter input M (positive integer):\n"))

    def get_TestS(self):
        for count in range(int(self.M)):
            x,y = input(f"Enter your {str(count+1)}{self.find_suffix(str(count+1))} point coordinates:\n").split()
            self.TestS.append([float(x),int(y)])
        print(f"your numbers are: {self.TestS}")
    
    def train_knn(self):
        self.TrainS_X = [[x[0]] for x in self.TrainS[:]]
        self.TrainS_Y = [[x[1]] for x in self.TrainS[:]]
        
        self.gs_knn.fit(self.TrainS_X,self.TrainS_Y)

    def test_knn(self):
        self.TestS_X = [[x[0]] for x in self.TestS[:]]
        self.TestS_Y = [[x[1]] for x in self.TestS[:]]
        
        print(self.gs_knn.best_params_)
        print(self.gs_knn.score(self.TestS_X, self.TestS_Y))


mod9_program_class = Module9()

def run_analysis():
    mod9_program_class.TrainS_X = [[4], [5], [10], [4], [3], [11], [14] , [8], [10], [12]]
    mod9_program_class.TrainS_Y = [[0], [0], [1], [0], [0], [1], [1], [0], [1], [1]]
    mod9_program_class.TestS_X = [[1],[2],[3],[6],[7],[8],[9],[13]]
    mod9_program_class.TestS_Y = [[0],[0],[0],[0],[1],[1],[1],[1]]
    mod9_program_class.train_knn()
    mod9_program_class.test_knn()
def run_program():
    '''
    Main Program
    '''
    mod9_program_class.get_user_input_size()
    mod9_program_class.get_TrainS()
    mod9_program_class.get_user_input_M()
    mod9_program_class.get_TestS()
    mod9_program_class.train_knn()
    mod9_program_class.test_knn()


if __name__ == "__main__":
    run_program()
    #run_analysis()
    
