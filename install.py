#!/usr/bin/env python

from _libs._modules.modules import *
from _libs._modules.pkg import *

module_installer=ModuleInstaller("module installer")
module_installer.init_export_file()
del module_installer

unset("CXX CC F77 FC")

for installer in [  ninja.NinjaInstaller, 
                    ompi.OpenMPInstaller, 
                    sundials.SundialsInstaller, 
                    petsc.PetscInstaller,
                    slepc.SlepcInstaller,
                    p4est.P4estInstaller,
                    trilinos.TrilinosInstaller,
                    oce.OCEInstaller,
                    dealii.DealIIInstaller, 
                    deal2lkit.Deal2lkitInstaller]:
  inst = installer()
  inst.print_status()
  inst.compile()
  inst.install()
  inst.export()
  del inst