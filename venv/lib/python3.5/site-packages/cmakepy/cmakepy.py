#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import argparse
from jinja2 import Environment, PackageLoader


subdirs=['src','Binaries','Build']

def check_path(string):    
    value = str(string)
    if os.path.exists(string):
        msg = "Folder %r already exists!!!" % string
        raise argparse.ArgumentTypeError(msg)  
    return value
  
  
def main():    
    parser = argparse.ArgumentParser(description='Creates a new Cmake project')
    parser.add_argument('project', metavar='project-name', type=check_path, help='a name for the project')    
    args = parser.parse_args()    
    project = args.project
    
    #Creates all folders for the project
    os.mkdir(project)
    for item in subdirs:
        os.makedirs(os.path.join(project,item))
    
    #Renders the templates
    env = Environment(loader=PackageLoader('cmakepy', 'templates'))
    
    template = env.get_template('CMakeLists.txt')    
    with open(os.path.join(project,'CMakeLists.txt'), 'w') as f:
        f.write(template.render(project=project))  
    
    template = env.get_template('main.cpp')
    with open(os.path.join(project,subdirs[0],'main.cpp'), 'w') as f:
        f.write(template.render(project=project))
    
    #Run cmake
    cwd = os.getcwd()
    os.chdir(os.path.join(cwd,project,subdirs[2]))
    subprocess.call(['cmake','..'])
    os.chdir(cwd)


if __name__=="__main__":
    main()