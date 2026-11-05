from main import print_box

def test_print_box(capsys):
    print_box()
    stdout = capsys.readouterr()

    expected = (
                 "**********\n"
                 "*        *\n"
                 "**********\n"
               )

    assert stdout.out == expected 

