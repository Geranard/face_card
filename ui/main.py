from tkinter import *
from login import Login

BLACK = "#1C2626"
WHITE = "#FFFFFF"
RED = "#FF0000"
PURPLE = "#552D96"
GREEN = "#00FF00"
GRAY = "#C4C4C4"
FONT = "Poppins"

main_window = Tk()
main_window.title("FACE CARD MANAGER")
main_window.config(bg=BLACK, padx=60, pady=60)
main_window.wm_minsize(875, 600)
main_window.wm_maxsize(875, 600)
main_window.iconbitmap("../ui_image/logo.ico")

login = Login(main_window)
login.login_page()

main_window.mainloop()