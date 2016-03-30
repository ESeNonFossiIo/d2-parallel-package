from _libs._modules.modules import *
              
class DealIIInstaller(ModuleInstaller):                
  def __init__(self):
    super(DealIIInstaller, self).__init__("dealii")
  
  def compile(self):
    super(DealIIInstaller, self).compile()
    build="build_"+self.hash_pkg
    mkdir(build)
    cd(build)
    cmake(  cmake_list_path = "..", 
            install_path = self.opt_inst_dir )

  def install(self):
    super(DealIIInstaller, self).install()
    make_install(np=self.np)

  def export(self):
    super(DealIIInstaller, self).export()
    export_var(self.name.upper()+"_DIR", self.opt_inst_dir)
    export = open(self.export_filename, 'a')
    export.write("export " + self.name.upper() + "_DIR=" + self.opt_inst_dir)
    export.close()