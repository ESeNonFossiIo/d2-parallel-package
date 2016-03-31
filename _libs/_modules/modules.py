from ConfigParser import *

from _libs._utilities.text import *
from _libs._utilities.bash_cmd import *
from _libs._utilities.log import *
from _libs._utilities.utilities import *


class ModuleInstaller(object):  
  def __init__(self, name):
    with open("_conf/configuration.cfg") as fp:
      self.general = SafeConfigParser()
      self.general.readfp(fp)
      self.root = self.general.get("default", "root")
      self.base_dir = self.general.get("default", "base_dir")
      self.opt_inst = self.general.get("default", "opt_inst")
      self.np = self.general.get("default", "np")
      self.export_filename = self.opt_inst+"export.conf"

    self.name = name
    
    if name!="module installer":
      self.package = SafeConfigParser()
      self.package.read("_conf/packages.cfg")

      self.path = self.package.get(self.name, "path")
      cd(self.path)
      self.hash_pkg = str(get_abbrev()).rstrip()

      self.opt_inst_dir = self.opt_inst+self.name+"-"+self.hash_pkg

  def __del__(self):
    cd(self.root)
  
  def compile(self):
    print " --> COMPILE"

  def install(self):
    print " --> INSTALL"

  def export(self):
    print " --> EXPORT"
            
  def print_status(self):
    print BAR
    print log_var("name",self.name)
    print log_var("base dir",self.base_dir)
    print log_var("opt dir",self.opt_inst)
    print log_var("path",self.path)
    print log_var("hash",self.hash_pkg)
    print log_var("np",self.np)
    print BAR

  def init_export_file(self):
    # TODO:
    export = open(self.export_filename, 'w+')
    export.write("\n")
    export.write("DST=`dirname $BASH_SOURCE`\n")
    export.write("echo $BASH_SOURCE\n")
    export.write("if [ -z \"$DST\" ]; then \n")
    export.write("    echo Need a destination directory\n")
    export.write("    return 1\n")
    export.write("fi\n")
    export.write("\n")
    export.write("#echo \"Assuming everything is on $DST\" \n")
    export.write("\n")
    export.write("function add_to_path \n")
    export.write("{\n")
    export.write("    if [ -d \"$1\" ] && [[ ! \"$PATH\" =~ (^|:)\"$1\"(:|$) ]]; then\n")
    export.write("        export PATH=$1:$PATH\n")
    export.write("        #echo Added $1 to PATH\n")
    export.write("    fi;\n")
    export.write("}\n")
    export.write("\n")
    export.write("# Export the above function\n")
    export.write("export -f add_to_path\n")
    export.write("\n")
    export.close()
