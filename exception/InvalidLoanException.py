class InvalidLoanException(Exception):
    def __init__(self, message="Invalid loan ID or operation"):
        self.message = message
        super().__init__(self.message)
