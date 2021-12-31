from tkinter import *
import json
import tkinter.ttk as tk

BLACK = "#1C2626"
WHITE = "#FFFFFF"
RED = "#FF0000"
PURPLE = "#552D96"
GREEN = "#00FF00"
GRAY = "#C4C4C4"
FONT = "Poppins"

class ViewClassInfo:
    def __init__(self, main_window, class_code):
        self.main_window = main_window
        self.class_code = class_code
        self.search_text = StringVar()
        self.search = ""

        with open("../data/class_student.json", mode="r") as file:
            self.info_dict = json.load(file)
        
        self.info_dict = self.info_dict[f"{self.class_code}"]
    
    def search_class(self, *event):
        query = str(self.search)
        selections = []
        for child in self.schedule_table.get_children():
            if query in self.schedule_table.item(child)["values"]:
                selections.append(child)

        self.schedule_table.selection_set(selections)

    def callback_manage_class(self, *args):
        self.search = str(self.search_text.get())

    def vcmd_manage_class(self):
        self.search_text.trace_add("write", callback=self.callback_manage_class)

    def click_search(self, *args):
        if str(self.search_text.get()) == "Search...":
            self.search_text.set("")

    def leave_search(self, *args):
        if str(self.search_text.get()) == "":
            self.search_text.set("Search...")

    def to_manage_schedule(self):
        from manage_class import ManageClass
        mc = ManageClass(self.main_window)
        mc.manage_class()

    def view_class_info(self):
        # --------------- reset page
        for widget in self.main_window.winfo_children():
            widget.destroy()

        info_frame = Frame(self.main_window, bg=BLACK)
        info_frame.grid(column=0, row=0)

        # --------------- title
        manage_class_label = Label(info_frame, text=f"MANAGE CLASS {self.class_code}", fg=WHITE, bg=BLACK, font=(FONT, 35, "bold"))
        manage_class_label.grid(column=0, row=0, columnspan=4, pady=(0, 50))

        # --------------- class info
        class_info_label = Label(info_frame, text=f"CLASS INFO:", fg=WHITE, bg=BLACK, font=(FONT, 12))
        class_info_label.grid(column=0, row=1, sticky="W", pady=(0, 20))
        
        # --------------- course name
        course_name_label = Label(info_frame, text=f"Course Name:", fg=WHITE, bg=BLACK, font=(FONT, 10))
        course_name_label.grid(column=0, row=2, sticky="W", pady=(0, 20))

        course_name = self.info_dict["Subject"]
        show_course_name = Label(info_frame, text=f"{course_name}", fg=WHITE, bg=BLACK, font=(FONT, 10))
        show_course_name.grid(column=1, row=2, pady=(0, 20), sticky="W")

        # --------------- lecture name
        lec_name_label = Label(info_frame, text=f"Lecturer Name:", fg=WHITE, bg=BLACK, font=(FONT, 10))
        lec_name_label.grid(column=0, row=3, sticky="W", pady=(0, 20))

        lec_name = self.info_dict["Lecturer"]
        show_lec_name = Label(info_frame, text=f"{lec_name}", fg=WHITE, bg=BLACK, font=(FONT, 10))
        show_lec_name.grid(column=1, row=3, pady=(0, 20), sticky="W")

        # --------------- time label
        time_label = Label(info_frame, text=f"Time:", fg=WHITE, bg=BLACK, font=(FONT, 10))
        time_label.grid(column=0, row=4, sticky="W", pady=(0, 20))

        time_name = self.info_dict["Time"]
        show_time_name = Label(info_frame, text=f"{time_name}", fg=WHITE, bg=BLACK, font=(FONT, 10))
        show_time_name.grid(column=1, row=4, pady=(0, 20), sticky="W")

        # --------------- total student
        total_student_label = Label(info_frame, text=f"Total Student:", fg=WHITE, bg=BLACK, font=(FONT, 10))
        total_student_label.grid(column=0, row=5, sticky="W", pady=(0, 20))

        total_student = len(self.info_dict["StudentNIM"])
        show_time_name = Label(info_frame, text=f"{total_student}", fg=WHITE, bg=BLACK, font=(FONT, 10))
        show_time_name.grid(column=1, row=5, pady=(0, 20), sticky="W")

        # --------------- search
        search_bar = Entry(info_frame, width=60, validate="focusin", validatecommand=self.vcmd_manage_class, textvariable=self.search_text)
        self.search_text.set("Search...")
        search_bar.bind("<FocusIn>", self.click_search)
        search_bar.bind("<FocusOut>", self.leave_search)
        search_bar.configure(background=GRAY, fg=BLACK, font=(FONT, 16))
        search_bar.grid(column=2, row=1)

        self.main_window.bind("<Return>", self.search_class)

        # --------------- table page
        table_style = tk.Style()
        table_style.configure("Treeview", font=("Poppins", 12), rowheight=30)
        table_style.configure("Treeview.Heading", font=("Poppins", 12, "bold"))

        scrollbar = Scrollbar(info_frame, orient="vertical")
        scrollbar.grid(column=3, row=1, sticky="NSW")

        self.schedule_table = tk.Treeview(info_frame, yscrollcommand=scrollbar.set)
        self.schedule_table.grid(column=2, row=1, sticky="W")

        scrollbar.config(command=self.schedule_table.yview)

        self.schedule_table["columns"] = ("Name", "Student ID")
        self.schedule_table.column("#0", width=0, stretch=NO)
        self.schedule_table.column("Name", anchor=CENTER, width=50, stretch=NO)
        self.schedule_table.column("Student ID", anchor=CENTER, width=50, stretch=NO)

        self.schedule_table.heading("#0", text="", anchor=CENTER)
        self.schedule_table.heading("Name", text="Class", anchor=CENTER)
        self.schedule_table.heading("Student ID", text="Course", anchor=CENTER)

        # self.schedule_table.bind("<Double-Button-1>", self.class_info)

        # counter = 0
        # for class_code in self.info_dict:
        #     student = self.info_dict[""]

        # # --------------- back button
        # back_button = Button(info_frame, text="Back", command=self.to_manage_schedule, width=14, height=1)
        # back_button.configure(background=BLACK, fg=WHITE, font=(FONT, 12, "bold"))
        # back_button.grid(column=0, row=3, pady=20, sticky="W")

        # # --------------- add class button
        # add_class_button = Button(info_frame, text="Add New", command="", width=14, height=1)
        # add_class_button.configure(background=PURPLE, fg=WHITE, font=(FONT, 12, "bold"))
        # add_class_button.grid(column=1, row=3, pady=20, sticky="E")