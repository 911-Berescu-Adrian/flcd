class ScannerException(Exception):
    def __init__(self, message, line_number):
        super().__init__(message)
        self.line_number = line_number

    def __str__(self):
        return f"ScannerException: {super().__str__()}, Line {self.line_number}"
