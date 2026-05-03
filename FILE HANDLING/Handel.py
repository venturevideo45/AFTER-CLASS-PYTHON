file_read = open('123.txt','r')
print("File in Read Mode-")
print(file_read.read())
file_read.close()

file_write = open('123.txt', 'w')

file_write.write(" File in write mode ....")
file_write.write("Lightweight, extreme and uncompromising. The BOLIDE is BUGATTI's track-only hypercar built around the iconic W16 engine.")
file_write.close()

file_append = open('123.txt', 'a')

file_append.write("\n File in append mode ....")
file_append.write("Lightweight, extreme and uncompromising. The BOLIDE is BUGATTI's track-only hypercar built around the iconic W16 engine.")
file_append.close()