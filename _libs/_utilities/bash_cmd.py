import sh as sh
import sys
import subprocess
from git import *
import os
import errno
from _libs._utilities.text import *

def print_out(line):
  print "                    OUTPUT ----> " + line,

def print_err(line):
  print "                    ERROR  ----> " + line,

def overwite_line(string, max_char=40, str_init="---> ", new_line=False):
  sys.stdout.write(str_init+max_char*" "+"\r",)
  if not new_line:
    sys.stdout.write(str_init+string[0:max_char].rstrip()+"\r",)
  else:
    sys.stdout.write(str_init+string[0:max_char].rstrip()+"\n",)
  sys.stdout.flush()

# GENERAL:
################################################################################
def run(cmd, executable="True"):
  script=""
  if executable:
    script = cmd.split()
  else:
    with open(cmd, 'rb') as file:
      script = file.read()

  process = subprocess.Popen(script, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

  # Poll process for new output until finished
  while True:
      nextline = process.stdout.readline()
      if nextline == '' and process.poll() != None:
          break
      overwite_line(nextline)
  overwite_line("DONE", new_line=True)

  exitCode = process.returncode

  print 
  if (exitCode == 0):
      return process.communicate()
  else:
      raise ProcessException(command, exitCode, output)

# Congigure:
##############################################################################
def configure(prefix="", aux_args=""):
  cmd="./configure"
  if prefix!="":
    cmd+=" --prefix="+prefix+" "
  if aux_args!="":
    cmd+=aux_args
  return run(cmd)
  
# Make:
##############################################################################
def make(np=0, install=False):
  cmd="make"
  if np != 0 :
    cmd+=" -j"+str(np)
  if install:
    cmd+=" install"
  return run(cmd)
  
def make_install(np=0):
  return make(np, install=True)

class BashCMD(object):
  
  def __init__(self):
    print " -> Initialize BashCMD"
  
  def execute(self, cmd, args=""):
    args=args.split(" ")
    process = sh.Command(cmd)
    return process(args)

  def bash(self, script=""):
    cmd="bash"
    args=" "
    if script != "" :
      args+=script+" "
    return self.execute(cmd,args)

  def pwd(self):
    return sh.pwd()

  def cd(self, path="."):
    sh.cd(path)
    return self.pwd()
  
  def set(self, var, val=""):
    try:
      os.environ[var] = val
      return True
    except:
      return False
    
  def unset(self, var_list):
    try:
      var_list=var.split(" ")
      for var in var_list:
        os.unsetenv(var)
      return True
    except:
      return False
    
  # CMAKE:
  ##############################################################################
  def cmake(self, cmake_list_path="", install_path="", flags=""):
    cmd = "cmake"
    args = " "
    if install_path != "" :
      args+="-DCMAKE_INSTALL_PREFIX:PATH="+install_path+" "
    if cmake_list_path != "" :
      args+=cmake_list_path+" "
    if flags != "" :
      args+=""
    return self.execute(cmd, args)
    
  # GIT:
  ##############################################################################
  def update_submodule(self):
    cmd = "git"
    return self.execute(cmd, "submodule update --init --recursive")

  def get_abbrev(self):
    cmd = "git"
    return self.execute(cmd, "show-ref --hash --abbrev HEAD")

        
  def add_submodule(self, url_path, name, base_dir):
    main_repo = Repo(path="./")
    #      # get a config writer to change configuration
    #      
    # assert not main_repo.bare
    sm = main_repo.create_submodule( name, base_dir+name, url=url_path)
    assert sm.exists() and sm.module_exists()
    print main_repo.submodule
    print main_repo.untracked_files
    main_repo.index.commit("Added submodule " + name)
    # sm.remove(module=True, configuration=False) 
    # self.main_repo.submodule_update(recursive=False)
    #     # .gitmodules was written and added to the index, which is now being committed
    #     cloned_repo.index.commit("Added submodule")
    #     assert sm.exists() and sm.module_exists()             # this submodule is defintely available
    # submodule = repos.submodule(base_dir_name)
    # # submodule.binsha = submodule.module().head.commit.binsha
    # repos.index.add([submodule])
    # submodule.module().git.checkout('wanted commit')
    # for line in sh.git("submodule", "add", url, base_dir_name, "--force", _iter=True) :#, _out=process_output, )
    # submodule_add = sh.git("submodule", "add",url, base_dir+name, "--name "+name, _out=print_out, _err=print_err)
    # submodule_add.wait()
  
  def mkdir(self, directory, status=False):
    try:
      os.mkdir(directory)
    except os.error, e:
      if e.errno != errno.EEXIST:
        raise
      else:
        if status:
          print_error("File exists: "+directory)