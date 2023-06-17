def openfile():
    with open("file.txt",'r') as file:
        file=file.readlines()
        return file

def writeline(toenter):
    with open("file.txt",'w') as file:
         file.writelines(toenter)

