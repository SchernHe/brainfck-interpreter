"""Entrypoint for the brainf*ck interpreter."""

import click
from pathlib import Path

from brainfck_interpreter.interpreter import BFInterpreter


@click.command()
@click.option(
    "--file_path",
    prompt="Brainf*ck file path",
)
def interpret_command(file_path: str):
    """Entrypoint to interpret a brainf*ck command sequence from file.

    Parameters
    ----------
    file_path : str
        Path containing the Brainf*ck command sequence.
    """
    raw_input = Path(file_path).read_text()

    interpreter = BFInterpreter()
    output = interpreter.interpret(raw_input)
    click.echo(output)
