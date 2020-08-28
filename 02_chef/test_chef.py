from unittest import mock
import random

q = ''.join(chr(random.randint(ord('a'), ord('z'))) for i in range(32))
@mock.patch('builtins.input', side_effect=[q])
def test_run(input, capsys):
    import chef

    captured = capsys.readouterr()
    lines = captured.out.split('\n')
    assert len(lines) > 1
    assert lines[-2] == f'WAS MEINST DU MIT "{q.upper()}"?!? DU BIST GEFEUERT!'
