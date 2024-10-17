import PySimpleGUI as sg
susunan=[[sg.Text("UNISKA MAAB",font=("helvetica",24))],
            [sg.Text("BANJARMASIN", font=("Courier",18))]]
Window = sg.Window(title="New Icon",
                    layout=susunan,
                    element_justification = "center",
                    icon="favicon.ico",
                    resizable=True,
                    size=(430,200))

Window.read()
Window.close()