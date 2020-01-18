from baidu_transl.cli import run

import termcolor
from click.testing import CliRunner

INPUT = 'Small things make base men proud.'

def test_run():
    runner = CliRunner()
    result = runner.invoke(run, [INPUT])
    assert not result.exception
    print(termcolor.colored(f'{test_run.__name__}', 'green'), f': {result}')


if __name__ == '__main__':
    test_run()
