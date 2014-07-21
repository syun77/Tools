#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import glob

dir = os.getcwd()
list = glob.glob(dir + '/src/*.png')
cmd = "/opt/local/bin/convert +append "
for fName in list:
	cmd += fName + " "

cmd += dir + '/out.png'

os.system(cmd)

