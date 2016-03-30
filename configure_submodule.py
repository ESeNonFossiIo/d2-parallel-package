#!/usr/bin/env python

from ConfigParser import *
from _libs._utilities.text import *
from _libs._utilities.bash_cmd import *

bash=BashCMD()

general = ConfigParser()
general.read("_conf/configuration.cfg")
general_secs=general.sections()

package = ConfigParser()
package.read("_conf/packages.cfg")
package_secs=package.sections()

base_dir = general.get("default", "base_dir")

for sec in package_secs:
  print_title(sec)
  name = package.get(sec, "name")
  url = package.get(sec, "url")
  # bash.mkdir(base_dir+name)
  bash.add_submodule(url, name, base_dir)