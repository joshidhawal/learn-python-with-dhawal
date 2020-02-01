import os
# First we will create a file.
f = open("C:/Users/joshidhawal/Documents/Git/learn-python-with-dhawal/testfile.txt","a+")
print("A new text file is created and opened in append+ mode")
# Writing in the file
f.write("Hello World! This is my first created file")
print("Message is written in file")
# Reading the written text
print("This is the position of cursor in the file : "+str(f.tell()))
f.seek(0)
print("We changed the cursor position to beginning,so now we can read the file.")
print(f.readline())
print("Message is read")
# Closing the file
f.close()   
print("File is closed")
# Delete the file
os.remove("C:/Users/joshidhawal/Documents/Git/learn-python-with-dhawal/testfile.txt")
print("File deleted")