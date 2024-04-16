import pytest
from mortgage import MortgageCalculator


class TestStrings:
    Mortgage = MortgageCalculator("test mortgage", "16-04-2024", 1000000, 0.05, 30, 0, 20000)

    def test_mortgage_calculator(self):
        self.mortgage = MortgageCalculator("test mortgage", "16-04-2024", 100000, 0.05, 30, 0, 20000)
        assert self.mortgage.principal == 100000

    def test_mortgage_with_string_values(self):
        with pytest.raises(ValueError):
            MortgageCalculator("test", "16-04-2024", "initial_principal", "initial_interest",
                               "initial_term", "extra_cost", "deposit")
