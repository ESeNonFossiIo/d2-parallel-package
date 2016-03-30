def str_to_bool(string):
  """
    Convert a string in a bolean
  """
  if string == 'True':
       return True
  elif string == 'False':
       return False
  else:
       raise ValueError