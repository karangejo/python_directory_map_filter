#!/usr/bin/env python
import optparse
from dir_library import dir_filter_map, recursive_dir_filter_map

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-e','--ext', dest='ext',help='extension to be filtered through')
    parser.add_option('-c','--cmd', dest='cmd',help='command to be mapped to all files')
    parser.add_option('-d','--dir', dest='dir',help='directory containing the files')
    parser.add_option('-o','--opt', dest='opt',help='options to be passed to the command')
    parser.add_option('-r','--rec', action="store_true", dest="rec", default=False, help='recursive map through directories')
    options = parser.parse_args()[0]
    if (options.cmd == None) or (options.dir == None) or (options.ext == None):
        parser.error("Please enter a command and a directory and an extension filter")
    return options

options = get_arguments()
print(options)
if not options.rec:
    if not options.opt:
        dir_filter_map(options.dir, options.cmd, options.ext)
    else:
        opt = list(options.opt.split(" "))
        dir_filter_map(options.dir,options.cmd, options.ext, opt)
elif (not options.opt):
    recursive_dir_filter_map(options.dir, options.cmd, options.ext)
else:
    opt = list(options.opt.split(" "))
    recursive_dir_filter_map(options.dir, options.cmd, options.ext, opt)

