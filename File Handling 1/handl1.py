
file = open('File Handling 1\handl1.txt','r')
print(file.read())
file.close()

file = open('File Handling 1\handl1.txt','r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

file = open('File Handling 1\handl1.txt','a')
file.write(" Hello , this is a text from the program.")
print("\n After appending \n")
file.close()
file = open('File Handling 1\handl1.txt','r')
print(file.read())
file.close()

