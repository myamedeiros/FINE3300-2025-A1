import csv

# Load latest USD/CAD rate
with open("BankOfCanadaExchangeRates.csv", newline="") as f:
    reader = csv.DictReader(f)
    latest_rate = float(list(reader)[-1]["USD/CAD"])

# Conversion function
def convert(amount, frm, to):
    if frm == "USD" and to == "CAD":
        return amount * latest_rate
    elif frm == "CAD" and to == "USD":
        return amount / latest_rate
    else:
        return 0

# User input
amount = float(input("Enter the $ Amount: "))
frm = input("From (USD or CAD): ").upper()
to = input("To (USD or CAD): ").upper()

converted = convert(amount, frm, to)
print(f"{amount} {frm} is equal to {converted:.2f} {to}")