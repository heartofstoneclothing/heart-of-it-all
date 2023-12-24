from flask import Flask, render_template, request

app = Flask(__name__)

class CurrencyConverter:
    def __init__(self, exchange_rates):
        self.exchange_rates = exchange_rates

    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            return None

        conversion_rate = self.exchange_rates[to_currency] / self.exchange_rates[from_currency]
        converted_amount = amount * conversion_rate

        return converted_amount

# Define your exchange rates
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.75,
    "JPY": 110.0,
}

# Create an instance of CurrencyConverter
converter = CurrencyConverter(exchange_rates)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        amount = float(request.form["amount"])
        from_currency = request.form["from_currency"]
        to_currency = request.form["to_currency"]

        result = converter.convert(amount, from_currency, to_currency)

    return render_template("index.html", result=result)

if __name__ == "__app.py__":
    app.run(debug=True)
