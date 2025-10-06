class MortgagePayment:
    def __init__(self, annual_rate, amortization_years):
        self.__annual_rate = annual_rate / 100  # convert percentage to decimal (private)
        self.__amortization_years = amortization_years  # private

    def _pva(self, rate_per_period, num_periods):
        return (1 - (1 + rate_per_period) ** -num_periods) / rate_per_period

    def payments(self, principal):
        # Monthly payments 
        monthly_rate = (1 + self.__annual_rate / 2) ** (1/6) - 1
        n_months = self.__amortization_years * 12
        monthly_payment = principal / self._pva(monthly_rate, n_months)

        # Semi-monthly payments (24 per yr)
        semi_monthly_rate = (1 + self.__annual_rate / 2) ** (1/12) - 1
        n_semi_monthly = self.__amortization_years * 24
        semi_monthly_payment = principal / self._pva(semi_monthly_rate, n_semi_monthly)

        # Bi-weekly payments (26 per yr)
        bi_weekly_rate = (1 + self.__annual_rate / 2) ** (1/13) - 1
        n_bi_weekly = self.__amortization_years * 26
        bi_weekly_payment = principal / self._pva(bi_weekly_rate, n_bi_weekly)

        # Accelerated bi-weekly payments (1/2 monthly)
        accelerated_bi_weekly_payment = monthly_payment / 2

        # Weekly payments (52 per yr)
        weekly_rate = (1 + self.__annual_rate / 2) ** (1/26) - 1
        n_weekly = self.__amortization_years * 52
        weekly_payment = principal / self._pva(weekly_rate, n_weekly)

        # Accelerated weekly payments (1/4 monthly)
        accelerated_weekly_payment = monthly_payment / 4

        return (round(monthly_payment, 2),
                round(semi_monthly_payment, 2),
                round(bi_weekly_payment, 2),
                round(weekly_payment, 2),
                round(accelerated_bi_weekly_payment, 2),
                round(accelerated_weekly_payment, 2))


# User input
principal = float(input("Enter Principal:"))
annualRate = float(input("Enter Annual Rate:"))
term = float(input("Enter Term:"))

mortgage = MortgagePayment(annualRate, term)
answers = mortgage.payments(principal)

typeList = ["Montly Payment: $","Semi-Montly Payment: $","Bi-Weekly Payment: $","Weekly Payment: $","Rapid Bi-Weekly Payment: $","Rapid Weekly Payment: $"];

# Rounding to cents
for i in range(len(answers)):
    print(typeList[i], round(answers[i], 2))
