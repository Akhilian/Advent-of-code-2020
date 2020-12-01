from functools import reduce
from typing import List

from day_one_expense_report.file_reader import FileReader


class ExpenseBook():
    def __init__(self, expenses: List[int]) -> None:
        self.rows = expenses

    def findMatchPair(self) -> List[int]:
        value_to_find = 2020
        for row in self.rows:
            matching_value = value_to_find - row

            if matching_value in self.rows:
                return [row, matching_value]

        return []

    def get_result(self):
        return reduce((lambda x, y: x * y), self.findMatchPair())


if __name__ == '__main__':
    file_reader = FileReader('./input')
    list_of_expenses = file_reader.to_int_list()
    expense_book = ExpenseBook(list_of_expenses)
    print(expense_book.get_result())
