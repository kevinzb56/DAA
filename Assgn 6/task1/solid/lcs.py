import pandas as pd
import re
import os
from abc import ABC, abstractmethod

# Abstraction for grade validation (ISP, DIP)
class GradeValidator(ABC):
    @abstractmethod
    def validate(self, grades: str):
        pass

# Concrete implementation of grade validation (SRP)
class StandardGradeValidator(GradeValidator):
    def validate(self, grades: str):
        if len(grades) != 40:
            raise ValueError(f"Invalid grade sequence length: {grades}. Expected length is 40 characters.")

        if any(char.isdigit() for char in grades):
            raise ValueError(f"Invalid grade sequence: {grades}. Numbers found in the sequence.")

        if not all(re.match(r"[A-F]{2}", grades[i:i + 2]) for i in range(0, len(grades), 2)):
            raise ValueError(f"Invalid grade sequence: {grades}. Invalid grade format detected.")

# LCS Calculator class (SRP)
class LCSCalculator:
    @staticmethod
    def calculate_lcs(str1: str, str2: str) -> str:
        dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        lcs_sequence = []
        i, j = len(str1), len(str2)
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                lcs_sequence.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        return ''.join(reversed(lcs_sequence))

# CSV Processor class (SRP, OCP)
class CSVProcessor:
    def __init__(self, validator: GradeValidator):
        self.validator = validator

    def process_csv(self, file_path: str) -> str:
        df = pd.read_csv(file_path)
        grades_list = df["Grades"].tolist()

        # Initialize LCS as the first student's grades
        overall_lcs = grades_list[0]

        for i in range(1, len(grades_list)):
            try:
                # Validate each student's grade sequence
                self.validator.validate(grades_list[i])
                # Calculate LCS only if the grades are valid
                overall_lcs = LCSCalculator.calculate_lcs(overall_lcs, grades_list[i])
            except ValueError as e:
                print(f"Error for student {df.iloc[i]['Student ID']}: {e}")
                return None

        return overall_lcs

# Test Runner class (SRP)
class TestRunner:
    def __init__(self, processor: CSVProcessor, directory: str):
        self.processor = processor
        self.directory = directory

    def run_test_cases(self, case_type: str, num_cases: int):
        print(f"\n{case_type.capitalize()} Test Cases:")
        for i in range(1, num_cases + 1):
            file_path = os.path.join(self.directory, f"{case_type}_test_case_{i}.csv")
            lcs_result = self.processor.process_csv(file_path)
            if lcs_result is not None:
                print(f"LCS for {case_type.capitalize()} Test Case {i}: {lcs_result}")
            else:
                print(f"Error detected in {case_type.capitalize()} Test Case {i}. Skipping LCS calculation.")

# Main function to run the program
def main():
    validator = StandardGradeValidator()
    processor = CSVProcessor(validator)
    test_runner = TestRunner(processor, "lcs_test_cases")

    # Run positive test cases
    test_runner.run_test_cases("positive", 5)
    # Run negative test cases
    test_runner.run_test_cases("negative", 5)

if __name__ == "__main__":
    main()
