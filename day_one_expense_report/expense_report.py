from functools import reduce
from typing import List

from day_one_expense_report.file_reader import FileReader


class ExpenseBook():
    def __init__(self, expenses: List[int]) -> None:
        self.rows = expenses

    def findMatchingPair(self) -> List[int]:
        VALUE_TO_FIND = 2020
        for entry in self.rows:
            matching_value = VALUE_TO_FIND - entry

            if matching_value in self.rows:
                return [entry, matching_value]

        return []

    def findMatchingTriplet(self) -> List[int]:
        VALUE_TO_FIND = 2020
        for index, initial_entry in enumerate(self.rows):
            remaining_entries = self.rows[index + 1:]
            for second_entry in remaining_entries:
                matching_value = VALUE_TO_FIND - initial_entry - second_entry

                if matching_value in self.rows:
                    return [initial_entry, second_entry, matching_value]

        return []

    def get_result(self) -> int:
        return reduce((lambda x, y: x * y), self.findMatchingPair())

    def get_result_for_triplet(self) -> int:
        return reduce((lambda x, y: x * y), self.findMatchingTriplet())


if __name__ == '__main__':
    file_reader = FileReader('./input')
    list_of_expenses = file_reader.to_int_list()
    expense_book = ExpenseBook(list_of_expenses)
    print(expense_book.get_result())
    print(expense_book.get_result_for_triplet())
