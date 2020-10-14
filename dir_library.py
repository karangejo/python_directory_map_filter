import subprocess
import os

def apply_one(path, cmd, options = []):
    if (options == []):
        subprocess.run([cmd, path])
    else:
        subprocess.run([cmd] + options + [path])

def dir_map(dir_path, cmd, options = []):
    file_list = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    for filename in file_list:
        apply_path = os.path.join(dir_path, filename)
        apply_one(apply_path, cmd, options)

def recursive_dir_map(dir_path, cmd, options = []):
    ls = os.listdir(dir_path)
    file_list = [f for f in ls if os.path.isfile(os.path.join(dir_path, f))]
    dir_list = [d for d in ls if os.path.isdir(os.path.join(dir_path, d))]
    for filename in file_list:
        apply_path = os.path.join(dir_path, filename)
        apply_one(apply_path, cmd, options)
    if(dir_list != []):
        for directory in dir_list:
            path = os.path.join(dir_path, directory)
            recursive_dir_map(path, cmd, options)

def dir_filter_map(dir_path, cmd, ext, options = []):
    file_list = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    for filename in file_list:
        extension = os.path.splitext(filename)[1]
        if(extension in ext):
            apply_path = os.path.join(dir_path, filename)
            apply_one(apply_path, cmd, options)


def recursive_dir_filter_map(dir_path, cmd, ext, options = []):
    ls = os.listdir(dir_path)
    file_list = [f for f in ls if os.path.isfile(os.path.join(dir_path, f))]
    dir_list = [d for d in ls if os.path.isdir(os.path.join(dir_path, d))]
    for filename in file_list:
        extension = os.path.splitext(filename)[1]
        if(extension in ext):
            apply_path = os.path.join(dir_path, filename)
            apply_one(apply_path, cmd, options)
    if(dir_list != []):
        for directory in dir_list:
            path = os.path.join(dir_path, directory)
            recursive_dir_filter_map(path, cmd, ext, options)
