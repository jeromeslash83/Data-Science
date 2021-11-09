import numpy as np
from numpy.core.fromnumeric import var

def calculate(list):
  try:
  #Make the list into an NumPy Array
    list = np.array(list)

  #Reshape the Array into a 3D Array
    new_ar = list.reshape(3,3)

  #Get the mean
    mean_column = np.mean(new_ar, axis = 0).tolist()
    mean_row = np.mean(new_ar, axis =1).tolist()
    flat = np.mean(list)

  #Get the variance
    variance_column = np.var(new_ar, axis=0).tolist()
    variance_row = np.var(new_ar, axis=1).tolist()
    flat_var = np.var(list)

  #Get the Standard Deviation
    std_dev_col= np.std(new_ar, axis = 0).tolist()
    std_dev_row= np.std(new_ar, axis = 1).tolist()
    std_flat = np.std(list)

  #Get Maximum , Minumum and Sum
    max_col = np.max(new_ar, axis=0).tolist()
    max_row = np.max(new_ar,axis = 1).tolist()
    max_flat = np.max(list)

    min_col = np.min(new_ar, axis=0).tolist()
    min_row = np.min(new_ar,axis = 1).tolist()
    min_flat = np.min(list)

    sum_col = np.sum(new_ar, axis=0).tolist()
    sum_row = np.sum(new_ar,axis = 1).tolist()
    sum_flat = np.sum(list)

  # Create a Dictionary and Join it all together
    answer = dict()
    answer['mean'] = [mean_column, mean_row, flat]
    answer['variance'] = [variance_column, variance_row, flat_var]
    answer['standard deviation'] = [std_dev_col, std_dev_row, std_flat]
    answer['max'] = [max_col, max_row, max_flat]
    answer['min'] = [min_col, min_row, min_flat]
    answer['sum'] = [sum_col, sum_row, sum_flat]

    return answer
  except ValueError:
     print("List must contain nine numbers.")
  


print(calculate([0,1,2,3,4,5,7]))
