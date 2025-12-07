class InsufficientFundsError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class ClientNotFoundError(Exception):
    pass

class AccountNotFoundError(Exception):
    pass

class AccountExistsError(Exception):
    pass
class AccountOwnershipError(Exception):
    pass

class BankAccount:
    def __init__(self, owner, currency):
        self.owner = owner
        self.currency = currency
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError()
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError()
        if amount > self.balance:
            raise InsufficientFundsError()
        self.balance -= amount


class Client:
    def __init__(self, client_id, name):
        self.client_id = client_id
        self.name = name
        self.secret_word = name
        self.accounts = {}

    def open_account(self, currency):
        if currency in self.accounts:
            raise AccountExistsError(f"Счет в волюте {currency} уже существует.")
        self.accounts[currency] = BankAccount(self, currency)

    def get_account(self, currency):
        if currency not in self.accounts:
            raise AccountNotFoundError()
        return self.accounts[currency]

    def close_account(self, currency):
        if currency not in self.accounts:
            raise AccountNotFoundError()
        del self.accounts[currency]

    def has_accounts(self):
        return len(self.accounts) > 0


class Bank:
    def __init__(self):
        self.clients = {}
        self.next_client_id = 1

    def register_client(self, name):
        client_id = f"C{self.next_client_id}"
        self.clients[client_id] = Client(client_id, name)
        self.next_client_id += 1
        return client_id

    def get_client(self, client_id):
        if client_id not in self.clients:
            raise ClientNotFoundError()
        return self.clients[client_id]

    def open_account(self, client_id, currency):
        client = self.get_client(client_id)
        client.open_account(currency)

    def close_account(self, client_id, currency):
        client = self.get_client(client_id)
        client.close_account(currency)

    def deposit(self, client_id, currency, amount):
        client = self.get_client(client_id)
        account = client.get_account(currency)
        account.deposit(amount)

    def withdraw(self, client_id, currency, amount):
        client = self.get_client(client_id)
        account = client.get_account(currency)
        account.withdraw(amount)

    def transfer(self, from_id, from_curr, to_id, to_curr, amount):
        if from_curr != to_curr:
            raise AccountNotFoundError("Валюты должны совпадать")
        from_client = self.get_client(from_id)
        to_client = self.get_client(to_id)
        from_account = from_client.get_account(from_curr)
        to_account = to_client.get_account(to_curr)
        if from_account.owner.client_id != from_id:
            raise AccountOwnershipError("Нельзя перевести деньги с чужого счета.")
        from_account.withdraw(amount)
        to_account.deposit(amount)

    def get_user_statement(self, client_id):
        client = self.get_client(client_id)
        lines = [f"Выписка по клиенту {client.name} (ID: {client_id})"]
        if not client.accounts:
            lines.append("У вас нет счетов.")
        else:
            for curr, acc in client.accounts.items():
                lines.append(f"- Счёт в {curr}: {acc.balance:.2f}\n")
                lines.append("\n(Балансы в разных валютах не суммируются)\n")
        return "\n".join(lines)

def verify_secret(client):
    attempt = input("Введите кодовое слово для подтверждения операции: ").strip()
    if attempt == client.secret_word:
        return True
    else:
        print("Нкверное кодовое слово! Операция отменена.")
        return False

def main():

    bank = Bank()
    print("Добро пожаловать в Банк!")

    while True:
        print("\n" + "="*50)
        print("ГЛАВНОЕ МЕНЮ")
        print("="*50)
        print("1. Зарегистрировать нового клиента")
        print("2. Войти в систему")
        print("3. Выйти из программы")
        choice = input("\nВыберите действие (1/2/3): ").strip()

        if choice == "1":
            name = input("Введите ваше полное имя: ").strip()
            if name:
                client_id = bank.register_client(name)
                print(f"\nУспешно! Клиент '{name}' зарегистрирован.")
                print(f"Ваш ID для входа: {client_id}")
                print("Запомните этот ID — он понадобится для входа в систему.")
            else:
                print("Ошибка: имя не может быть пустым.")

        elif choice == "2":
            client_id = input("Введите ваш ID для входа: ").strip()
            try:
                client = bank.get_client(client_id)
                print(f"\nДобро пожаловать, {client.name}!")
                print(f"Ваш ID: {client.client_id}")

                while True:
                    print("\n" + "-"*50)
                    print("ЛИЧНЫЙ КАБИНЕТ")
                    print("-"*50)
                    print("1. Открыть новый счёт")
                    print("2. Закрыть существующий счёт")
                    print("3. Пополнить счёт")
                    print("4. Снять деньги со счёта")
                    print("5. Перевести деньги другому клиенту")
                    print("6. Получить выписку по всем счетам")
                    print("7. Выйти из личного кабинета")
                    action = input("\nВыберите операцию (1-7): ").strip()

                    if action in ("1", "2", "3", "4", "5", "6"):
                        if not verify_secret(client):
                            continue

                    try:
                        if action == "1":
                            currency = input("Введите код валюты для нового счёта (например, RUB): ").strip().upper()
                            if currency:
                                bank.open_account(client_id, currency)
                                print(f"\nУспешно! Открыт новый счёт в валюте: {currency}")
                            else:
                                print("Ошибка: валюта не может быть пустой.")

                        elif action == "2":
                            currency = input("Введите валюту счёта, который хотите закрыть: ").strip().upper()
                            if currency:
                                bank.close_account(client_id, currency)
                                print(f"\nУспешно! Счёт в валюте {currency} закрыт.")
                            else:
                                print("Ошибка: валюта не может быть пустой.")

                        elif action == "3":
                            currency = input("Введите валюту счёта для пополнения: ").strip().upper()
                            amount = float(input("Введите сумму для пополнения: "))
                            bank.deposit(client_id, currency, amount)
                            print(f"\nУспешно! Счёт в {currency} пополнен на {amount:.2f} {currency}.")
                            acc = bank.get_client(client_id).get_account(currency)
                            print(f"Текущий баланс: {acc.balance:.2f} {currency}")

                        elif action == "4":
                            currency = input("Введите валюту счёта для снятия: ").strip().upper()
                            amount = float(input("Введите сумму для снятия: "))
                            bank.withdraw(client_id, currency, amount)
                            print(f"\nУспешно! Со счёта в {currency} снято {amount:.2f} {currency}.")
                            acc = bank.get_client(client_id).get_account(currency)
                            print(f"Текущий баланс: {acc.balance:.2f} {currency}")

                        elif action == "5":
                            print("\nПЕРЕВОД СРЕДСТВ")
                            from_curr = input("Введите валюту вашего счёта: ").strip().upper()
                            to_id = input("Введите ID получателя: ").strip()
                            to_curr = input("Введите валюту счёта получателя: ").strip().upper()
                            amount = float(input("Введите сумму перевода: "))
                            bank.transfer(client_id, from_curr, to_id, to_curr, amount)
                            print(f"\nУспешно! Переведено {amount:.2f} {from_curr} клиенту {to_id}.")

                        elif action == "6":
                            statement = bank.get_user_statement(client_id)
                            print("\n"+ statement)
                            filename = f"statement_{client_id}.txt"
                            with open(filename, "w", encoding="utf-8") as f:
                                f.write(statement)
                            print(f"Выписка сохранена в файл '{filename}'")

                        elif action == "7":

                            print("\nВыход из личного кабинета...")
                            break

                    except ValueError:
                        print("Ошибка: сумма должна быть числом.")
                    except AccountOwnershipError as e:
                        print(f"Ошибка доступа: {e}")
                    except InsufficientFundsError:
                        print("Ошибка: недостаточно средств на счёте.")
                    except InvalidAmountError:
                        print("Ошибка: сумма должна быть положительной.")
                    except AccountNotFoundError as e:
                        msg = str(e)
                        if "Валюты должны совпадать" in msg:
                            print("Ошибка: перевод возможен только между счетами в одинаковой валюте.")
                        else:
                            print("Ошибка: счёт в указанной валюте не найден.")
                    except AccountExistsError as e:
                        print(f"Ошибка: {e}")
            except ClientNotFoundError:
                print("Ошибка: клиент с указанным ID не найден.")

        elif choice == "3":
            print("\nСпасибо за использование банка! До свидания!")
            break

        else:
            print("Неверный выбор. Введите 1, 2 или 3.")


if __name__ == "__main__":
    main()