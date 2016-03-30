#!/usr/bin/env python

from ConfigParser import *
from _libs._utilities.text import *
from _libs._utilities.bash_cmd import *
from _libs._utilities.log import *
from _libs._utilities.utilities import *


general = ConfigParser()
general.read("_conf/configuration.cfg")
general_secs=general.sections()

package = ConfigParser()
package.read("_conf/packages.cfg")
package_secs=package.sections()

package_inst = ConfigParser()
package_inst.read("_conf/packages_inst.cfg")
package_inst_secs=package.sections()

base_dir = general.get("default", "base_dir")
opt_inst = general.get("default", "opt_inst")
np = general.get("default", "np")


print BAR
print log_var("base dir package", base_dir)
print log_var("opt install path", opt_inst)
print log_var("number of process", np)
print BAR

# Ompi:
################################################################################

unset("CXX CC F77 FC")

package_list = ["ompi" ]
for pkg in package_list:
  
  name         = package.get(pkg, "name")
  path         = package.get(pkg, "path")

  cd(path)
  print "--->"+pwd()
  
  do_autogen   = str_to_bool(package_inst.get(pkg, "autogen"))
  do_configure = str_to_bool(package_inst.get(pkg, "configure"))
  do_cmake     = str_to_bool(package_inst.get(pkg, "cmake"))
  do_make_inst = str_to_bool(package_inst.get(pkg, "make_inst"))
  hash_pkg     = str(get_abbrev()).rstrip()

  print BAR
  print bar
  print log_var("name", name)
  print log_var("path", path)
  print log_var("hash", hash_pkg)
  print log_var("build", path+"/build-"+hash_pkg)
  print log_var("autogen", str(do_autogen))
  print log_var("configure", str(do_configure))
  print log_var("make_inst", str(do_make_inst))
  print log_var("cmake", str(do_cmake))
  print bar

  # Define variables:
  install_path=opt_inst+name+"-"+hash_pkg

  build=name+"-"+hash_pkg
  
  install_path=opt_inst+build
  
  if do_autogen:
    print_title("autogen")
    run("./autogen.sh")
    
  if do_configure:
    print_title("configure")
    configure(prefix=install_path)

  if cmake:
    print_title("cmake")
    make_dir(build)
    cd(build)
    cmake("..",install_path)
    make_install(np)

  if make_inst:
    print_title("make install")
    make_install(np)

  print BAR