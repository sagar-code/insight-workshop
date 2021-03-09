# 15. Imagine you are designing a banking application. What would a
# customer look like? What attributes would she have? What methods
# would she have?


class Bank_account:
    bank_details = {
        'bank_name': 'Global IME',
        'bank_address': 'Danchhi, Kathmandu',
        'bank_ceo': 'Sagar Budhathoki',
        'bank_registration_no': '534-146-20-123',
        'bank_branches': ['Kathmandu', 'Biratnagar','Janakpur', 'Pokhara', 'Dang', 'Butwal', 'Mahendranagar']
    }

    def __init__(self,
                 account_holder_name,
                 account_holder_address,
                 account_number,
                 balance):
        self.account_holder_name = account_holder_name
        self.account_holder_address = account_holder_address
        self.balance = balance

    @classmethod
    def get_bank_details(cls):
        return cls.bank_details

    def deposite(self, amount):
        self.balance += amount


    def withdraw(self, amount):
        if self.balance < amount:
            return False

        self.balance -= amount
        return True

    def get_balance(self):
        return self.balance


Rabina = Bank_account('Rabina Karki',
                   'Kathmandu',
                   '134-34567-9000-91',
                   '1000')
print('Bank Details:\n', Bank_account.get_bank_details())