def log_var(var_name, var, lenght=30):
  string=" "
  string+=var_name
  string+=" : "
  string+=(lenght-len(var_name))*"."
  string+=" "
  string+=var
  return string