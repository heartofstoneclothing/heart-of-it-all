class CurrencyConverter:
    def __init__(self, exchange_rates):
        self.exchange_rates = exchange_rates

    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            print("Invalid currencies.")
            return None

        conversion_rate = self.exchange_rates[to_currency] / self.exchange_rates[from_currency]
        converted_amount = amount * conversion_rate

        return converted_amount

if __name__ == "__main__":
    # Define your exchange rates
    exchange_rates = {
        "USD": 1.0,     # 1 USD to USD (base currency)
        "EUR": 0.85,    # 1 USD to EUR
        "GBP": 0.75,    # 1 USD to GBP
        "JPY": 110.0,   # 1 USD to JPY
    }

    # Create an instance of CurrencyConverter
    converter = CurrencyConverter(exchange_rates)

    # Get user input
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the source currency (e.g., USD): ").upper()
    to_currency = input("Enter the target currency (e.g., EUR): ").upper()

    # Perform conversion
    result = converter.convert(amount, from_currency, to_currency)

    # Display the result
    if result is not None:
        print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")
