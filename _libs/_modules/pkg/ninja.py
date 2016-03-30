from _libs._modules.modules import *

class NinjaInstaller(ModuleInstaller):
  def __init__(self):
    super(NinjaInstaller,self).__init__("ninja")
  
  def compile(self):
    super(NinjaInstaller,self).compile()
    run("./configure.py --bootstrap")

  def install(self):
    super(NinjaInstaller,self).install()
    cp_dir(".", self.opt_inst_dir)

  def export(self):
    super(NinjaInstaller,self).export()
    add_to_path(self.opt_inst_dir)
    export = open(self.export_filename, 'a')
    export.write("add_to_path " + self.opt_inst_dir + " \n")
    export.close()