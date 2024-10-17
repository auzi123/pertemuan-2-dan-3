import PySimpleGUI as sg
sg.theme("dark magenta")
sg.theme_text_color("#006400")
window = sg.Window(title="Profile",
layout=[[sg.Text("SELAMAT DATANG DI KELAS",
font=("Arial",25,"italic","bold","underline"))],
[sg.Text("NPM : 2210010510 ")],
[sg.Text("Nama : AHMAD FAUZI ")],
[sg.Text("Kelas : 5M Regular Banjarmasin ")],
[sg.Text("Matkul : Pemograman berbasis obejek 2 ")]
],
size=(510,200),
font=("Times", 18))
window()
window.close()