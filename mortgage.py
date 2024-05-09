class Mortgage:
    def __init__(self, mortgage_id, mortgage_name, start_date, initial_interest, initial_term, initial_principal, extra_cost, deposit, user_id):
        self._mortgage_id = mortgage_id
        self._mortgage_name = mortgage_name
        self._start_date = start_date
        self._initial_interest = initial_interest
        self._initial_term = initial_term
        self._initial_principal = initial_principal
        self._extra_cost = extra_cost
        self._deposit = deposit
        self._user_id = user_id

    @property
    def mortgage_id(self):
        return self._mortgage_id

    @mortgage_id.setter
    def mortgage_id(self, mortgage_id):
        if not mortgage_id:
            raise ValueError("Mortgage ID is required")
        try:
            mortgageid = int(mortgage_id)
        except ValueError:
            raise ValueError("Mortgage ID must be an integer")
        self._mortgage_id = mortgageid

    @property
    def mortgage_name(self):
        return self._mortgage_name

    @mortgage_name.setter
    def mortgage_name(self, mortgage_name):
        if not mortgage_name:
            self._mortgage_name = ""
        else:
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
        # Need to look up and check float type checking
        try:
            initialinterest = float(initial_interest)
        except ValueError:
            raise ValueError("Initial interest must be a number")
        self._initial_interest = initialinterest

    @property
    def initial_term(self):
        return self._initial_term

    @initial_term.setter
    def initial_term(self, initial_term):
        if not initial_term:
            raise ValueError("Initial term is required")
        try:
            initialterm = int(initial_term)
        except ValueError:
            raise ValueError("Initial term must be an integer")
        self._initial_term = initialterm

    @property
    def initial_principal(self):
        return self._initial_principal

    @initial_principal.setter
    def initial_principal(self, initial_principal):
        if not initial_principal:
            raise ValueError("Initial principal is required")
        try:
            initialprincipal = int(initial_principal)
        except ValueError:
            raise ValueError("Initial principal must be an integer")
        self._initial_principal = initialprincipal

    @property
    def extra_cost(self):
        return self._extra_cost

    @extra_cost.setter
    def extra_cost(self, extra_cost):
        if not extra_cost:
            self._extra_cost = 0
        try:
            extracost = int(extra_cost)
        except ValueError:
            raise ValueError("Extra cost must be an integer")
        self._extra_cost = extracost

    @property
    def deposit(self):
        return self._deposit

    @deposit.setter
    def deposit(self, deposit):
        if not deposit:
            self._deposit = 0
        try:
            deposit = int(deposit)
        except ValueError:
            raise ValueError("Deposit must be an integer")
        self._deposit = deposit

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        if not user_id:
            raise ValueError("User ID is required")
        if len(str(userid)) >= 10:
            raise ValueError("Invlaid ID")
        try:
            userid = int(userid)
        except ValueError:
            raise ValueError("User ID must be an integer")
        self._user_id = userid

    def calculate_monthly_interest(self):
        # Might be problems with this equation with float and int types. Will look into it
        return self.initial_principal * self.initial_interest / 12 if self.initial_principal > 0 else 0

    def calculate_repayment(self):
        rate_per_month = self.initial_interest / 12 / 100
        term_in_months = self.initial_term * 12
        return self.initial_principal * (rate_per_month / (1 - (1 + rate_per_month) ** -term_in_months))

    def __str__(self):
        return "\n".join([
            f"Mortgage ID: {self.mortgage_id}",
            f"Mortgage Name: {self.mortgage_name}",
            f"Start Date: {self.start_date}",
            f"Initial Interest: {self.initial_interest}",
            f"Initial Term: {self.initial_term}",
            f"Initial Principal: {self.initial_principal}",
            f"Extra Cost: {self.extra_cost}",
            f"Deposit: {self.deposit}",
            f"User ID: {self.user_id}"
        ])


if __name__ == "__main__":
    print("Start Tests")
    mortgage = Mortgage(
        mortgage_id=1,
        mortgage_name="test Mortgage",
        start_date="2024-05-06",
        initial_interest=5.0,
        initial_term=30,
        initial_principal=300000,
        extra_cost=0,
        deposit=50000,
        user_id=12345678
    )

    print(mortgage)
    assert (
            str(mortgage)
            == "Mortgage ID: 1\nMortgage Name: test Mortgage\nStart Date: 2024-05-06\nInitial Interest: "
               "5.0\nInitial Term: 30\nInitial Principal: 300000\nExtra Cost: 0\nDeposit: 50000\nUser ID: 12345678"
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
    print("Repayment:", mortgage.calculate_repayment())
    print("End Tests")
