from _libs._modules.modules import *

class OpenMPInstaller(ModuleInstaller):  
  def __init__(self):
    super(OpenMPInstaller, self).__init__("ompi")
  
  def compile(self):
    super(OpenMPInstaller, self).compile()
    run("./autogen.sh")
    configure(prefix=self.opt_inst_dir)

  def install(self):
    super(OpenMPInstaller, self).install()
    make(np=self.np)

  def export(self):
    super(OpenMPInstaller, self).export()
    add_to_path(self.opt_inst_dir + "/bin")
    export_var(self.name.upper()+"_DIR", self.opt_inst_dir)
    export = open(self.export_filename, 'a')
    export.write("add_to_path " + self.opt_inst_dir + "/bin" + " \n")
    export.write("export " + self.name.upper() + "_DIR=" + self.opt_inst_dir)
    export.close()