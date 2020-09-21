from Tkinter import *


class MyGroup:
    def __init__(self, group_name, list_member):
        self.group_name = group_name
        self.list_member = list_member
        root.title("Test")

    def header(self):
        Label(root, text=self.group_name, font="ROBOTO 20 bold", anchor=CENTER).pack()

    def member(self):
        for index, val in enumerate(self.list_member):
            txt = str(index + 1) + ". " + val
            Label(root, text=txt, anchor=CENTER, font="HEVALTICA 12").pack()

    def app(self):
        self.header()
        self.member()


root = Tk()
root.geometry("700x450")
member_list = ['Pramudya Saputra', 'Pram Grizie', 'Almighty Pram']
group = MyGroup('Kelompok XVII : ', member_list)

group.app()
mainloop()
