from model.Loan import Loan

class CarLoan(Loan):
    def __init__(self, loan_id, customer, principal_amount, interest_rate, loan_term_months, loan_status, car_model, car_value):
        super().__init__(loan_id, customer, principal_amount, interest_rate, loan_term_months, 'CarLoan', loan_status)
        self.car_model = car_model
        self.car_value = car_value
