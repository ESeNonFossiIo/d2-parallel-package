def str_to_bool(string):
    if string == 'True':
         return True
    elif string == 'False':
         return False
    else:
         raise ValueError # evil ValueError that doesn't tell you what the wrong value was