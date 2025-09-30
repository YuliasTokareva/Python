class Client:
    def __init__(self):
        self.accounts = []

    def logout(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        self.username = username
        self.password = password

    def addAccount(self, account):
        self.accounts.append(account)
    def removeAccount(self, account):
        self.accounts.remove(account)





class BankAccount:
    def __init__(self, client, volute):
        self.client = client
        self.volute = volute
        self.balance = 0.0
