import unittest

from day_1_expense_report.expense_report import ExpenseBook


class FindMatchingPair(unittest.TestCase):
    def test_should_return_empty_table_when_nothing_found(self):
        # given
        expense_book = ExpenseBook([1721, 979, 366, 291, 675, 1456])

        # when
        result = expense_book.findMatchingPair()

        # then
        self.assertEqual(result, [])

    def test_should_find_result_for_easiest_case(self):
        # given
        expense_book = ExpenseBook([2019, 1])

        # when
        result = expense_book.findMatchingPair()

        # then
        self.assertEqual(result, [2019, 1])

    def test_should_find_the_pair_for_a_short_list(self):
        # given
        expense_book = ExpenseBook([1721, 979, 366, 299, 675, 1456])

        # when
        result = expense_book.findMatchingPair()

        # then
        self.assertEqual(result, [1721, 299])

    def test_should_give_result(self):
        # given
        expense_book = ExpenseBook([2019, 1])

        # when
        result = expense_book.get_result()

        # then
        self.assertEqual(result, 2019)

    def test_should_find_the_result_for_a_list(self):
        # given
        expense_book = ExpenseBook([1721, 979, 366, 299, 675, 1456])

        # when
        result = expense_book.get_result()

        # then
        self.assertEqual(result, 514579)


class FindMatchingTriplet(unittest.TestCase):
    def test_should_find_the_pair_for_a_short_list(self):
        # given
        expense_book = ExpenseBook([1721, 979, 366, 299, 675, 1456])

        # when
        result = expense_book.findMatchingTriplet()

        # then
        self.assertEqual(result, [979, 366, 675])

    def test_should_find_the_result_for_triplet(self):
        # given
        expense_book = ExpenseBook([1721, 979, 366, 299, 675, 1456])

        # when
        result = expense_book.get_result_for_triplet()

        # then
        self.assertEqual(result, 241861950)


if __name__ == '__main__':
    unittest.main()
