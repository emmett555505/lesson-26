class IOString():

    def __init__(self):
        self.str1=""

    def get_string(self):
        self.str1 = input("enter string : ")

    def print_string(self):
        print("result is :", self.str1.upper())

stri = IOString()

stri.get_string()
stri.print_string()