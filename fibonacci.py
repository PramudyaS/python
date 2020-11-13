class Fibonacci:
    def __init__(self,row_count):
        self.row_count = int(row_count)
        self.list = [1, 1]

        if self.row_count > 1:
            for index in range(2, self.row_count):
                self.list.append(self.list[index - 1] + self.list[index - 2])

    def result(self):
        print('Hasil :')

        for index in range(len(self.list)):
            print(str(self.list[index]), end=",")


row_selected = input("Masukan Batas Deret : ")
action = Fibonacci(row_selected)
action.result()
