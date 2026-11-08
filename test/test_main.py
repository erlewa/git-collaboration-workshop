from main import main

expected_3_3 = (
 "***\n"
 "* *\n"
 "***\n"
)

def test_one_input(monkeypatch, capsys):
  monkeypatch.setattr("builtins.input", lambda _: "3")
  monkeypatch.setattr("builtins.input", lambda _: "3")
  monkeypatch.setattr("builtins.input", lambda _: "0")
  main()
  stdout = capsys.readouterr()

  assert stdout.out == expected_3_3 


def test_one_input_late_exit(monkeypatch, capsys):
  monkeypatch.setattr("builtins.input", lambda _: "3")
  monkeypatch.setattr("builtins.input", lambda _: "3")
  monkeypatch.setattr("builtins.input", lambda _: "2")
  monkeypatch.setattr("builtins.input", lambda _: "0")

  main()
  stdout = capsys.readouterr()

  assert stdout.out == expected_3_3 
