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
    OMPI_DIR=os.environ["OMPI_DIR"]
    export_var("MPI_HOME",OMPI_DIR)
    export_var("CC",which("mpicc"))
    export_var("CXX",which("mpic++"))
    export_var("F77",which("mpif77"))
    export_var("FC",which("mpif77"))
    export_var("F90",which("mpif90"))
    export = open(self.export_filename, 'a')
    export.write("add_to_path " + self.opt_inst_dir + "/bin" + " \n")
    export.write("export " + self.name.upper() + "_DIR=" + self.opt_inst_dir)
    export.write("MPI_HOME="+OMPI_DIR)
    export.write("CC="+which("mpicc"))
    export.write("CXX="+which("mpic++"))
    export.write("F77="+which("mpif77"))
    export.write("FC="+which("mpif77"))
    export.write("F90="+which("mpif90"))
    export.close()