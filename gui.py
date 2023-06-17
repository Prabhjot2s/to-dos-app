import function
import PySimpleGUI as py
a=[9,0]
file=function.openfile()
label=py.Text(file)
input_box=py.InputText(tooltip="Enter Todo")
button=py.Button("Submit")
button.ButtonPressCallBack(function.writeline(a))
window=py.Window('App',layout=[[label,input_box],[button]])
window.read()
window.close()
