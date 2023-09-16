'''Implement  a class called bankAccount that represent  a backaccount. the class should have private
attributes for accounts number,account holder name,and account balance. include methods to
deposit money,withdraw money, and display the accountbalance.ensure that the account balance
cannot be accessed  directly from outside the class.write a program to crate an instance of the 
bankaccount class and test the deposit and withdraw functionality.'''


class BankAccount:

  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name =account_holder_name
    self.__account_balance = initial_balance

  def deposit (self, amount):
    if amount > 0:
        self.__account_balance += amount
     #self.__account_balance = self.__account_balance+amount
        print("Deposited ₹{}. New balance: ₹{}".format(amount,
      self.__account_balance))
    else:
        print("invalid deposit amount.")
   
  def withdraw(self,amount):
    if amount > 0 and amount <= self.__account_balance:
     self.__account_balance -= amount
   #self.__ account_balance = self.__account_balance+amount
     print("withdraw ₹{}.New balance: ₹{}".format(amount,
        self.__account_balance))
    else:
       print("invalid withdraw amount or insufficient balance.")

  def display_balance(self):
   print("account balance for {} Account #{}): ₹{}".format(
self.__account_holder_name,self.__account_number,
        self.__account_balance))


#create an instance of the bankaccount class name
account = BankAccount(account_number="123456789",
account_holder_name="mahesh",
initial_balance=5000.0)

#test deposit and withdraw functionality 
account. display_balance()
account. deposit(500.0)
account. withdraw (200.0)
account. withdraw (20000.0)
account. display_balance()