import os
try :
    f = open("C:/Users/joshidhawal/Documents/Git/learn-python-with-dhawal/testfile.txt","r")

except  FileNotFoundError:
    print ("The desired file is not found, we will create one for you instead.")
    f = open("C:/Users/joshidhawal/Documents/Git/learn-python-with-dhawal/testfile.txt","a+")
    print("A new file is created")
    f.write("Hello World!")
    print("Message is written in it.")
finally:
    f.seek(0)
    print("The cursor is moved to beginning of file")
    print(f.read())
    print("The message is read")
    f.close()
    print("File is closed")
    os.remove("C:/Users/joshidhawal/Documents/Git/learn-python-with-dhawal/testfile.txt")
    print("the file is been deleted")
    
    