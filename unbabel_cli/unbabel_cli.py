import click
from translations_metrics.sma import sma_translations_process


# TODO: add another option for metric entry types (e.g. avg, wpm)
# TODO: add --verbose arg to explain the cli

@click.group(invoke_without_command=True)
@click.option('-i', '--input_file', default='',
              type=click.Path(exists=True, file_okay=True),
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

    # window should be positive
    if window_size <= 0:
        raise click.UsageError('-w, -window_size must be greater than 0')

    # to share between tasks (e.g. sma)
    ctx.ensure_object(dict)
    ctx.obj['cli_shared_data'] = {
         'input_file': input_file,
         'window_size': window_size,
    }

    cli.add_command(sma_translations_process)
    ctx.invoke(sma_translations_process)


if __name__ == '__main__':
    cli(obj={})