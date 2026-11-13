from main import print_box

expected_2_2 = "**\n**\n"

expected_3_3 = "***\n* *\n***\n"

expected_5_4 = "*****\n*   *\n*   *\n*****\n"

expected_10_3 = "**********\n*        *\n**********\n"

expected_3_10 = "***\n* *\n* *\n* *\n* *\n* *\n* *\n* *\n* *\n***\n"

expected_15_12 = (
    "***************\n"
    "*             *\n"
    "*             *\n"
    "*             *\n"
    "*             *\n"
    "*             *\n"
    "*             *\n"
    "*             *\n"
    "*             *\n"
    "*             *\n"
    "*             *\n"
    "***************\n"
)


def test_2_2(capsys):
    print_box(2, 2)
    stdout = capsys.readouterr()

    assert stdout.out == expected_2_2


def test_3_3(capsys):
    print_box(3, 3)
    stdout = capsys.readouterr()

    assert stdout.out == expected_3_3


def test_5_4(capsys):
    print_box(5, 4)
    stdout = capsys.readouterr()

    assert stdout.out == expected_5_4


def test_10_3(capsys):
    print_box(10, 3)
    stdout = capsys.readouterr()

    assert stdout.out == expected_10_3


def test_3_10(capsys):
    print_box(3, 10)
    stdout = capsys.readouterr()

    assert stdout.out == expected_3_10


def test_15_12(capsys):
    print_box(15, 12)
    stdout = capsys.readouterr()

    assert stdout.out == expected_15_12