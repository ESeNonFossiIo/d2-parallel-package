from _libs._modules.modules import *
              
class SlepcInstaller(ModuleInstaller):
  def __init__(self):
    super(SlepcInstaller, self).__init__("slepc")
  
  def compile(self):
    super(SlepcInstaller, self).compile()
    configure(  prefix=self.opt_inst_dir)

  def install(self):
    super(SlepcInstaller, self).install()
    make(np=self.np)
    make("SLEPC_DIR="+pwd()+" ")
    make("SLEPC_DIR="+pwd()+" install")

  def export(self):
    super(SlepcInstaller, self).export()
    export_var(self.name.upper()+"_DIR", self.opt_inst_dir)
    
    export = open(self.export_filename, 'a')
    export.write("export " + self.name.upper() + "_DIR=" + self.opt_inst_dir)
    export.close()