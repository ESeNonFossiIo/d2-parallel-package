from shutil import copy2, copytree
import sys
import subprocess
from git import *
import os
import errno
from _libs._utilities.text import *

def overwite_line(string, max_char=40, str_init="\t---> ", new_line=False):
  """
    Format the output to have an ouput made by single line.
    
    Parameters
    ----------
    string: str
      Text to print
    max_char : Optional[int]
      Maximum number of characters / Lenght of the line.
      (Default value = 40)
    str_init : Optional[str]
      Initial string printed at the begin of every line.
      (Default value = "\\t---> ")
    new_line : Optional[bool]
      New line at the end of the string.
      (Default value = False)

  """
  sys.stdout.write(str_init+max_char*" "+"\r",)
  if not new_line:
    sys.stdout.write(str_init+string[0:max_char].rstrip()+"\r",)
  else:
    sys.stdout.write(str_init+string[0:max_char].rstrip()+"\n",)
  sys.stdout.flush()

# GENERAL:
################################################################################
def run(cmd, split=True, executable=True, use_shell=False, show_output=True):
  script=""
  if executable:
    if split:
      script = cmd.split()
    else:
      script = cmd
  else:
    with open(cmd, 'rb') as file:
      script = file.read()

  process = subprocess.Popen(script, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=use_shell)

  while True:
    nextline = process.stdout.readline()
    if nextline == '' and process.poll() != None:
        break
    if show_output:
      overwite_line(nextline)
  if show_output:
    overwite_line("DONE", new_line=True)

  if (process.returncode == 0):
    return process.communicate()
  else:
    print "--> ERROR!"

def get_output(cmd):
  return subprocess.check_output(cmd.split(" "));

# Congigure:
##############################################################################
def autoconf():
  cmd = which("autoconf")
  return run(cmd)

def configure(prefix="", flags=""):
  cmd="./configure"
  if prefix!="":
    cmd+=" --prefix="+prefix+" "
  if flags!="":
    cmd+=flags
  return run(cmd)
  
# Make:
################################################################################
def make(np=1, args=""):
  cmd = which("make")
  if np != 1 :
    cmd+=" -j"+str(np)
  if args!="":
    cmd+=" "+args
  return run(cmd)
  
def make_install(np=1):
  return make(np, "install")

def make_clean(np=1):
  return make(np, "clean")

# CMake:
################################################################################
def cmake(cmake_list_path="", install_path="", flags=""):
  cmd = which("cmake")
  args = " "
  if install_path != "" :
    args+="-DCMAKE_INSTALL_PREFIX:PATH="+install_path+" "
  if cmake_list_path != "" :
    args+=cmake_list_path+" "
  if flags != "" :
    args+=""
  cmd+=" "+args
  return run(cmd)

# Bash:
################################################################################
def pwd():
  return os.getcwd()

def cp(src, dst):
  return copy2(src, dst)

def cp_dir(src, dst):
  try:
    return copytree(src, dst)
  except:
    return "ERROR"
  
def cd(path="."):
  try:
    return os.chdir(path)
  except os.error, e:
    if e.errno != errno.EEXIST:
      raise

def mkdir(directory, status=False):
  try:
    os.mkdir(directory)
  except os.error, e:
    if e.errno != errno.EEXIST:
      raise
    else:
      if status:
        return "File exists: " + directory
        
def export_var(var, val=""):
  try:
    os.environ[var] = val
    return True
  except:
    return False
  
def unset(var_list):
  try:
    var_list=var.split(" ")
    for var in var_list:
      os.unsetenv(var)
    return True
  except:
    return False

def source(source_file):
  cmd="source "+str(source_file)+"; env"
  out = run(cmd, use_shell=True, split=False, output=False)
  print out[0]

def add_to_path(new_path):
  if new_path!="" and os.environ["PATH"].find(new_path)==-1 :
    os.environ["PATH"] = new_path + os.pathsep + os.environ["PATH"]

def list_dirs(path):
  return os.listdir(path)

def which(cmd):
  return get_output("which "+cmd)

# GIT:
################################################################################
    
def get_abbrev():
  return get_output("git show-ref --hash --abbrev HEAD")
    
  # # GIT:
  # ##############################################################################
  # def update_submodule(self):
  #   cmd = "git"
  #   return self.execute(cmd, "submodule update --init --recursive")
  # 
  # 
  #       
  # def add_submodule(self, url_path, name, base_dir):
  #   main_repo = Repo(path="./")
  #   #      # get a config writer to change configuration
  #   #      
  #   # assert not main_repo.bare
  #   sm = main_repo.create_submodule( name, base_dir+name, url=url_path)
  #   assert sm.exists() and sm.module_exists()
  #   print main_repo.submodule
  #   print main_repo.untracked_files
  #   main_repo.index.commit("Added submodule " + name)
  #   # sm.remove(module=True, configuration=False) 
  #   # self.main_repo.submodule_update(recursive=False)
  #   #     # .gitmodules was written and added to the index, which is now being committed
  #   #     cloned_repo.index.commit("Added submodule")
  #   #     assert sm.exists() and sm.module_exists()             # this submodule is defintely available
  #   # submodule = repos.submodule(base_dir_name)
  #   # # submodule.binsha = submodule.module().head.commit.binsha
  #   # repos.index.add([submodule])
  #   # submodule.module().git.checkout('wanted commit')
  #   # for line in sh.git("submodule", "add", url, base_dir_name, "--force", _iter=True) :#, _out=process_output, )
  #   # submodule_add = sh.git("submodule", "add",url, base_dir+name, "--name "+name, _out=print_out, _err=print_err)
  #   # submodule_add.wait()
  
