from _libs._modules.modules import *
              
class PetscInstaller(ModuleInstaller):
  def __init__(self):
    super(PetscInstaller, self).__init__("petsc")
    self.configure_flags= " --with-make-np="+self.np+" \
                            --with-debugging=0 \
                            --with-mpi-dir="+os.environ["OMPI_DIR"]+" \
                            --with-sundials-dir="+os.environ["SUNDIALS_DIR"]+" \
                            --with-shared-libraries \
                            --with-external-packages-dir=./petsc-external \
                            --download-parmetis \
                            --download-metis \
                            --download-hypre \
                            --download-mumps \
                            --download-scalapack \
                            --download-superlu \
                            --download-superlu_dist \
                            --download-hdf5"
  
  def compile(self):
    super(PetscInstaller, self).compile()
    unset("PETSC_DIR PETSC_ARCH CC CXX F77 F90 FC")
    configure(  prefix=self.opt_inst_dir, 
                flags=self.configure_flags)

  def install(self):
    super(PetscInstaller, self).install()
    make(np=self.np)
    make("PETSC_DIR="+pwd()+" PETSC_ARCH=uly all")
    make("PETSC_DIR="+pwd()+" PETSC_ARCH=uly install")

  def export(self):
    super(PetscInstaller, self).export()
    export_var(self.name.upper()+"_DIR", self.opt_inst_dir)
    PETSC_DIR=os.environ["PETSC_DIR"]
    export_var("PETSC_ARCH","")
    export_var("OPENMPI_DIR",PETSC_DIR)
    export_var("HDF5_DIR",PETSC_DIR)
    export_var("METIS_DIR",PETSC_DIR)
    export_var("PARMETIS_DIR",PETSC_DIR)
    export_var("SUPERLU_DIST_DIR",PETSC_DIR)
    export_var("SUPERLU_DIR",PETSC_DIR)
    export_var("SCALAPACK_DIR",PETSC_DIR)
    export_var("MUMPS_DIR",PETSC_DIR)
    export_var("HYPRE_DIR",PETSC_DIR)
    
    export = open(self.export_filename, 'a')
    export.write("export " + self.name.upper() + "_DIR=" + self.opt_inst_dir)
    export.write("export PETSC_ARCH=")
    export.write("export OPENMPI_DIR="+PETSC_DIR)
    export.write("export HDF5_DIR="+PETSC_DIR)
    export.write("export METIS_DIR="+PETSC_DIR)
    export.write("export PARMETIS_DIR="+PETSC_DIR)
    export.write("export SUPERLU_DIST_DIR="+PETSC_DIR)
    export.write("export SUPERLU_DIR="+PETSC_DIR)
    export.write("export SCALAPACK_DIR="+PETSC_DIR)
    export.write("export MUMPS_DIR="+PETSC_DIR)
    export.write("export HYPRE_DIR="+PETSC_DIR)
    export.close()