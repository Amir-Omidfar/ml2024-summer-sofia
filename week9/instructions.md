1. Create a Python program:

The program asks the user for input N (positive integer) and reads it.

Then the program asks the user to provide N (x, y) pairs (one by one) and reads all of them: first: x value, then: y value for every pair one by one. X is treated as the input feature and Y is treated as the class label. X is a real number, Y is a non-negative integer.

This set of pairs constitutes the training set TrainS = {(x, y)\_i}, i = 1..N.

Then the program asks the user for input M (positive integer) and reads it.

Then the program asks the user to provide M (x, y) pairs (one by one) and reads all of them: first: x value, then: y value for every pair one by one. X is treated as the input feature and Y is treated as the class label. X is a real number, Y is a non-negative integer.

This set of pairs constitutes the test set TestS = {(x, y)\_i}, i = 1..M.

In the end, the program outputs: the best k for the kNN Classification method and the corresponding test accuracy. kNN Classifier should be trained on pairs from TrainS, tested on x values from TestS and compared with y values from TestS.

The basic functionality of data processing (data initialization, data insertion), should be done using Numpy library while the computation (ML) part should be done using Scikit-learn library as much as possible (note: you can combine with what you've done from the previous tasks).

Note: you can try the following range of k: 1 <= k <= 10.
