#!/bin/bash

set -e # close the bash on error

# update all submodule directory
################################################################################
git submodule update --init --recursive