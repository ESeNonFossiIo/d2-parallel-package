#!/bin/bash

################################################################################
# This programms add all submodule written in PKG_CFG
################################################################################

# set -e

# Conifigure variables:
################################################################################
PKG_CFG="./_conf/packages.cfg"

# Conifigure commands and functions:
################################################################################
CUT=$(which cut)
SED=$(which sed)
GIT=$(which git)
function extract_value {
  echo $1 | $CUT -d "=" -f 2 | $SED "s# ##"
}

# add submodules:
################################################################################
exec 10<$PKG_CFG
while read -u10 p; do
  
  read -u10 p
  NAME=`extract_value "$p"`
  
  read -u10 p
  MODULE_PATH=`extract_value "$p"`
  
  read -u10 p
  URL=`extract_value "$p"`

  echo "======================================================================="
  echo " Name ....... " $NAME
  echo " path ....... " $MODULE_PATH
  echo " url ........ " $URL
  echo "  ----> add submodule"
  echo "-----------------------------------------------------------------------"
  $GIT submodule add --force --name $NAME $URL $MODULE_PATH
  echo "======================================================================="
  echo ""
  read -u10 p
done

# $GIT submodule sync
$GIT submodule update --remote --recursive 