class Loan:
    def __init__(self, loan_id, customer, principal_amount, interest_rate, loan_term_months, loan_type, loan_status):
        self.loan_id = loan_id
        self.customer = customer
        self.principal_amount = principal_amount
        self.interest_rate = interest_rate
        self.loan_term_months = loan_term_months
        self.loan_type = loan_type
        self.loan_status = loan_status
