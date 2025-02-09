
from tkinter import Frame, Button, Text, Entry, Label, messagebox
from tkinter.ttk import Combobox

from Circle import Circle
from Rectangle import Rectangle
from Cylinder import Cylinder

class TaskGui:
    def __init__(self, main):
        self.main = main
        main.title("Task GUI") # võib ka ilma self. antud  versioonis
        self.main.geometry("500x300")


        #Frame
        self.frame = Frame(self.main, background= 'lightgreen')
        self.frame.pack(fill='both', expand=True)

        #Combobox
        self.cmb = Combobox(self.frame, values=("Vali kujund", "Ring", "Ristkülik", "Silinder"))
        self.cmb.current(0)
        self.cmb['state']='readonly'
        self.cmb.grid(row=0, column=0, padx=3, pady=3   , columnspan=2 ,sticky='ew')

        #ujuvad vidinad(ring, ristkülik ja silinder)
        self.lbl_circle, self.txt_circle = self.creat_circle_widget()
        self.lbl_a, self.lbl_b, self.txt_a, self.txt_b = self.create_rectangle_widget()
        self.lbl_height, self.lbl_radius, self.txt_height, self.txt_radius = self.create_cylinder_widget()


        self.btn_submit = self.create_button()
        #Creat result Text
        self.result =self.create_result()

        #Peidame ringi, ristküliku ja silindri asjad
        self.forget_circle()
        self.forget_rectangle()# Peida ristkülik
        self.forget_cylinder()

        #kuula comboboxi muutusi
        self.cmb.bind('<<ComboboxSelected>>', self.changed)
        self.main.bind('<Return>', lambda event=None: self.calculate())

    def create_button(self):
        button =Button(self.frame, text='Näita', command=lambda: self.calculate())
        button['state'] ='disabled'
        button.grid(row=3, column=0, padx=3, pady=2,columnspan=2, sticky='ew')
        return button

    def create_result(self):
        result = Text(self.frame, height=5, width=25)
        result.grid(row=4, column=0, padx=3, pady=2,columnspan=2, sticky='ew')
        result['state']='disabled'
        return result

    def creat_circle_widget(self):
        label =Label(self.frame,text="Raadius")
        label.grid(row=1, column=0, padx=3, pady=3, sticky='ew')

        text =Entry(self.frame,width=12)
        text.focus()
        text.grid(row=1, column=1, padx=3, pady=3, sticky='ew')
        return label,text

    def create_rectangle_widget(self):
        label_a = Label(self.frame,text="Külg a")
        label_a.grid(row=1, column=0, padx=3, pady=3, sticky='ew')

        text_a = Entry(self.frame,width=12)
        text_a.grid(row=1, column=1, padx=3, pady=3, sticky='ew')
        text_a.focus()

        label_b =Label(self.frame, text='Külg b')
        label_b.grid(row=2, column=0, padx=3, pady=3, sticky='ew')

        text_b = Entry(self.frame, width=12)
        text_b.grid(row=2, column=1, padx=3, pady=3, sticky='ew')

        return label_a,label_b,text_a,text_b

    def create_cylinder_widget(self):
        label_height=Label(self.frame,text="Kõrgus")
        label_height.grid(row=1, column=0, padx=3, pady=3, sticky='ew')

        text_height=Entry(self.frame,width=12)
        text_height.grid(row=1, column=1, padx=3, pady=3, sticky='ew')
        text_height.focus()

        label_radius=Label(self.frame, text="Raadius")
        label_radius.grid(row=2, column=0, padx=3, pady=3, sticky='ew')

        text_radius = Entry(self.frame, width=12)
        text_radius.grid(row=2, column=1, padx=3, pady=3, sticky='ew')
        text_radius.focus()
        return label_height,label_radius,text_height,text_radius


    def forget_circle(self):
        self.lbl_circle.grid_forget()
        self.txt_circle.grid_forget()
        self.btn_submit['state']='disabled' #nuppu ei saa klikkida

    def forget_rectangle(self):
        self.lbl_a.grid_forget()
        self.lbl_b.grid_forget()
        self.txt_a.grid_forget()
        self.txt_b.grid_forget()
        self.btn_submit['state']='disabled'

    def forget_cylinder(self):
        self.lbl_height.grid_forget()
        self.lbl_radius.grid_forget()
        self.txt_height.grid_forget()
        self.txt_radius.grid_forget()
        self.btn_submit['state']='disabled'


    def changed(self, event=None):
        combo_index = self.cmb.current() #mitmes valik comboboxist (0,1,2)

        if combo_index == 0:
            self.forget_circle()
            self.forget_rectangle()
            self.forget_cylinder()
            self.btn_submit['state']='normal'

        elif combo_index == 1:
            self.lbl_circle, self.txt_circle = self.creat_circle_widget()
            self.forget_rectangle()
            self.forget_cylinder()
            self.btn_submit['state']='normal'
        elif combo_index == 2:
            self.lbl_a, self.lbl_b, self.txt_a, self.txt_b = self.create_rectangle_widget()
            self.forget_circle()
            self.forget_cylinder()
            self.btn_submit['state']='normal'
        elif combo_index == 3:  # Silinder
            self.forget_circle()
            self.forget_rectangle()
            self.lbl_height, self.lbl_radius, self.txt_height, self.txt_radius = self.create_cylinder_widget()
            self.btn_submit['state'] = 'normal'

        self.clear_result()

    def clear_result(self):
        self.result.config(state='normal')
        self.result.delete('1.0', 'end')
        self.result.config(state='disabled')

    def calculate(self):
        cmb_index = self.cmb.current()
        if cmb_index == 1:
            try:
                radius=float(self.txt_circle.get().strip())
                circle = Circle(radius) #loo objekt Ring
                self.clear_result()
                self.result.config(state='normal') #vastuse lisamisks
                self.result.insert('1.0',str(circle))#täis vastus classis circle
                self.result.config(state='disabled')

            except ValueError:
                messagebox.showerror("Viga", "Raadius peab olema number.")

            self.txt_circle.delete(0, 'end')#Tühjenda raadiuse kast
            self.txt_circle.focus()

        elif cmb_index == 2:
            try:
                width = float(self.txt_a.get().strip())
                hight = float(self.txt_b.get().strip())
                rectangle = Rectangle(width, hight)
                self.clear_result()
                self.result.config(state='normal')
                self.result.insert('1.0',str(rectangle))
                self.result.config(state='disabled')
            except ValueError:
                messagebox.showerror("Viga", "Külg peab olema number.")

            self.txt_a.delete(0, 'end')
            self.txt_b.delete(0, 'end')
            self.txt_a.focus()

        elif cmb_index == 3:  # Silinder
            try:
                radius = float(self.txt_radius.get().strip())
                height = float(self.txt_height.get().strip())
                cylinder = Cylinder(radius, height)

                self.clear_result()
                self.result.config(state='normal')
                self.result.insert('1.0', f"Ruumala: {cylinder.volume()}\n")
                self.result.insert('end', f"Põhjapindala: {cylinder.base_area()}\n")
                self.result.insert('end', f"Külgpindala: {cylinder.lateral_area()}\n")
                self.result.insert('end', f"Kogu pindala: {cylinder.total_area()}\n")
                self.result.config(state='disabled')

            except ValueError:
                messagebox.showerror("Viga", " Külg peab olema number")

            self.txt_a.delete(0, 'end') #Tühjenda külg a kast
            self.txt_b.delete(0, 'end') #Tühjenda külg b kast
            self.txt_a.focus()


