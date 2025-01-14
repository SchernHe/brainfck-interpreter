import pytest
from brainfck_interpreter.interpreter import BFInterpreter


@pytest.fixture(scope="function")
def interpreter():
    """Provide an instance of the interpreter fixture."""
    yield BFInterpreter(128)


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


class TestExtractInstructions:
    """Test extaction of the valid BF command sequence."""

    def test_extract_instructions(self, interpreter: BFInterpreter):
        """Extract the instructions from a raw input string containing only bf variables."""
        cmd_sequence = interpreter.extract_instructions("[->+<].,")
        expected_output = ["[", "-", ">", "+", "<", "]", ".", ","]
        assert cmd_sequence == expected_output

    def test_extract_instructions_with_comments(self, interpreter: BFInterpreter):
        """Extract the instructions from a raw input string containing non-bf variables."""
        cmd_sequence = interpreter.extract_instructions("qwrqr[wrqa-afasd>asfdf+asdadasa<s]a")
        expected_output = ["[", "-", ">", "+", "<", "]"]
        assert cmd_sequence == expected_output


class TestInterpretation:
    """Test interpretation of bf code."""

    def test_jump_forward(self, interpreter: BFInterpreter):
        """Jump forward adjusts instruction pointer correctly."""
        cmd_sequence = ["-", "[", "-", ">", "+", "<", "]", "-"]

        interpreter.ip = 1
        interpreter.jump_forward(cmd_sequence)

        assert interpreter.ip == 6
        assert cmd_sequence[interpreter.ip] == "]"

    def test_jump_forward_raises_ValueError_closing_not_found(self, interpreter: BFInterpreter):
        """Jump forward raises error if no closing bracket can be found in remaining instructions."""
        cmd_sequence = ["-", "[", "-", ">", "+", "<", "-"]
        interpreter.ip = 1

        with pytest.raises(ValueError):
            interpreter.jump_forward(cmd_sequence)

    def test_jump_backward(self, interpreter: BFInterpreter):
        """Jump backward adjusts instruction pointer correctly."""
        cmd_sequence = ["-", "[", "-", ">", "+", "<", "]", "-"]

        interpreter.ip = 6
        interpreter.loop_open = True
        interpreter.jump_backwards(cmd_sequence)

        assert interpreter.ip == 1
        assert cmd_sequence[interpreter.ip] == "["

    def test_jump_backward_raises_ValueError_without_open_loop(self, interpreter: BFInterpreter):
        """Jump backward raises error if no loop was not opened prior."""
        cmd_sequence = ["-", "-", ">", "+", "<", "]", "-"]
        with pytest.raises(ValueError):
            interpreter.jump_backwards(cmd_sequence)

    def test_interpret_without_loop(self, interpreter: BFInterpreter):
        """Interpreter a simple instruction sequence without loops."""
        cmd_sequence = ("+" * 72 + ".") + ">" + ("+" * 69 + ".") + "<" + ("+" * 4 + "." + ".") + ("+++" + ".")
        expected_result = "HELLO"
        assert interpreter.interpret(cmd_sequence) == expected_result

    def test_interpret_with_loop(self, interpreter: BFInterpreter):
        """Interpreter returns `Hello!` correctly."""
        cmd_sequence = "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++.>+.+++++++..+++.<<+++."
        expected_result = "Hello!"
        assert interpreter.interpret(cmd_sequence) == expected_result
