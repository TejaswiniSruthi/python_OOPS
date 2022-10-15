class Customer:
    ifsc='IDFB4567'
    def __init__(self,name):
        self.name=name
        self.acc='20P31A1233'
        
class Employee(Customer):
    def __init__(self,name):
        self.bal=10000
        self.pin=123
        super().__init__(name)
    def display(self):
        print(' Name: ',self.name,'\n','Account Number: ',self.acc,'\n',
              'IFSC: ',self.ifsc,'\n','Account Balance: ',self.bal,'\n',)
    def deposit(self):
        amount=int(input('Enter the amount to deposit: '))
        self.bal+=amount
        print('Your account XXXX543 is credited with ',amount,' rupees\n')
        
    def withdrawal(self):
        amount=int(input('Enter the amount to withdraw: '))
        if(self.bal>=amount):
            self.bal-=amount
            print('Your account XXXX543 is debited with ',amount,' rupees\n')
        else:
            print("Insufficient Balance!\n")
    def change_pin(self):
        
        ppin=int(input('Enter you pin to change the pin: \n'))
        if(ppin==self.pin):
            ppin=int(input('Enter your new pin: '))
            self.pin=ppin
            print('Your new pin: ',self.pin)
    def view_pin(self):
        if(self.pin==123):
            print('Your current Pin : ',self.pin,'\n')
        else:
            print('Your current Pin : ',self.pin,'\n')
    def view(self):
        while(True):
            s=int(input('Enter 1 to deposit the Money\nEnter 2 to withdraw your Money\nEnter 3 to change pin\nEnter 4 to view pin\nEnter 5 to display your information\nEnter 6 to Exit our services\n'))
            if(s==1):
                e.deposit()
            elif(s==2):
                e.withdrawal()
            elif(s==3):
                e.change_pin()
            elif(s==4):
                e.view_pin()
            elif(s==5):
                e.display()
            elif(s==6):
                print('Thank You! Visit us again!')
                break
e=Employee('Tejaswini Thambabathula')
e.view()


