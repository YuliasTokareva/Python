# Собственные исключения
class BankError(Exception):
    """Ошибка: Базовое исключение для всех ошибок банка."""
    pass

class ClientNotFoundError(BankError):
    """Ошибка: Клиент с указанным ID не найден."""
    pass

class AccountNotFoundError(BankError):
    """Ошибка: Счёт с указанным номером не найден."""
    pass

class InsufficientFundsError(BankError):
    """Ошибка: Недостаточно средств на счёте для операции."""
    pass

class InvalidAmountError(BankError):
    """Ошибка: Сумма операции введена неверно."""
    pass

class AccountExistsError(BankError):
    """Ошибка: Счёт в указанной валюте уже существует у клиента."""
    pass

class CurrencyMismatchError(BankError):
    """Ошибка: Попытка перевода между счетами с разными валютами."""
    pass

class AccountOwnershipError(BankError):
    """Ошибка: Попытка выполнить операцию над чужим счётом."""
    pass

class CannotCloseAccountWithBalanceError(BankError):
    """Ошибка: Нельзя закрыть счёт, на котором есть деньги."""
    pass

class InvalidCurrencyError(BankError):
    """Ошибка: Указана недопустимая валюта."""
    pass

class Client:
    def __init__(self, client_id, username):
        self.client_id = client_id
        self.username = username
        self.accounts = []

    def open_account(self, volute):
        print(f"Попытка открыть счёт в валюте {volute} для клиента {self.username}")
        for acc in self.accounts:
            if acc.volute == volute:
                print(f"Ошибка: счёт в валюте {volute} уже существует у клиента {self.username}")
                return False
        new_acc = BankAccount(volute, self)
        self.accounts.append(new_acc)
        print(f"Поздравляем! счёт в валюте {volute} открыт для клиента {self.username}")
        return True

    def close_account(self, volute):
        print(f"Попытка закрыть счёт в валюте {volute} для клиента {self.username}")
        i = 0
        while i < len(self.accounts):
            if self.accounts[i].volute == volute:
                del self.accounts[i]
                print(f"Счёт в валюте {volute} закрыт для клиента {self.username}")
                return True
            i = i + 1
        print(f"Ошибка: счёт в валюте {volute} не найден у клиента {self.username}")
        return False

    def has_accounts(self):
        if len(self.accounts) == 0:
            print(f"Проверка: у клиента {self.username} нет счетов")
            return False
        else:
            print(f"Проверка: у клиента {self.username} есть счета")
            return True

    def total_accounts(self):
        count = len(self.accounts)
        print(f"Запрос: общее количество счетов у клиента {self.username} = {count}")
        return count

    def count_currencies(self):
        currencies = []
        print(f"Подсчёт количества валют для клиента {self.username}")
        for acc in self.accounts:
            already_have = False
            for c in currencies:
                if c == acc.volute:
                    already_have = True
            if not already_have:
                currencies.append(acc.volute)
                print(f"  Найдена новая валюта: {acc.volute}")
        total = len(currencies)
        print(f"Итого валют у клиента {self.username}: {total}")
        return total

    def get_statement(self):
        if len(self.accounts) == 0:
            message = f"У клиента {self.username} (ID: {self.client_id}) нет счетов."
            print(f"Выписка: {message}")
            return message

class BankAccount:
    def __init__(self, client, volute):
        self.client = client
        self.volute = volute
        self.balance = 0.0
        print(f"Создан новый счёт в валюте {self.volute} для клиента {self.client.name}")

    def deposit(self, amount):
        if amount <= 0:
            print(f"Ошибка: попытка пополнить на {amount}. Сумма должна быть положительной.")
            return False
        old_balance = self.balance
        self.balance = self.balance + amount
        print(f"Счёт в {self.volute}: пополнение на {amount}. Баланс изменён с {old_balance:.2f} на {self.balance:.2f}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print(f"Ошибка: попытка снять {amount}. Сумма должна быть положительной.")
            return False
        if amount > self.balance:
            print(f"Ошибка: недостаточно средств. Попытка снять {amount}, но баланс всего {self.balance:.2f}")
            return False
        old_balance = self.balance
        self.balance = self.balance - amount
        print(f"Счёт в {self.volute}: снято {amount}. Баланс изменён с {old_balance:.2f} на {self.balance:.2f}")
        return True

    def can_withdraw(self, amount):
        if amount <= 0:
            print(f"Проверка снятия: сумма {amount} недопустима (должна быть > 0)")
            return False
        if amount > self.balance:
            print(f"Проверка снятия: недостаточно средств для снятия {amount} (баланс: {self.balance:.2f})")
            return False
        print(f"Проверка снятия: можно снять {amount} из счёта в {self.volute}")
        return True

    def get_balance(self):
        print(f"Запрос баланса для счёта в {self.volute}: {self.balance:.2f}")
        return self.balance

    def get_volute(self):
        print(f"Запрос валюты счёта: {self.volute}")
        return self.volute

    def get_info(self):
        info = f"Счёт в {self.volute}, баланс: {self.balance:.2f}"
        print(f"Получена информация о счёте: {info}")
        return info

    def is_same_volute(self, other_account):
        if other_account is None:
            print("Ошибка: второй счёт не существует")
            return False
        if self.volute == other_account.currency:
            print(f"Валюты совпадают: {self.volute} == {other_account.volute}")
            return True
        else:
            print(f"Валюты не совпадают: {self.volute} != {other_account.volute}")
            return False

class Bank:
    def __init__(self, clients=None):
        self.clients = clients if clients is not None else {}
        print("Банк создан")

    def register_client(self, username):
        next_id = len(self.clients) + 1
        client_id = f"C{next_id}"
        new_client = Client(client_id, username)
        self.clients[client_id] = new_client
        print(f"Клиент {username} зарегистрирован с ID {client_id}")
        return client_id

    def get_client(self, client_id):
        if client_id in self.clients:
            print(f"Клиент {client_id} найден")
            return self.clients[client_id]
        else:
            print(f"Клиент {client_id} не найден")
            return None

    def open_account_for_client(self, client_id, volute):
        client = self.get_client(client_id)
        if client is None:
            print("Невозможно открыть счёт: клиент не найден")
            return False
        result = client.open_account(volute)
        if result:
            print(f"Счёт в валюте {volute} открыт для клиента {client_id}")
        else:
            print(f"Не удалось открыть счёт в валюте {volute} для клиента {client_id}")
        return result

    def close_account_for_client(self, client_id, volute):
        client = self.get_client(client_id)
        if client is None:
            print("Невозможно закрыть счёт: клиент не найден")
            return False
        result = client.close_account(volute)
        if result:
            print(f"Счёт в валюте {volute} закрыт для клиента {client_id}")
        else:
            print(f"Не удалось закрыть счёт в валюте {volute} для клиента {client_id}")
        return result

    def deposit_to_account(self, client_id, volute, amount):
        client = self.get_client(client_id)
        if client is None:
            print("Пополнение отменено: клиент не найден")
            return False
        account = client.find_my_account(volute)
        if account is None:
            print(f"У клиента {client_id} нет счёта в валюте {volute}")
            return False
        result = account.deposit(amount)
        if result:
            print(f"Счёт пополнен на {amount} {volute}")
        else:
            print("Ошибка при пополнении: сумма должна быть положительной")
        return result

    def withdraw_from_account(self, client_id, volute, amount):
        client = self.get_client(client_id)
        if client is None:
            print("Снятие отменено: клиент не найден")
            return False
        account = client.find_my_account(volute)
        if account is None:
            print(f"У клиента {client_id} нет счёта в валюте {volute}")
            return False
        result = account.withdraw(amount)
        if result:
            print(f"Снято {amount} {volute} со счёта")
        else:
            print("Недостаточно средств или неверная сумма")
        return result

    def transfer_between_clients(self, from_client_id, from_volute, to_client_id, to_volute, amount):
        print("Начало перевода между клиентами")
        from_client = self.get_client(from_client_id)
        to_client = self.get_client(to_client_id)
        if from_client is None or to_client is None:
            print("Перевод отменён: клиент не найден")
            return False
        from_account = from_client.find_my_account(from_volute)
        to_account = to_client.find_my_account(to_volute)
        if from_account is None or to_account is None:
            print("Перевод отменён: счёт не найден")
            return False
        if from_account.volute != to_account.volute:
            print("Перевод отменён: валюты не совпадают")
            return False
        if not from_account.can_withdraw(amount):
            print("Перевод отменён: недостаточно средств")
            return False
        from_account.withdraw(amount)
        to_account.deposit(amount)
        print(f"Перевод выполнен: {amount} {from_account.volute}")
        return True

    def get_statement_for_client(self, client_id):
        client = self.get_client(client_id)
        if client is None:
            print("Выписка невозможна: клиент не найден")
            return "Клиент не найден"
        statement = client.get_statement()
        print("Выписка сформирована")
        return statement


def main():
    bank = Bank()
    print("Добро пожаловать в банк!")

    while True:
        print("\n--- Главное меню ---")
        print("1. Зарегистрировать нового клиента")
        print("2. Войти в систему")
        print("3. Выйти из системы")

        choice = input("Введите номер операции: ")

        if choice == "1":
            username = input("Введите имя клиента: ")
            client_id = bank.register_client(username)
            print(f"Клиент зарегистрирован. Ваш ID: {client_id}")

        elif choice == "2":
            client_id = input("Введите ваш ID: ")
            client = bank.get_client(client_id)
            if client is None:
                print("Ошибка: клиент с таким ID не найден")
            else:
                print(f"Здравствуйте, {client.username}!")
                while True:
                    print("\n--- Личный кабинет ---")
                    print("1. Открыть счёт")
                    print("2. Закрыть счёт")
                    print("3. Пополнить счёт")
                    print("4. Снять деньги")
                    print("5. Перевести деньги другому клиенту")
                    print("6. Получить выписку")
                    print("7. Назад в главное меню")

                    action = input("Выберите операцию: ")

                    if action == "1":
                        volute = input("Введите валюту счёта (например, RUB): ")
                        bank.open_account_for_client(client_id, volute)

                    elif action == "2":
                        volute = input("Введите валюту счёта для закрытия: ")
                        bank.close_account_for_client(client_id, volute)

                    elif action == "3":
                        volute = input("Введите валюту счёта: ")
                        amount_str = input("Введите сумму для пополнения: ")
                        try:
                            amount = float(amount_str)
                            bank.deposit_to_account(client_id, volute, amount)
                        except ValueError:
                            print("Ошибка: сумма должна быть числом")

                    elif action == "4":
                        volute = input("Введите валюту счёта: ")
                        amount_str = input("Введите сумму для снятия: ")
                        try:
                            amount = float(amount_str)
                            bank.withdraw_from_account(client_id, volute, amount)
                        except ValueError:
                            print("Ошибка: сумма должна быть числом")

                    elif action == "5":
                        from_volute = input("Валюта вашего счёта: ")
                        to_client_id = input("ID получателя: ")
                        to_volute = input("Валюта счёта получателя: ")
                        amount_str = input("Сумма перевода: ")
                        try:
                            amount = float(amount_str)
                            bank.transfer_between_clients(client_id, from_volute, to_client_id, to_volute, amount)
                        except ValueError:
                            print("Ошибка: сумма должна быть числом")

                    elif action == "6":
                        statement = bank.get_statement_for_client(client_id)
                        print("\n" + statement)

                    elif action == "7":
                        print("Выход из личного кабинета...")
                        break

                    else:
                        print("Неверный выбор, попробуйте снова")

        elif choice == "3":
            print("Спасибо за использование банка! До свидания!")
            break

        else:
            print("Неверный выбор, попробуйте снова")

 if __name__ == "__main__":
     main()
