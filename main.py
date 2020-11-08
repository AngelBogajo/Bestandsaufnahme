# Bestandsaufnahme bei Angel jesus Bogajo
#
# muss haben:
#
# window
# fixed size
# not resizable
# a menu (Home, Add, Info, Exit)
# option to exit
# different screens
# add product form
# save data temporarily
# display data listed on the home screen


from tkinter import *


window = Tk()
window.geometry("400x400")
window.title("BESTANDSAUFNAHME -> Angel J. Bogajo")
window.resizable(False, False)
# Menü
mein_Menu = Menu(window)

# Hauptmenü
mein_Menu.add_cascade(label="Home")
mein_Menu.add_command(label="Add")
mein_Menu.add_command(label="Info")
mein_Menu.add_command(label="Exit", command=window.quit)

# carga el menu
window.config(menu=mein_Menu)


window.mainloop()