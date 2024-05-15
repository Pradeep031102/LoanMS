from model.Loan import Loan

class HomeLoan(Loan):
    def __init__(self, loan_id, customer, principal_amount, interest_rate, loan_term_months, loan_status, property_address, property_value):
        super().__init__(loan_id, customer, principal_amount, interest_rate, loan_term_months, 'HomeLoan', loan_status)
        self.property_address = property_address
        self.property_value = property_value
