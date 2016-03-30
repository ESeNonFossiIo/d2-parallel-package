from _libs._modules.modules import *

class SundialsInstaller(ModuleInstaller):
  cmake_flags = " -DLAPACK_ENABLE:BOOL=ON\
                  -DMPI_ENABLE:BOOL=ON\
                  -DPTHREAD_ENABLE:BOOL=ON"
                
  def __init__(self):
    super(SundialsInstaller, self).__init__("sundials")
  
  def compile(self):
    super(SundialsInstaller, self).compile()
    build="build_"+self.hash_pkg
    mkdir(build)
    cd(build)
    cmake(  cmake_list_path = "..", 
            install_path = self.opt_inst_dir, 
            flags = self.cmake_flags )

  def install(self):
    super(SundialsInstaller, self).install()
    make_install(np=self.np)

  def export(self):
    super(SundialsInstaller, self).export()
    export_var(self.name.upper()+"_DIR", self.opt_inst_dir)
    export = open(self.export_filename, 'a')
    export.write("export " + self.name.upper() + "_DIR=" + self.opt_inst_dir)
    export.close()