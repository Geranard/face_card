from tkinter import *
import tkinter.ttk as tk

main_window = Tk()
main_window.title("FACE CARD MANAGER")
main_window.config(bg="#000000", padx=60, pady=60)
main_window.wm_minsize(875, 600)
main_window.wm_maxsize(875, 600)

frame = Frame(main_window, bg="#000000")
frame.grid(column=0, row=0)

style = tk.Style()
style.configure("Treeview", font=("Poppins", 12), rowheight=30)
style.configure("Treeview.Heading", font=("Poppins", 12, "bold"))

bar = Scrollbar(frame, orient="vertical")
bar.grid(column=1, row=0, sticky="NSW")

table = tk.Treeview(frame, yscrollcommand=bar.set)
table.grid(column=0, row=0)

bar.config(command=table.yview)

table["columns"] = ("Class", "Course", "Time")
table.column("#0", width=0, stretch=NO)
table.column("Class", anchor=CENTER, width=100, stretch=NO)
table.column("Course", anchor=CENTER, width=150, stretch=NO)
table.column("Time", anchor=CENTER, width=200, stretch=NO)

table.heading("#0", text="", anchor=CENTER)
table.heading("Class", text="Class", anchor=CENTER)
table.heading("Course", text="Course", anchor=CENTER)
table.heading("Time", text="Time", anchor=CENTER)

for i in range(50):
    table.insert(parent="", index="end", iid=i, text="", values=(f"AA0{i}", "Artificial Inteligence", "Monday 09.20-13.00"))
# table.column("Class", "AA01")
# table.column("Course", "Artificial Inteligence")
# table.column("Time", "09.20-13.00")

main_window.mainloop()

# AA01 Artificial Inteligence Monday 09.20-13.00