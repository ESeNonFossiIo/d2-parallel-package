from _libs._modules.modules import *
              
class TrilinosInstaller(ModuleInstaller):
  cmake_flags = " -DCMAKE_BUILD_TYPE:STRING=RELEASE \
                  -DTPL_ENABLE_Boost:BOOL=OFF \
                  -DTPL_ENABLE_BoostLib:BOOL=OFF \
                  -DTrilinosFramework_ENABLE_MPI:BOOL=ON \
                  -DTPL_ENABLE_MPI:BOOL=ON \
                  -DTPL_ENABLE_Netcdf:BOOL=OFF \
                  -DTrilinos_ENABLE_OpenMP:BOOL=OFF \
                  -DBUILD_SHARED_LIBS:BOOL=ON \
                  -DTrilinos_WARNINGS_AS_ERRORS_FLAGS:STRING=\"\" \
                  -DCMAKE_VERBOSE_MAKEFILE:BOOL=FALSE \
                  -DTrilinos_ASSERT_MISSING_PACKAGES:BOOL=OFF \
                  -DTrilinos_ENABLE_TESTS:BOOL=OFF \
                  -DTrilinos_ENABLE_ALL_PACKAGES:BOOL=OFF \
                  -DTrilinos_ENABLE_ALL_OPTIONAL_PACKAGES:BOOL=ON \
                  -DTrilinos_ENABLE_Epetra:BOOL=ON \
                  -DTrilinos_ENABLE_EpetraExt:BOOL=ON \
                  -DTrilinos_ENABLE_Tpetra:BOOL=ON \
                  -DTrilinos_ENABLE_STK:BOOL=OFF \
                  -DTrilinos_ENABLE_Jpetra:BOOL=ON \
                  -DTrilinos_ENABLE_Kokkos:BOOL=ON \
                  -DTrilinos_ENABLE_Sacado:BOOL=ON \
                  -DTrilinos_ENABLE_Amesos:BOOL=ON \
                  -DTrilinos_ENABLE_AztecOO:BOOL=ON \
                  -DTrilinos_ENABLE_Ifpack:BOOL=ON \
                  -DTrilinos_ENABLE_Teuchos:BOOL=ON \
                  -DTrilinos_ENABLE_Rythmos:BOOL=ON \
                  -DTrilinos_ENABLE_Piro:BOOL=ON \
                  -DTrilinos_ENABLE_MOOCHO:BOOL=ON \
                  -DTrilinos_ENABLE_ML:BOOL=ON \
                  -DTrilinos_ENABLE_MueLu:BOOL=ON \
                  -DTrilinos_ENABLE_Komplex:BOOL=ON \
                  -DTrilinos_ENABLE_Thyra:BOOL=ON \
                  -DTrilinos_ENABLE_TrilinosCouplings:BOOL=ON "
                
  def __init__(self):
    super(TrilinosInstaller, self).__init__("trilinos")
  
  def compile(self):
    super(TrilinosInstaller, self).compile()
    build="build_"+self.hash_pkg
    mkdir(build)
    cd(build)
    cmake(  cmake_list_path = "..", 
            install_path = self.opt_inst_dir, 
            flags = self.cmake_flags )

  def install(self):
    super(TrilinosInstaller, self).install()
    make_install(np=self.np)

  def export(self):
    super(TrilinosInstaller, self).export()
    export_var(self.name.upper()+"_DIR", self.opt_inst_dir)
    export = open(self.export_filename, 'a')
    export.write("export " + self.name.upper() + "_DIR=" + self.opt_inst_dir)
    export.close()