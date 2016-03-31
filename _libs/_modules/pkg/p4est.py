from _libs._modules.modules import *
              
class P4estInstaller(ModuleInstaller):
  configure_flags= "  --enable-mpi \
                      --without-blas \
                      --disable-vtk-binary \
                      --without-lapack"
                      
  def __init__(self):
    super(P4estInstaller, self).__init__("p4est")
  
  def compile(self):
    super(P4estInstaller, self).compile()
    run("autoconf")
    run("git submodule init && git submodule update")
    run("./bootstrap")
    configure(  prefix=self.opt_inst_dir, 
                flags=self.configure_flags)

  def install(self):
    super(P4estInstaller, self).install()
    make_install(np=self.np)

  def export(self):
    super(P4estInstaller, self).export()
    export_var(self.name.upper()+"_DIR", self.opt_inst_dir)
    export = open(self.export_filename, 'a')
    export.write("export " + self.name.upper() + "_DIR=" + self.opt_inst_dir)
    export.close()