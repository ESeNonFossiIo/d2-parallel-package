from _libs._modules.modules import *
              
class OCEInstaller(ModuleInstaller):
  cmake_flags = " -DOCE_BUILD_SHARED_LIB:BOOL=ON \
                  -DOCE_BUILD_TYPE:STRING=Release \
                  -DOCE_DATAEXCHANGE:BOOL=ON \
                  -DOCE_DISABLE_X11:BOOL=ON \
                  -DOCE_DRAW:BOOL=OFF \
                  -DOCE_MODEL:BOOL=ON \
                  -DOCE_MULTITHREAD_LIBRARY:STRING=NONE \
                  -DOCE_OCAF:BOOL=ON \
                  -DOCE_OSX_USE_COCOA:BOOL=ON \
                  -DOCE_USE_TCL_TEST_FRAMEWORK:BOOL=OFF \
                  -DOCE_VISUALISATION:BOOL=OFF \
                  -DOCE_WITH_FREEIMAGE:BOOL=OFF \
                  -DOCE_WITH_GL2PS:BOOL=OFF \
                  -DOCE_WITH_OPENCL:BOOL=OFF "
                
  def __init__(self):
    super(OCEInstaller, self).__init__("oce")
  
  def compile(self):
    super(OCEInstaller, self).compile()
    build="build_"+self.hash_pkg
    mkdir(build)
    cd(build)
    cmake(  cmake_list_path = "..", 
            install_path = self.opt_inst_dir, 
            flags = self.cmake_flags )

  def install(self):
    super(OCEInstaller, self).install()
    make_install(np=self.np)

  def export(self):
    super(OCEInstaller, self).export()
    export_var(self.name.upper()+"_DIR", self.opt_inst_dir)
    export = open(self.export_filename, 'a')
    export.write("export " + self.name.upper() + "_DIR=" + self.opt_inst_dir)
    export.close()