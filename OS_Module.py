# -*- coding: utf-8 -*-
"""
Created on Wed May  9 12:30:32 2018

@author: Jagan
"""
#%%
import os

#%%
"To get the login name of the user"

print (os.getlogin())


"To get parent/USer process id"

print(os.getppid())   # dynamically created each time login

#print(dir(os))
"To Print the current working directory"

print(os.getcwd())
#%%
"To chane=ge or navigate the directory"

os.chdir('D:/MIT/MAIN PROJECTS/new_jagan')
print(os.getcwd())
#%%
"To check the files and folders in the directory"

print (os.listdir())



#%%
"To create the folder"
#os.mkdirs("folder_name",mode=0o777)    # mode --> will set the permission to the directory
os.mkdir('new_jagan') #To create single level folder



#%%
"to create multilevel/hierarchial folder."
#os.mkdirs("folder_name",mode=0o777,exist_ok=True)  		# exits_ok=False   --->  shows error if directory exist.
															# exits_ok=True     --->  If folder exists, it won't shows any error but it will skip the creation for that folder.
os.makedirs('new_jagan1/jagan1/jagan2',exist_ok=True)


#%%
"To remove the folder"

os.rmdir('new_jagan')


#%%
"to create multilevel folder."

os.removedirs('new_jagan1/jagan1/jagan2')


#%%
"To rename the file"

os.rename('demo.txt', 'test.txt')
#%%


"to check the status of the files"

print(os.stat('test.txt'))     #os.stat_result(st_mode=16749, st_ino=562949953423519, st_dev=2155988667, st_nlink=1, st_uid=0, st_gid=0,
								# st_size=16384, st_atime=1555650690, st_mtime=1555650690, st_ctime=1541072344)


#%%

"To read the links for the directory or from the files in the directory"
#os.readlink("path/to/the/file or directory")
print (os.readlink('C:/Users/jagannathan.s/Desktop/sendfile'))


#%%
"To get the directory path,directory names, filename via os.walk"

for dirpath, dirname, filename in os.walk('D:\MIT\MAIN PROJECTS\CONFERENCES'):
    print("directory path:",dirpath)   #directory path
    print("directory name:",dirname)   #directories or folders
    print("file name:",filename)       #file names
#%%
"To get the environment variables"

os.environ   #To print all environment variables.
#%%
"To get specific environment variable"

print(os.environ.get('bin'))
#%%
"To create  file- Method 1 : manually putting up the path laong with file"

path=os.getcwd()
new_file_path=path + '\\'  + 'new.txt'
print(new_file_path)
#%%
"To create  file- Method 1 : using os.path.join"

new_file_path=os.path.join(os.getcwd(),'new.txt')
print(new_file_path)
#%%
"Use of os.path.basename()"

new_file_path=os.path.join(os.getcwd(),'new.txt') #this will provide the base file name
print(os.path.basename(new_file_path))
#%%
"Use of os.path.dirname()"

new_file_path=os.path.join(os.getcwd(),'new.txt') #this will provide the directory name
print(os.path.dirname(new_file_path))
#%%
"Use of os.path.split()"

new_file_path=os.path.join(os.getcwd(),'new.txt') #this will split the directory and file namee
                                                  # put it in a tuple
print(os.path.split(new_file_path))
#%%
"""
SOme other common functions are

os.path.exsists()
os.path.isdir()
os.path.isfile()
"""
#%%
"os.path.splitext() -- To split the file name and its extension"

new_file_path=os.path.join(os.getcwd(),'new.txt') #this will provide the directory name
print(os.path.splitext(new_file_path))
#%%

