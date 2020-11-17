import numpy as np

def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  np_array = np.array(list).reshape(3, 3)
  results = {}
  results['mean'] = [np_array.mean(axis = 0).tolist(),
                     np_array.mean(axis = 1).tolist(),
                     np_array.mean()]
  
  results['variance'] = [np_array.var(axis = 0).tolist(),
                     np_array.var(axis = 1).tolist(),
                     np_array.var()]
  
  results['standard deviation'] = [np_array.std(axis = 0).tolist(),
                     np_array.std(axis = 1).tolist(),
                     np_array.std()]

  results['max'] = [np_array.max(axis = 0).tolist(),
                     np_array.max(axis = 1).tolist(),
                     np_array.max()]

  results['min'] = [np_array.min(axis = 0).tolist(),
                     np_array.min(axis = 1).tolist(),
                     np_array.min()]
                    
  results['sum'] = [np_array.sum(axis = 0).tolist(),
                     np_array.sum(axis = 1).tolist(),
                     np_array.sum()]


  return results