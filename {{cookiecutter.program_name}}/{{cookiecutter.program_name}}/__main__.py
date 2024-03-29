import typer
from {{cookiecutter.program_name}}.logger import init_logger, logger, console
from {{cookiecutter.program_name}} import __version__

app = typer.Typer(
    add_completion=False,
    rich_markup_mode='rich',
    context_settings={'help_option_names': ['-h', '--help']},
    pretty_exceptions_show_locals=False
)


@app.command(no_args_is_help=True, help='{{cookiecutter.program_name}} help!')
def main(
    debug: bool = typer.Option(False, '--debug', help='Enable [green]DEBUG[/] output')):

    init_logger(debug)


if __name__ == '__main__':
    app(prog_name='{{cookiecutter.program_name}}')
