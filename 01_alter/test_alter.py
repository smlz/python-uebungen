from unittest import mock


@mock.patch('builtins.input', side_effect=['18'])
def test_compile(input, capsys):
    import alter
    import sys

    captured = capsys.readouterr()
    lines = captured.out.split('\n')
    done = False
    i = iter(lines)
    days = False
    while not done:
        try:
            line = next(i)
        except StopIteration:
            done = True

        if 'tag' in line.lower():
            try:
                days = int(next(i))
            except StopIteration:
                done = True
            except ValueError:
                pass
    assert days > 6400
    assert days < 6700

    done = False
    i = iter(lines)
    hours = False
    while not done:
        try:
            line = next(i)
        except StopIteration:
            done = True

        if 'stund' in line.lower():
            try:
                hours = int(next(i))
            except StopIteration:
                done = True
            except ValueError:
                pass
    assert hours > 150000
    assert hours < 160000
