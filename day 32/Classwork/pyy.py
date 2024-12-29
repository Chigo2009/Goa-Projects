class User:
    def __init__(self, name, surname, born_year, password, email):
        self.name = name
        self.surname = surname
        self.born_year = born_year
        self.password = password
        self.email = email
        self.cards = []  # list of Card objects
    
    def add_card(self, card):
        self.cards.append(card)
        
    def __str__(self):
        return f"{self.name} {self.surname} - Email: {self.email}"

class Card:
    def __init__(self, card_type, card_number):
        self.card_type = card_type  # e.g., "mastercard", "amex"
        self.card_number = card_number
        
    def __str__(self):
        return f"{self.card_type} - {self.card_number}"

class Transaction:
    def __init__(self, sender, receiver, amount, currency_from, currency_to):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.currency_from = currency_from
        self.currency_to = currency_to

    def process_transaction(self):
        # Here, we'll just assume the transaction is successful
        # In a real system, we'd validate if the sender has enough balance
        print(f"Transaction from {self.sender.name} to {self.receiver.name}:")
        print(f"Amount: {self.amount} {self.currency_from} -> {self.amount} {self.currency_to}")
        
        # After the transaction is processed, we can reduce balances or update records

class CurrencyConverter:
    conversion_rates = {
        'GEL-USD': 0.38,  # Example rate
        'USD-GEL': 2.64    # Example rate
    }
    
    @staticmethod
    def convert(amount, currency_from, currency_to):
        if currency_from == 'GEL' and currency_to == 'USD':
            return amount * CurrencyConverter.conversion_rates['GEL-USD']
        elif currency_from == 'USD' and currency_to == 'GEL':
            return amount * CurrencyConverter.conversion_rates['USD-GEL']
        else:
            return amount  # For unsupported conversions, return the same amount

# Example usage

# Creating users
user1 = User(name="John", surname="Doe", born_year=1990, password="12345", email="john@example.com")
user2 = User(name="Jane", surname="Smith", born_year=1992, password="67890", email="jane@example.com")

# Adding cards to users
card1 = Card(card_type="mastercard", card_number="1234-5678-9101-1121")
card2 = Card(card_type="amex", card_number="2345-6789-1011-2233")
user1.add_card(card1)
user2.add_card(card2)

# Process a transaction
transaction = Transaction(sender=user1, receiver=user2, amount=100, currency_from="GEL", currency_to="USD")
transaction.process_transaction()

# Convert GEL to USD
amount_in_usd = CurrencyConverter.convert(100, 'GEL', 'USD')
print(f"100 GEL = {amount_in_usd} USD")

# Show user details
print(user1)
print(user2)
