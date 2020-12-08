from typing import List

from common.file_reader import FileReader


def find_missing_boarding_pass(seats: List[int]) -> int:
    for neighbour in seats:
        me = neighbour + 1
        neighbour2 = me + 1

        if me not in seats and neighbour2 in seats:
            return me


class BoardingPass():
    def __init__(self, sequence: str):
        self._sequence = sequence

    def get_row(self) -> int:
        rows = list(range(0, 128))
        positions = iter(self._sequence.strip()[0:7])

        while True:
            try:
                position = next(positions)
                is_upper_half = position.startswith('F')
                limit = int(len(rows) / 2)

                if is_upper_half:
                    rows = rows[0:limit]
                else:
                    rows = rows[limit:]
            except StopIteration:
                break

        return rows[0]

    def get_column(self) -> int:
        rows = list(range(0, 8))
        positions = iter(self._sequence.strip()[7:])

        while True:
            try:
                position = next(positions)
                is_upper_half = position.startswith('L')
                limit = int(len(rows) / 2)

                if is_upper_half:
                    rows = rows[0:limit]
                else:
                    rows = rows[limit:]
            except StopIteration:
                break

        return max(rows)

    def get_seat_id(self) -> int:
        return self.get_row() * 8 + self.get_column()


if __name__ == '__main__':
    file_reader = FileReader('./input')
    sequences = file_reader.to_str_list()
    list_of_seats_id = [BoardingPass(sequence).get_seat_id() for sequence in sequences]

    max_seat_id = max(list_of_seats_id)

    print(f"Max Seat ID : {max_seat_id}")
    print(f"My Seat ID : {find_missing_boarding_pass(list_of_seats_id)}")
