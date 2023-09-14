from pathlib import Path
import pdb
"""
program to flatten files from directory and avoid duplicate files
"""
duplicate_file_count = {}
def get_duplicate_file_name_count(file_name):
    """
    Returns the count of unique file names from the `duplicate_file_count` dictionary.

    Args:
        file_name (str): The name of the file.

    Returns:
        int: The count of the duplicate file name.
    """
    return duplicate_file_count[file_name]

def update_duplicate_file_name_count(file_name):
    if file_name in duplicate_file_count:
        duplicate_file_count[file_name] = duplicate_file_count[file_name]+1
    else:
         print("hello")
         duplicate_file_count[file_name] = 1

def flatten(folder: dir):
    target_dir = folder.parents[0]
    """ This function  iterate through all folders and flatten the files"""
    if folder.is_dir():
        for files in  folder.rglob("*"):
                if files.suffix == '.txt':
                    
                    if files.name in duplicate_file_count:
                        count = get_duplicate_file_name_count(files.name)
                        files.rename(target_dir.joinpath(f"{files.stem}{count}{files.suffix}"))
                        update_duplicate_file_name_count(files.name)
                        update_duplicate_file_name_count(f"{files.stem}{count}{files.suffix}")
                        pdb.set_trace()
                    else:
                        files.rename(target_dir.joinpath(files.name))
                        update_duplicate_file_name_count(files.name)

    else:
         print('passed argument  is not folder')
                     
                     


                

if __name__=="__main__":
    cwd = Path.cwd()
    print(cwd)
    target_dir = cwd.parents[0]  
    # for files in cwd.rglob("*"):
    #     if files.suffix == '.txt':
    #          files.rename(target_dir.joinpath(f"{files.stem}temp{files.suffix}"))
    #          print(files.name)
    # for files in cwd.rglob("*"):
    #     print(files.name)
    # print(type(cwd))
    flatten(cwd)
    

