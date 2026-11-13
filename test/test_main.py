from main import main

expected_3_3 = "***\n* *\n***\n"


def test_one_input(monkeypatch, capsys):
    inputs = iter(["3", "3", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    main()
    stdout = capsys.readouterr()

    assert stdout.out == expected_3_3


def test_one_input_late_exit(monkeypatch, capsys):
    inputs = iter(["3", "3", "2", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main()
    stdout = capsys.readouterr()

    assert stdout.out == expected_3_3