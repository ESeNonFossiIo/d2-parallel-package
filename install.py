#!/usr/bin/env python

from ConfigParser import *
from _libs._utilities.text import *
from _libs._utilities.bash_cmd import *
from _libs._utilities.log import *

bash=BashCMD()

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

name = package.get("ompi", "name")
path = package.get("ompi", "path")
hash_pkg = str(bash.get_abbrev()).rstrip()
print  BAR
print log_var("name", name)
print log_var("path", path)
print log_var("hash", hash_pkg)
print log_var("build", path+"/build-"+hash_pkg)
print  BAR

# bash.mkdir(path+"/build-"+hash_pkg)
bash.cd(path)
bash.unset("CXX CC F77 FC")

install_path=opt_inst+name+"-"+hash_pkg
# run("./autogen.sh")
# configure(prefix=install_path)
make(np=3)

# bash.cmake("..",install_path)

# for sec in package_secs:
#   print_title(sec)"
#   name = package.get(sec, "name")"
#   url = package.get(sec, "url")
#   # bash.mkdir(base_dir+name)
#   bash.add_submodule(url, name, base_dir)

