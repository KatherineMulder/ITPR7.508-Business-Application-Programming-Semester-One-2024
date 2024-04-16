class MortgageCalculator:
    def __init__(self, mortgage_name, established_date, initial_principal, initial_interest, initial_term,
                 extra_cost, deposit):
        self.m_name = mortgage_name
        self.date = established_date
        self._principal = initial_principal
        self.interest = initial_interest
        self.term = initial_term / 12
        self.extra_costs = extra_cost
        self.deposit = deposit

    @property
    def principal(self):
        return self._principal

    @principal.setter
    def principal(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError
        self._principal = value
        return

    @property
    def interest(self):
        return self._interest

    @interest.setter
    def interest(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Interest must be a number")
        if value < 0:
            raise ValueError("Interest rate cannot be less than 0")
        self._interest = value
