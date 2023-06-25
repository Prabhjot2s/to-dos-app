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
exit=py.Button("Exit")
#Layout window
window=py.Window('App',layout=[[label],[input_box,button],[compelte,list_box,edit],[exit]]
                 ,font=('Times new roman',20))


while True:

    value=window.read()
    print(value)

    if value[0] == 'Add':
        file_value = function.openfile()
        file_value.append((value[1]['todo'])+'\n')
        function.writeline(file_value)
        window['todos'].update(file_value)

    elif value[0] == 'Complete':
        to_remove = value[1]['todos'][0]
        vari = function.openfile()
        vari.remove(to_remove)
        function.writeline(vari)
        window['todos'].update(values=vari)
        window['todo'].update(value='')

    elif value[0] == 'Edit':

            todos=value[1]['todos'][0]
            new_todo=value[1]['todo']+'\n'
            values=function.openfile()
            index=values.index(todos)
            values[index]=new_todo
            function.writeline(values)
            window['todos'].update(values=values)

    elif value[0]=='todos' :
      window['todo'].update(value[1]['todos'][0])

    elif value[0]=='Exit':
        break




    elif value[0]==py.WIN_CLOSED:
        break

window.close()
