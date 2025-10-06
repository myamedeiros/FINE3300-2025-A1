class MortgagePayment:
    def __init__(self, annual_rate, amortization_years):
        """
        Initialize the mortgage with a fixed annual interest rate and amortization period (in years).
        """
        self.annual_rate = annual_rate / 100  # convert % to decimal
        self.amortization_years = amortization_years

    def _pva(self, rate_per_period, num_periods):
        """
        Present Value of Annuity Factor (PVA)
        """
        return (1 - (1 + rate_per_period) ** -num_periods) / rate_per_period

    def payments(self, principal):
        """
        Calculate various periodic mortgage payments and return as a tuple:
        (monthly, semi-monthly, bi-weekly, accelerated bi-weekly, weekly, accelerated weekly)
        """
        # Monthly payments
        monthly_rate = (1 + self.annual_rate / 2) ** (1/6) - 1  # monthly rate from semiannual compounding
        n_months = self.amortization_years * 12
        monthly_payment = principal / self._pva(monthly_rate, n_months)

        # Semi-monthly payments (24 per year)
        semi_monthly_rate = (1 + self.annual_rate / 2) ** (1/12) - 1
        n_semi_monthly = self.amortization_years * 24
        semi_monthly_payment = principal / self._pva(semi_monthly_rate, n_semi_monthly)

        # Bi-weekly payments (26 per year)
        bi_weekly_rate = (1 + self.annual_rate / 2) ** (1/26) - 1
        n_bi_weekly = self.amortization_years * 26
        bi_weekly_payment = principal / self._pva(bi_weekly_rate, n_bi_weekly)

        # Accelerated bi-weekly payments (half of monthly)
        accelerated_bi_weekly_payment = monthly_payment / 2

        # Weekly payments (52 per year)
        weekly_rate = (1 + self.annual_rate / 2) ** (1/52) - 1
        n_weekly = self.amortization_years * 52
        weekly_payment = principal / self._pva(weekly_rate, n_weekly)

        # Accelerated weekly payments (quarter of monthly)
        accelerated_weekly_payment = monthly_payment / 4

        return (round(monthly_payment, 2),
                round(semi_monthly_payment, 2),
                round(bi_weekly_payment, 2),
                round(accelerated_bi_weekly_payment, 2),
                round(weekly_payment, 2),
                round(accelerated_weekly_payment, 2))
                

# input
principal = float(input("Enter Principal:"))
annualRate = float(input("Enter Annual Rate:"))
term = float(input("Enter Term:"))

mortgage = MortgagePayment(annualRate, term)
answers = mortgage.payments(principal)

typeList = ["Montly Payment: $","Semi-Montly Payment: $","Bi-Weekly Payment: $","Weekly Payment: $","Rapid Bi-Weekly Payment: $","Rapid Weekly Payment: $"];

#easier way to print?
#round to cents?
for i in range(len(answers)):
    print(typeList[i],round(answers[i],2))