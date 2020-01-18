import click

from .run import trans

@click.command()
@click.argument('src')
@click.option('--from', '-f', 'from_',
              type=str,
              default='en',
              help='srouce language')
@click.option('--to', '-t',
              type=str,
              default='zh',
              help='target language')
def run(src: str,
        from_: str,
        to: str) -> None:
    trans(src, from_, to)
