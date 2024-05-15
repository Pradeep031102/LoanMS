from dao.ILoanRepository import ILoanRepository
from model import Loan
from util.DBConnUtil import DBConnUtil
from exception import InvalidLoanException
import pyodbc

class ILoanRepositoryImpl(ILoanRepository):
    def __init__(self):
        self.db_conn_util = DBConnUtil()

    def apply_loan(self, loan: Loan):
        connection = self.db_conn_util.getDBConn()
        cursor = connection.cursor()
        try:
            # Assuming Loan table has columns loan_id, customer_id, principal_amount, interest_rate, loan_term_months, loan_type, loan_status
            cursor.execute("""
                INSERT INTO Loan (customer_id, principal_amount, interest_rate, loan_term_months, loan_type, loan_status)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (loan.customer.customer_id, loan.principal_amount, loan.interest_rate, loan.loan_term_months, loan.loan_type, loan.loan_status))
            connection.commit()
            print("Loan applied successfully!")
        except pyodbc.Error as e:
            print(f"Error applying loan: {e}")
        finally:
            cursor.close()
            connection.close()

    def calculate_interest(self, loan_id):
        connection = self.db_conn_util.getDBConn()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT principal_amount, interest_rate, loan_term_months FROM Loan WHERE loan_id = ?", (loan_id,))
            loan_data = cursor.fetchone()
            if not loan_data:
                raise InvalidLoanException("Invalid loan ID")

            principal_amount, interest_rate, loan_term_months = loan_data
            interest = (principal_amount * interest_rate * loan_term_months) / 12
            return interest
        except pyodbc.Error as e:
            print(f"Error calculating interest: {e}")
        finally:
            cursor.close()
            connection.close()

    def loan_status(self, loan_id):
        connection = self.db_conn_util.getDBConn()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT credit_score FROM Customer WHERE customer_id=(SELECT customer_id FROM Loan WHERE loan_id=?)", (loan_id,))
            credit_score = cursor.fetchone()[0]
            if credit_score > 650:
                print("Loan approved.")
                update_query = "UPDATE Loan SET loan_status='approved' WHERE loan_id=?"
                cursor.execute(update_query, (loan_id,))
                connection.commit()
            else:
                print("Loan rejected based on credit score.")
        except pyodbc.Error as e:
            print(f"Error checking credit score: {e}")
        finally:
            cursor.close()
            connection.close()

    def calculate_emi(self, loan_id):
        connection = self.db_conn_util.getDBConn()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT principal_amount, interest_rate, loan_term_months FROM Loan WHERE loan_id=?", (loan_id,))
            loan_data = cursor.fetchone()
            if not loan_data:
                raise InvalidLoanException("Invalid loan ID")

            principal_amount, interest_rate, loan_term_months = loan_data
            monthly_interest_rate = interest_rate / 12 / 100
            emi = (principal_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** loan_term_months)) / (((1 + monthly_interest_rate) ** loan_term_months) - 1)
            return emi
        except pyodbc.Error as e:
            print(f"Error calculating EMI: {e}")
        finally:
            cursor.close()
            connection.close()

    def loan_repayment(self, loan_id, amount):
        connection = self.db_conn_util.getDBConn()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT principal_amount, interest_rate, loan_term_months FROM Loan WHERE loan_id=?", (loan_id,))
            loan_data = cursor.fetchone()
            if not loan_data:
                raise InvalidLoanException("Invalid loan ID")

            principal_amount, interest_rate, loan_term_months = loan_data
            emi = (principal_amount * interest_rate * ((1 + interest_rate) ** loan_term_months)) / (((1 + interest_rate) ** loan_term_months) - 1)
            no_of_emi = amount // emi
            if amount < emi or no_of_emi == 0:
                print("Payment rejected. Amount is less than EMI.")
            else:
                print(f"No. of EMIs that can be paid with {amount}: {no_of_emi}")
                # Update variable here
        except pyodbc.Error as e:
            print(f"Error processing loan repayment: {e}")
        finally:
            cursor.close()
            connection.close()

    def get_all_loan(self):
        connection = self.db_conn_util.getDBConn()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Loan")
            loans = cursor.fetchall()
            if loans:
                for loan in loans:
                    print(loan)  # Adjust printing as per your model
            else:
                print("No loans found.")
        except pyodbc.Error as e:
            print(f"Error fetching loans: {e}")
        finally:
            cursor.close()
            connection.close()

    def get_loan_by_id(self, loan_id):
        connection = self.db_conn_util.getDBConn()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Loan WHERE loan_id=?", (loan_id,))
            loan = cursor.fetchone()
            if loan:
                print(loan)  # Adjust printing as per your model
            else:
                raise InvalidLoanException("Loan not found.")
        except pyodbc.Error as e:
            print(f"Error fetching loan: {e}")
        finally:
            cursor.close()
            connection.close()
