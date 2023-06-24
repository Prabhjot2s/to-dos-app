import function
import PySimpleGUI as py


label=py.Text("To-do-list")
#Input box
input_box=py.InputText(tooltip="Enter Todo",key='todo')
list_box=py.Listbox(values=function.openfile(),key='todos',enable_events=True,size=[45,10])

#Button for all the operations
button=py.Button("Add")
compelte=py.Button('Complete')
edit=py.Button("Edit")
#Layout window
window=py.Window('App',layout=[[label],[input_box,button],[compelte,list_box,edit]]
                 ,font=('Times new roman',20))


while True:

    value=window.read()
    window['todo'].update(value[1]['todos'][0])
    print(value)


    if value[0] == 'Add':
        file_value = function.openfile()
        file_value.append((value[1]['todo'])+'\n')
        function.writeline(file_value)
    elif value[0] == 'Complete':
        try:
            num = int(value[1]['todo'])
            vari = function.openfile()
            vari.pop(num - 1)
            function.writeline(vari)
        except IndexError:
            print("This line does not exsist")

    elif value[0] == 'Edit':

            todos=value[1]['todos'][0]
            new_todo=value[1]['todo']+'\n'
            values=function.openfile()
            index=values.index(todos)
            values[index]=new_todo
            function.writeline(values)
            window['todos'].update(values=values)




    elif value[0]==py.WIN_CLOSED:
        break

window.close()
