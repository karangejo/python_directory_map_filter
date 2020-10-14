#!/usr/bin/env python
import optparse
from dir_library import dir_map, recursive_dir_map

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-c','--cmd', dest='cmd',help='command to be mapped to all files')
    parser.add_option('-d','--dir', dest='dir',help='directory containing the files')
    parser.add_option('-o','--opt', dest='opt',help='options to be passed to the command')
    parser.add_option('-r','--rec', action="store_true", dest="rec", default=False, help='recursive map through directories')
    options = parser.parse_args()[0]
    if not options.cmd and not options.dir:
        parser.error("Please enter a command and a directory")
    return options

options = get_arguments()
if not options.rec:
    if not options.opt:
        dir_map(options.dir, options.cmd)
    else:
        opt = list(options.opt.split(" "))
        dir_map(options.dir,options.cmd, opt)
elif (not options.opt):
    recursive_dir_map(options.dir, options.cmd)
else:
    opt = list(options.opt.split(" "))
    recursive_dir_map(options.dir, options.cmd, opt)

