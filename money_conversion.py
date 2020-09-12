def getInput(message):
    while True:
        try:
            userInput = int(raw_input(message))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput


class Conversion:
    kurs = 15000

    def __init__(self,amount):
        self.amount = float(amount)

    def rupiahToDollar(self):
        calculate = self.amount / self.kurs
        return calculate

    def dollarToRupiah(self):
        calculate = self.amount * self.kurs
        return calculate

class ShowMenu:
    def __init__(self):
        print "-------  Menu Conversion ---------"
        print "[1] Rupiah To Dollar "
        print "[2] Dollar To Rupiah"

        menu = input("Select Menu : ")
        print "\n"

        self.amount = getInput("Input Amount : ")
        print "\n"

        if menu == 1:
            total = Conversion(self.amount)
            print "Total Conversion : $" + str(total.rupiahToDollar())
        elif menu == 2:
            total = Conversion(self.amount)
            print "Total Conversion : Rp." + str(total.dollarToRupiah())
        else:
            print "Menu Doesn't Exist"

conversion = ShowMenu()