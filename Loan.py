from dao.ILoanRepositoryImpl import ILoanRepositoryImpl
from model import Loan
from exception import InvalidLoanException

class MainModule:
    def __init__(self):
        self.loan_repo = ILoanRepositoryImpl()

    def display_menu(self):
        print("\n--- Loan Management System Menu ---")
        print("1. Apply for a loan")
        print("2. Calculate interest for a loan")
        print("3. Check loan status")
        print("4. Calculate EMI for a loan")
        print("5. Repay a loan")
        print("6. View all loans")
        print("7. View loan by ID")
        print("8. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.apply_loan()
            elif choice == '2':
                self.calculate_interest()
            elif choice == '3':
                self.check_loan_status()
            elif choice == '4':
                self.calculate_emi()
            elif choice == '5':
                self.repay_loan()
            elif choice == '6':
                self.view_all_loans()
            elif choice == '7':
                self.view_loan_by_id()
            elif choice == '8':
                print("Exiting Loan Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

    def apply_loan(self):
        customer_id = int(input("Enter customer ID: "))
        principal_amount = float(input("Enter principal amount: "))
        interest_rate = float(input("Enter interest rate: "))
        loan_term_months = int(input("Enter loan term (months): "))
        loan_type = input("Enter loan type (HomeLoan/CarLoan): ")
        loan_status = 'pending'  # Default status for new loan applications

        if loan_type.lower() == 'homeloan':
            property_address = input("Enter property address: ")
            property_value = float(input("Enter property value: "))
            loan = Loan(customer_id=customer_id, principal_amount=principal_amount, interest_rate=interest_rate,
                        loan_term_months=loan_term_months, loan_type=loan_type, loan_status=loan_status,
                        property_address=property_address, property_value=property_value)
        elif loan_type.lower() == 'carloan':
            car_model = input("Enter car model: ")
            car_value = float(input("Enter car value: "))
            loan = Loan(customer_id=customer_id, principal_amount=principal_amount, interest_rate=interest_rate,
                        loan_term_months=loan_term_months, loan_type=loan_type, loan_status=loan_status,
                        car_model=car_model, car_value=car_value)
        else:
            print("Invalid loan type. Please enter either HomeLoan or CarLoan.")
            return

        self.loan_repo.apply_loan(loan)

    def calculate_interest(self):
        loan_id = int(input("Enter loan ID: "))
        try:
            interest = self.loan_repo.calculate_interest(loan_id)
            print(f"Interest for loan ID {loan_id}: {interest}")
        except InvalidLoanException as e:
            print(e)

    def check_loan_status(self):
        loan_id = int(input("Enter loan ID: "))
        try:
            status = self.loan_repo.loan_status(loan_id)
            print(f"Loan status for loan ID {loan_id}: {status}")
        except InvalidLoanException as e:
            print(e)

    def calculate_emi(self):
        loan_id = int(input("Enter loan ID: "))
        try:
            emi = self.loan_repo.calculate_emi(loan_id)
            print(f"EMI for loan ID {loan_id}: {emi}")
        except InvalidLoanException as e:
            print(e)

    def repay_loan(self):
        loan_id = int(input("Enter loan ID: "))
        amount = float(input("Enter repayment amount: "))
        try:
            self.loan_repo.loan_repayment(loan_id, amount)
        except InvalidLoanException as e:
            print(e)

    def view_all_loans(self):
        self.loan_repo.get_all_loan()

    def view_loan_by_id(self):
        loan_id = int(input("Enter loan ID: "))
        try:
            self.loan_repo.get_loan_by_id(loan_id)
        except InvalidLoanException as e:
            print(e)

if __name__ == "__main__":
    main_module = MainModule()
    main_module.run()
