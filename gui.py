import function
import PySimpleGUI as py
import time




label=py.Text("To-do-list")
labels=py.Text("",key="Clock")
#Input box
input_box=py.InputText(tooltip="Enter Todo",key='todo')
list_box=py.Listbox(values=function.openfile(),key='todos',enable_events=True,size=[45,10])

#Button for all the operations
button=py.Button("Add")
compelte=py.Button('Complete')
edit=py.Button("Edit")
exit=py.Button("Exit")
#Layout window
window=py.Window('App',layout=[[label,labels],[input_box,button],[compelte,list_box,edit],[exit]]
                 ,font=('Times new roman',20))


while True:

    value=window.read(timeout=200)
    print(value)
    window['Clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    if value[0] == 'Add':
        file_value = function.openfile()
        file_value.append((value[1]['todo'])+'\n')
        function.writeline(file_value)
        window['todos'].update(file_value)

    elif value[0] == 'Complete':
        try:
            to_remove = value[1]['todos'][0]
            vari = function.openfile()
            vari.remove(to_remove)
            function.writeline(vari)
            window['todos'].update(values=vari)
            window['todo'].update(value='')
        except IndexError:
            py.popup('Select a task to compelte',title="Error",font=20)

    elif value[0] == 'Edit':
        try:

                todos=value[1]['todos'][0]
                new_todo=value[1]['todo']+'\n'
                values=function.openfile()
                index=values.index(todos)
                values[index]=new_todo
                function.writeline(values)
                window['todos'].update(values=values)
        except IndexError:
            py.popup("Select Something First To Edit ",font=20,title="Error")



    elif value[0]=='todos' :
     try:
        window['todo'].update(value[1]['todos'][0])
     except IndexError:
        continue

    elif value[0]=='Exit':
        break




    elif value[0]==py.WIN_CLOSED:
        break

window.close()
