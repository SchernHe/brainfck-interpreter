import pytest
from brainfck_interpreter.interpreter import BFInterpreter


@pytest.fixture(scope="function")
def interpreter():
    yield BFInterpreter(128)


def test_interpreter_returns_hello_world_correctly():
    """Interpreter returns `Hello!` correctly."""
    cmd_sequence = "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++.>+.+++++++..+++.<<+++."
    expected_result = "Hello!"
    assert BFInterpreter().interpret(cmd_sequence) == expected_result


class TestInitializeBFInterpreter:
    """Test initialization of the BFInterpreter."""

    def test_initialize_correct_memory(self, interpreter: BFInterpreter):
        """Memory is initialized correctly."""
        assert len(interpreter.stack) == 128
        assert sum(interpreter.stack) == 0

    def test_initialize_correct_pointer(self, interpreter: BFInterpreter):
        """Pointers are initialized correctly."""
        assert interpreter.cp == 0
        assert interpreter.ip == 0


class TestCommandSequencExtraction:
    """Test extaction of the valid BF command sequence."""

    def test_extract_sequence(self, interpreter: BFInterpreter):
        """Extract the commands from a raw input string containing only bf variables."""
        cmd_sequence = interpreter.extract_sequence("[->+<].,")
        expected_output = ["[", "-", ">", "+", "<", "]", ".", ","]
        assert cmd_sequence == expected_output

    def test_extract_sequence_with_comments(self, interpreter: BFInterpreter):
        """Extract the commands from a raw input string containing non-bf variables."""
        cmd_sequence = interpreter.extract_sequence("qwrqr[wrqa-afasd>asfdf+asdadasa<s]a")
        expected_output = ["[", "-", ">", "+", "<", "]"]
        assert cmd_sequence == expected_output
