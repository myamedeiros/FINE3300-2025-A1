import csv

class CurrencyConverter:
    def __init__(self):
        # Fetch the USD/CAD rates from BOC file as a private attribute
        with open("BankOfCanadaExchangeRates.csv", newline="") as f:
            reader = csv.DictReader(f)
            self.__latest_rate = float(list(reader)[-1]["USD/CAD"])

    # applying the rate fetched
    def convert(self, amount, frm, to):
        if frm == "USD" and to == "CAD":
            return amount * self.__latest_rate
        elif frm == "CAD" and to == "USD":
            return amount / self.__latest_rate
        else:
            return 0

# Initialize the converter
converter = CurrencyConverter()

# User input
amount = float(input("Enter the $ Amount: "))
frm = input("From (USD or CAD): ").upper()
to = input("To (USD or CAD): ").upper()

# Punishment for incorrect input
if frm not in ["USD", "CAD"] or to not in ["USD", "CAD"]:
    print("OH NO! You have to pick between CAD or USD.")
else:
    converted = converter.convert(amount, frm, to)
    print(f"{amount} {frm} is equal to {converted:.2f} {to}")
