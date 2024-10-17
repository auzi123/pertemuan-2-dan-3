import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
Window = sg.Window(title="Contoh Button",
                    layout=[[sg.text("Contoh Button")],
                    [sg.Button("Button simpan")],
                    [sg.Button("Button keluar")]
                    ],
            size=(400,200),
            font=("Times",18))
kejadian,nilai = Window.read()
print(kejadian,"=>",nilai)
Window.close()