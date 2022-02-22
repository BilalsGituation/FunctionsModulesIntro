'''
Working with os:
Create a directory structure by using os.
Create one parent directory with at least five child
directories.
Create a file in each directory simply by using os and by changing directories
beforehand
'''
import os

# Deletes any trace of the script from before
os.system("rm -r Parent")
# Make Parent Directory
os.mkdir("Parent")
# Make first Child Directory
os.mkdir("Parent/Child1")
# Write a file into it
os.system("touch Parent/Child1/file1")
# Do same for second Child Directory
os.mkdir("Parent/Child2")
os.system("touch Parent/Child2/file2")
# Do same for third Child Directory
os.mkdir("Parent/Child3")
os.system("touch Parent/Child3/file3")
# Do same for fourth Child Directory
os.mkdir("Parent/Child4")
os.system("touch Parent/Child4/file4")
# Do same for fifth Child Directory
os.mkdir("Parent/Child5")
os.system("touch Parent/Child5/file5")
# Shows what has been done
print("Contents of Directory we have run this script in are:")
os.system("ls")
os.chdir("Parent")
print("Contents of Directory Parent are:")
os.system("ls")
os.chdir("Child1")
print("Contents of Directory Child1 are:")
os.system("ls")
os.chdir("../Child2")
print("Contents of Directory Child2 are:")
os.system("ls")
os.chdir("../Child3")
print("Contents of Directory Child3 are:")
os.system("ls")
os.chdir("../Child4")
print("Contents of Directory Child4 are:")
os.system("ls")
os.chdir("../Child5")
print("Contents of Directory Child5 are:")
os.system("ls")
# Deletes directory so that system returns to start point
os.chdir(r"..")
os.chdir(r"..")
print("Deleting directories formed by this script...")
os.system("rm -r Parent")
print("Contents of the directory in which we ran the script:")
os.system("ls")
