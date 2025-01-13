"""Entrypoint for the brainf*ck interpreter."""

import click


@click.command()
@click.option("--file_path", prompt="Brainf*ck file path")
def interpret_command(file_path: str) -> str:
    """Entrypoint to interpret a brainf*ck command sequence from file.

    Parameters
    ----------
    file_path : str
        Path containing the Brainf*ck command sequence.

    Returns
    -------
    str
        Interpretation of the command sequence (sys.out).
    """
    return ""
