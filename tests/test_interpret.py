from pathlib import Path

from brainfck_interpreter.interpret import interpret_command
from click.testing import CliRunner


class TestInterpretCommandCli:
    def test_interpret_from_path_successful(self, test_data: Path):
        """Interpretation from file path works."""
        runner = CliRunner()
        file_path = str(test_data / "hello_world.txt")

        result = runner.invoke(interpret_command, input=file_path)

        assert result.exit_code == 0
        assert "Hello, World!" in result.output

    def test_interpret_from_invalidpath_raises_error(self):
        """Interpretation from file path works."""
        runner = CliRunner(mix_stderr=False)
        file_path = "this-file-does-not-exist.txt"

        result = runner.invoke(interpret_command, input=file_path)

        assert result.exit_code == 1
        assert isinstance(result.exception, FileNotFoundError)
