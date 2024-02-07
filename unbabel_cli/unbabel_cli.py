import click
from translations_metrics.sma import sma_translations_process


# TODO: add another option for metric entry types (e.g. avg, wpm)

# https://click.palletsprojects.com/en/8.1.x/commands/
# /#group-invocation-without-command
@click.group(invoke_without_command=True)
@click.option('-i', '--input_file', default='',
              help='.JSON file expected', )
@click.option('-w', '--window_size', default=0, type=int,
              help='window size to SMA calculations', )
@click.pass_context
def cli(ctx: click.Context, input_file: str, window_size: int) -> None:
    """Manage input cli args and assign command tasks.

    :param ctx: click context
    :param input_file: file input via command line
    :param window_size: window ize input via command line
    """

    # to share between tasks (e.g. sma)
    ctx.ensure_object(dict)
    ctx.obj['cli_shared_data'] = {
         'input_file': input_file,
         'window_size': window_size,
    }
    click.echo(ctx.obj['cli_shared_data'].get('input_file'))
    cli.add_command(sma_translations_process)
    ctx.invoke(sma_translations_process)


if __name__ == '__main__':
    cli(obj={})