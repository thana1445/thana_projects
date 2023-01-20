class ATM:
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance

  def check_balance(self):
    print(f"Account: {self.name} Balance: {self.balance}")
    #print(message)

  def desposit(self, money):
    self.balance += money
    print("Deposit Successfully")
    print(f"New Balance: {self.balance}")

  def change_acc_name(self, new_acc_name):
    self.name = new_acc_name
    print('Your account name has been changed.')
    print(f"New Account Name: {self.name}")

  def withdraw(self, money_2):
    self.balance -= money_2
    print("Withdraw Successfully")
    print(f"New Balance: {self.balance}")

  def statement(self, month, mail):
    self.month = month
    self.mail = mail
    print(f"The statement has been send to your e-mali({self.mail}), please check !")