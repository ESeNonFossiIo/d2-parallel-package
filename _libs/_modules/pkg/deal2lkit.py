from _libs._modules.modules import *
              
class Deal2lkitInstaller(ModuleInstaller):                
  def __init__(self):
    super(Deal2lkitInstaller, self).__init__("deal2lkit")
  
  def compile(self):
    super(Deal2lkitInstaller, self).compile()
    build="build_"+self.hash_pkg
    mkdir(build)
    cd(build)
    cmake(  cmake_list_path = "..", 
            install_path = self.opt_inst_dir )

  def install(self):
    super(Deal2lkitInstaller, self).install()
    make_install(np=self.np)

  def export(self):
    super(Deal2lkitInstaller, self).export()
    export_var(self.name.upper()+"_DIR", self.opt_inst_dir)
    export = open(self.export_filename, 'a')
    export.write("export " + self.name.upper() + "_DIR=" + self.opt_inst_dir)
    export.close()