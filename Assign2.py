#normal 'r' mode
with open('file.txt', 'r') as f:  # default `r` mode
    f.write("test \n")
    
#'r+' mode
with open('file.txt', 'r+') as f:
f.write("new line \n")    
    
#'w' mode    
 myfile = open(“file.txt”,'w')
 myfile.write(“Hello from Python!”)

#'w+' mode
with open('file.txt', 'w+') as f:   # create a new file or truncates it
f.write("hi1\n")
f.write("hi2\n")
f.write("hi3\n")             
f.seek(0)                       
lines = f.read()                
print(lines)  

#'a' mode
with open('file.txt','a') as f:
f.write("4")
 
#'a+' mode  
with open('file.txt','a+') as f:
f.seek(0)                       
lines = f.readlines()           
f.write("\n" + str(len(lines))) 
