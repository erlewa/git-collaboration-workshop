from main import print_box

expected_2_2 = (
  "**\n"
  "**\n"
)

expected_10_3 = (
  "**********\n"
  "*        *\n"
  "**********\n"
)

expected_3_10 = (
  "***\n"
  "* *\n"
  "* *\n"
  "* *\n"
  "* *\n"
  "* *\n"
  "* *\n"
  "* *\n"
  "* *\n"
  "***\n"
)

def test_2_2(capsys):
    print_box(2, 2)
    stdout = capsys.readouterr()

    assert stdout.out == expected_2_2

def test_10_3(capsys):
    print_box(10, 3)
    stdout = capsys.readouterr()

    assert stdout.out == expected_10_3

def test_10_3(capsys):
    print_box(3, 10)
    stdout = capsys.readouterr()

    assert stdout.out == expected_3_10
