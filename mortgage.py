from decimal import Decimal


class Mortgage:
    def __init__(self, mortgage_id, mortgage_name, start_date, initial_interest, initial_term, initial_principal):
        self._mortgage_id = mortgage_id
        self._mortgage_name = mortgage_name
        self._start_date = start_date
        self._initial_interest = initial_interest
        self._initial_term = initial_term
        self._initial_principal = initial_principal

    @property
    def mortgage_id(self):
        return self._mortgage_id

    @mortgage_id.setter
    def mortgage_id(self, mortgage_id):
        if not mortgage_id:
            raise ValueError("Mortgage ID is required")
        self._mortgage_id = mortgage_id

    @property
    def mortgage_name(self):
        return self._mortgage_name

    @mortgage_name.setter
    def mortgage_name(self, mortgage_name):
        if not mortgage_name:
            raise ValueError("Mortgage name is required")
        self._mortgage_name = mortgage_name

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if not start_date:
            raise ValueError("Start date is required")
        self._start_date = start_date

    @property
    def initial_interest(self):
        return self._initial_interest

    @initial_interest.setter
    def initial_interest(self, initial_interest):
        if not initial_interest:
            raise ValueError("Initial interest is required")
        self._initial_interest = initial_interest

    @property
    def initial_term(self):
        return self._initial_term

    @initial_term.setter
    def initial_term(self, initial_term):
        if not initial_term:
            raise ValueError("Initial term is required")
        self._initial_term = initial_term

    @property
    def initial_principal(self):
        return self._initial_principal

    @initial_principal.setter
    def initial_principal(self, initial_principal):
        if not initial_principal:
            raise ValueError("Initial principal is required")
        self._initial_principal = initial_principal

    def __str__(self):
        return "\n".join([
            f"Mortgage ID: {self.mortgage_id}",
            f"Mortgage Name: {self.mortgage_name}",
            f"Start Date: {self.start_date}",
            f"Initial Interest: {self.initial_interest}",
            f"Initial Term: {self.initial_term}",
            f"Initial Principal: {self.initial_principal}",
        ])

    def calculate_monthly_interest(self):
        if self.initial_principal > 0:
            return (Decimal(str(self.initial_principal)) * Decimal(str(self.initial_interest)) / Decimal('12') / Decimal('100')).quantize(Decimal('.01'))
        else:
            return Decimal('0')

    def calculate_monthly_repayment(self):
        rate_per_month = Decimal(str(self.initial_interest)) / Decimal('12') / Decimal('100')
        term_in_months = self.initial_term * 12
        return (Decimal(str(self.initial_principal)) * (rate_per_month / (Decimal('1') - (Decimal('1') + rate_per_month) ** -term_in_months))).quantize(Decimal('.01'))

    def calculate_monthly_principal_repayment(self):
        monthly_interest = self.calculate_monthly_interest()
        monthly_repayment = self.calculate_monthly_repayment()
        return monthly_repayment - monthly_interest

    def calculate_principal_remaining(self, months):
        remaining_principal = Decimal(str(self.initial_principal))
        for _ in range(months):
            monthly_principal_repayment = self.calculate_monthly_principal_repayment()
            remaining_principal -= monthly_principal_repayment
        return remaining_principal

    def calculate_fortnightly_interest(self):
        if self.initial_principal > 0:
            return (Decimal(str(self.initial_principal)) * Decimal(str(self.initial_interest)) / Decimal('26') / Decimal('100')).quantize(Decimal('.01'))
        else:
            return Decimal('0')

    def calculate_fortnightly_repayment(self):
        rate_per_fortnight = Decimal(str(self.initial_interest)) / Decimal('26') / Decimal('100')
        term_in_fortnights = self.initial_term * 26
        return (Decimal(str(self.initial_principal)) * (rate_per_fortnight / (Decimal('1') - (Decimal('1') + rate_per_fortnight) ** -term_in_fortnights))).quantize(Decimal('.01'))

    def calculate_fortnightly_principal_repayment(self):
        fortnightly_interest = self.calculate_fortnightly_interest()
        fortnightly_repayment = self.calculate_fortnightly_repayment()
        return fortnightly_repayment - fortnightly_interest

    def calculate_fortnightly_principal_remaining(self, fortnights):
        for _ in range(fortnights):
            fortnightly_principal_repayment = self.calculate_fortnightly_principal_repayment()
            self.initial_principal -= fortnightly_principal_repayment


if __name__ == "__main__":
    print("Start Tests")
    mortgage = Mortgage(
        mortgage_id=1,
        mortgage_name="test Mortgage",
        start_date="2024-05-06",
        initial_interest=5.0,
        initial_term=30,
        initial_principal=300000,
    )

    print(mortgage)
    assert (
            str(mortgage)
            == "Mortgage ID: 1\nMortgage Name: test Mortgage\nStart Date: 2024-05-06\nInitial Interest: "
               "5.0\nInitial Term: 30\nInitial Principal: 300000"
    ), "__str__ not the same"

    mortgage.mortgage_name = "New Mortgage"
    assert mortgage.mortgage_name == "New Mortgage", "just a getter and setter"

    try:
        mortgage.mortgage_id = ""
    except ValueError:
        pass
    except:
        raise

    print("Monthly Interest:", mortgage.calculate_monthly_interest())
    print("Monthly Repayment:", mortgage.calculate_monthly_repayment())
    print("Monthly Principal Repayment:", mortgage.calculate_monthly_principal_repayment())
    print("Fortnightly Interest:", mortgage.calculate_fortnightly_interest())
    print("Fortnightly Repayment:", mortgage.calculate_fortnightly_repayment())
    print("Fortnightly Principal Repayment:", mortgage.calculate_fortnightly_principal_repayment())
    print("End Tests")

# TODO add deposit function

# TODO add extra cost function
