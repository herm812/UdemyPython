import FreeSimpleGUI as sg
import converters

sg.theme="LightGreen4"

label1 = sg.Text("Enter feet: ")
label2 = sg.Text("Enter inches: ")
button1 = sg.Button("Convert")
input1 = sg.Input(key="feet")
input2 = sg.Input(key="inches")
exit_button = sg.Button("Exit")

outputtext=sg.Text("", key="output")
window = sg.Window("Converter",
                    layout = [[label1, input1],
                              [label2, input2],
                              [button1, exit_button, outputtext]],
                    font=('Arial', 18))

while True:
    event,values = window.read()
    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
    try:
        foot = float(values["feet"])
        inch = float(values["inches"])
        answer = converters.convert(foot, inch)
        window["output"].update(value=f"{answer} meters", text_color="Black")
    except ValueError:
        sg.popup("Please enter a both numbers", font=('Times',20))

window.close()
