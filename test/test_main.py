from main import main

expected_0 = ""

expected_3_3_0 = (
 "***\n"
 "* *\n"
 "***\n"
)

expected_4_3_3_4_0 = (
  "****\n"
  "*  *\n"
  "****\n"
  "***\n"
  "* *\n"
  "* *\n"
  "***\n"
)

def test_exit(monkeypatch, capsys):
  inputs = iter(["0"])
  monkeypatch.setattr("builtins.input", lambda _: next(inputs))
  main()
  stdout = capsys.readouterr()

  assert stdout.out == expected_0 

def test_one_input(monkeypatch, capsys):
  inputs = iter(["3", "3", "*", " ", "0"])
  monkeypatch.setattr("builtins.input", lambda _: next(inputs))
  main()
  stdout = capsys.readouterr()

  assert stdout.out == expected_3_3_0


def test_one_input_late_exit(monkeypatch, capsys):
  inputs = iter(["3", "3", "*", " ", "2", "0"])
  monkeypatch.setattr("builtins.input", lambda _: next(inputs))

  main()
  stdout = capsys.readouterr()

  assert stdout.out == expected_3_3_0

def test_two_boxes(monkeypatch, capsys):
  inputs = iter(["4", "3", "*", " ", "3", "4", "*", " ", "0"])
  monkeypatch.setattr("builtins.input", lambda _: next(inputs))

  main()
  stdout = capsys.readouterr()

  assert stdout.out == expected_4_3_3_4_0

