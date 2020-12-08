import itertools

from common.file_reader import FileReader


def count_unique_answers(answers: str) -> int:
    given_answers = [answer.strip() for answer in answers.strip()]
    unique_answers = set(itertools.chain(*given_answers))

    return len(unique_answers)


def count_answers_where_everyone_says_yes(answers: str) -> int:
    answers_by_people = [set(list(answer)).intersection() for answer in answers.split()]

    return len(answers_by_people[0].intersection(*answers_by_people))


def count_total_answers(answers_by_group) -> int:
    return sum([count_unique_answers(group) for group in answers_by_group])


def count_total_answers_part_2(answers_by_group) -> int:
    return sum([count_answers_where_everyone_says_yes(group) for group in answers_by_group])


if __name__ == '__main__':
    file_reader = FileReader('./input')
    answers_by_group = file_reader.to_str_list('\n\n')

    print(count_total_answers(answers_by_group))
    print(count_total_answers_part_2(answers_by_group))
