from Tkinter import *


class Box:
    def __init__(self, data):
        self.data = data
        root.title('Quiz 5')

    def bubble_sort(self):
        for index in range(1, len(self.data)):
            for j in range(0, len(self.data) - 1):
                if data[j] < data[j + 1]:

                    tmp = data[j]
                    data[j] = data[j + 1]
                    data[j + 1] = tmp

        return data

    def unsorted(self):
        Label(text="Data Sebelum Di urutkan : ").pack()
        for i in range(len(data)):
            boxes_one.insert(i + 1, data[i])
        boxes_one.pack()

    def sorted(self):
        Label(text="Data Sesudah Di Urutkan : ").pack()
        for j in range(len(data)):
            boxes_two.insert(j, listbox.bubble_sort()[j])
        boxes_two.pack()


root = Tk()
root.geometry("700x450")
data = [25, 57, 48, 100]

mainlabel = Label(root, text="BUBBLE SORT MENURUN", font="ROBOTO 20 bold", anchor=CENTER).pack()

boxes_one = Listbox(height=10, width=50)
boxes_two = Listbox(height=10, width=50)

listbox = Box(data)
listbox.unsorted()
listbox.sorted()

mainloop()
