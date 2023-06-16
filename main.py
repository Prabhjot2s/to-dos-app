import time
now=time.strftime("%b %Y, %H:%M:%S")
print("It is",now)

print("Welcome to the list\n ")


def openfile():
    with open("file.txt",'r') as file:
        file=file.readlines()
        return file

def writeline(toenter):
    with open("file.txt",'w') as file:
         file.writelines(toenter)


items=[]
while True:
    choice=input("Do you want to ADD,SHOW,CREATE,EXIT ,edit,compelete ").strip()

    if 'add' in choice[0:4]:
        it=choice[4:]+'\n'
        fromfile=openfile()
        fromfile.append(it)
        writeline(fromfile)



    elif 'show' in choice:
        values=openfile()
        for index,each in enumerate(values):
          print(f"{index+1}-{each}".strip())



    elif 'exit' in choice:
        break


    elif 'edit' in choice:
        try:
            edi=openfile()
            print(edi)
            if edi:
                 for i,each in enumerate(edi):
                    print(f"{i+1}-{each.strip()}")
                 cho=int(input('enter the number you want to edit '))
                 cho=cho-1
                 ed=input('enter the new edited paart ')
                 edi[cho]=ed+'\n'
                 writeline(edi)
            else:
                print("No items to edit")

        except IndexError:
            print("It is not part of the list")
            continue


    elif 'compelte' in choice:
        try:
            num=int(input("Enter the index you want me to delete "))
            vari=openfile()
            vari.pop(num-1)
            file=open("file.txt",'w')
            writeline(vari)
        except IndexError:
            print("This line does not exsist")


    else:
        print("Enter the given options")




