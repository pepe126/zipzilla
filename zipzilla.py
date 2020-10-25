import os
import zipfile
import shutil

# Saving the current directory in 'directory' and
# the items in it in 'objects'

objects = os.listdir()
directory = os.getcwd()

# COMPRESSION FUNCTION


def compress(files, dir):
    # First loop check if compressed.zip is already there to avoid conflicts
    for file in files:
        if file == 'compressed.zip':
            print("compressed.zip already in the folder")
            return None  # end the funcition
    # Generation and opening of the .zip file
    comp_file = zipfile.ZipFile("compressed.zip", 'w')
    # Return the current base - directory(split between root and last dir)
    rootdir = os.path.basename(dir)
    # Walk loop through all directories in current directory
    for path, dir, files in os.walk(dir):
        for file in files:
            if "zipzilla" in file:  # Check for zipzilla in order to skip it
                continue
            else:
                # Join the path and the file name
                file_path = os.path.join(path, file)
                # Find the relative path starting from current dir to filepath
                parent_path = os.path.relpath(file_path)
                # Join the current base path to the relative path
                arcname = os.path.join(rootdir, parent_path)
                # Write in the compressed file the definitive path
                comp_file.write(file_path, arcname)
    comp_file.close()  # Close the .zip file


# CLEAR FUNCTION / Remove all the files


def clear(files):
    for file in files:
        # Check for zipzilla and compressed / they don't have to be removed
        if 'zipzilla' in file:
            pass
        elif 'compressed' in file:
            break
        else:
            # Error handling / os.remove return error for folders
            try:
                os.remove(file)
            except OSError:
                # Handle the error with shutil and remove full folder tree
                shutil.rmtree(file, ignore_errors=True)


# EXTRACT FUNCTION


def extract(files):
    for file in files:
        if file == "zipzilla.py":  # Check for zipzilla in order to skip it
            pass
        else:
            # Error handler in order to avoid any other file
            # as the program should extract only if there are zipzilla and
            # the .zip file I'm not expecting other files
            try:
                zip_obj = zipfile.ZipFile(file, 'r')    # open file.zip
                zip_obj.extractall('extracted')         # extract
                zip_obj.close()                         # close file.zip
            except OSError:
                print("There is no .zip file")


# LOGIC

# The code compress if there are more than 2 objects in the directory including
# zipzilla

# The code extract if there are only 2 objects in the directory including
# zipzilla

if len(objects) > 2:
    compress(objects, directory)
    clear(objects)
else:
    extract(objects)
