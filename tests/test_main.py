import sys
from context import main


def test_correct_usage(capfd):
    sys.argv = ["main.py", "27"]
    main()
    out, err = capfd.readouterr()
    assert out == "[20, 5, 2]\n"


def test_no_args_passed(capfd):
    sys.argv = ["main.py"]
    main()
    out, err = capfd.readouterr()
    assert out == "Please pass an argument\n"
