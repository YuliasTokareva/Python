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



def main():
    bank = Bank

    print("Приветствуем в нашем банке!")
    name = input("Для регистрации введите ваше имя:")
    client = Bank.register_account(name)
    print(f"Поздравляем! Вы зарегистрированы. Ваш ID: {client.username_id}\n")
    while True:
        print("\n Доступные операции")
        print("1. Открыть новый счет.")
        print("2. Закрыть текущий счет.")
        print("3. Пополнить текущий счет.")
        print("4. Снять наличные.")
        print("5. Перевод средств на другой счет.")
        print("6. Получить выписку по текушему счету.")
        print("0. Выйти.")

        choice = input("Выберите операцию: ").strip()



