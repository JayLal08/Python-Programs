text = input("Enter content which you want to store in file: ")
with open("file.txt","w") as f:
 f.write(text)
 print("Entered content written to the file successfully!!!")
 print("File closed")
with open("file.txt","r") as f:
 file_text = f.read()
 print("Content of file:\n",file_text)