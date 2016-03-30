#!/usr/bin/env python

from _libs._modules.modules import *
from _libs._modules.pkg import *

module_installer=ModuleInstaller("module installer")
module_installer.init_export_file()

unset("CXX CC F77 FC")

# [ ninja.NinjaInstaller(), 
#   ompi.OpenMPInstaller(), 
#   sundials.SundialsInstaller(), 
#   trilinos.TrilinosInstaller(),
#   oce.OCEInstaller(),
#   dealii.DealIIInstaller(), 
#   deal2lkit.Deal2lkitInstaller()]
for installer in [oce.OCEInstaller()]:
  installer.print_status()
  installer.compile()
  installer.install()
  installer.export()

# from ConfigParser import *
# 
# from _libs._utilities.text import *
# from _libs._utilities.bash_cmd import *
# from _libs._utilities.log import *
# from _libs._utilities.utilities import *
# 
# 
# general = ConfigParser()
# general.read("_conf/configuration.cfg")
# general_secs=general.sections()
# 
# package = ConfigParser()
# package.read("_conf/packages.cfg")
# package_secs=package.sections()
# 
# package_inst = ConfigParser()
# package_inst.read("_conf/packages_inst.cfg")
# package_inst_secs=package.sections()
# 
# base_dir = general.get("default", "base_dir")
# opt_inst = general.get("default", "opt_inst")
# np = general.get("default", "np")
# 
# 
# print BAR
# print log_var("base dir package", base_dir)
# print log_var("opt install path", opt_inst)
# print log_var("number of process", np)
# print BAR
# 
# # Ompi:
# ################################################################################
# 
# 
# 
# # package_list = ["ompi", "sundials", "oce" ]
# 
# # package_list = [ "p4est" ]
# package_list = [ "trilinos" ]
# 
# for pkg in package_list:
#   
#   name         = package.get(pkg, "name")
#   path         = package.get(pkg, "path")
# 
#   cd(path)
#   print "--->"+pwd()
# 
#   do_autogen   = str_to_bool(package_inst.get(pkg, "autogen"))
#   do_configure = str_to_bool(package_inst.get(pkg, "configure"))
#   if do_configure:
#     do_autoconf=str_to_bool(package_inst.get(pkg, "autoconf"))
#     configure_flags=package_inst.get(pkg, "conf_flags").replace('\n',' ')
#   do_cmake     = str_to_bool(package_inst.get(pkg, "cmake"))
#   do_make_inst = str_to_bool(package_inst.get(pkg, "make_inst"))
#   do_make_clean = str_to_bool(package_inst.get(pkg, "make_clean"))
#   if do_cmake:
#     cmake_flags=package_inst.get(pkg, "cmake_flags").replace('\n',' ')
#   hash_pkg     = str(get_abbrev()).rstrip()
# 
#   print BAR
#   print bar
#   print log_var("name", name)
#   print log_var("path", path)
#   print log_var("hash", hash_pkg)
#   print log_var("build", path+"/build-"+hash_pkg)
#   print log_var("autogen", str(do_autogen))
#   print log_var("configure", str(do_configure))
#   if do_configure:
#     print log_var("autoconf", str(do_autoconf))
#     print log_var("configure_flags", configure_flags)
#   print log_var("make_inst", str(do_make_inst))
#   print log_var("make_clean", str(do_make_clean))
#   print log_var("cmake", str(do_cmake))
#   if do_cmake:
#     print log_var("cmake_flags", cmake_flags)
#   print bar
# 
#   # Define variables:
#   build="build_"+hash_pkg
#   install_path=opt_inst+name+"-"+hash_pkg
#   
#   if do_autogen:
#     print_title("autogen")
#     run("./autogen.sh")
#     
#   if do_configure:
#     if(do_make_clean):
#       make_clean()
#     if(do_autoconf):
#       autoconf()
#     print_title("configure")
#     mkdir(install_path)
#     print pwd()
#     configure(prefix=install_path, flags=configure_flags)
# 
#   if do_cmake:
#     print_title("cmake")
#     mkdir(build)
#     cd(build)
#     cmake( cmake_list_path = "..", install_path = install_path, flags = cmake_flags)
# 
#   if do_make_inst:
#     print_title("make install")
#     make_install(np)
# 
#   # Update env settings:
#   # TODO: add .conf...
#   for line in list_dirs(opt_inst):
#     path_library=opt_inst+line
#     name=line.split("-")[0].upper()
#     export(name+"_DIR",path_library)
#     add_to_path(path_library+"/bin")
#     print " Library : " + name
#     print "   path  : " + path_library
#     # print os.environ
# 
#   # Additional varibales set within OMPI
#   try: 
#     OMPI_DIR=os.environ["OMPI_DIR"]
#     export("MPI_HOME",OMPI_DIR)
#     export("CC",which("mpicc"))
#     export("CXX",which("mpic++"))
#     export("F77",which("mpif77"))
#     export("FC",which("mpif77"))
#     export("F90",which("mpif90"))
#   except:
#     pass
#     
#   # Additional libraries downloaded within PETSc
#   try:
#     PETSC_DIR=os.environ["PETSC_DIR"]
#     export("PETSC_ARCH","")
#     export("OPENMPI_DIR",PETSC_DIR)
#     export("HDF5_DIR",PETSC_DIR)
#     export("METIS_DIR",PETSC_DIR)
#     export("PARMETIS_DIR",PETSC_DIR)
#     export("SUPERLU_DIST_DIR",PETSC_DIR)
#     export("SUPERLU_DIR",PETSC_DIR)
#     export("SCALAPACK_DIR",PETSC_DIR)
#     export("MUMPS_DIR",PETSC_DIR)
#     export("HYPRE_DIR",PETSC_DIR)
#   except:
#     pass
