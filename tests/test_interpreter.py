from brainfck_interpreter.interpreter import BFInterpreter


def test_interpreter_returns_hello_world_correctly():
    """Interpreter returns `Hello!` correctly."""
    cmd_sequence = (
        "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++.>+.+++++++..+++.<<+++."
    )
    expected_result = "Hello!"
    assert BFInterpreter().interpret(cmd_sequence) == expected_result


class TestInitializeBFInterpreter:
    """Test initialization of the BFInterpreter."""

    def test_initialize_correct_memory(self):
        """Memory is initialized correctly."""
        interpreter = BFInterpreter(128)
        assert len(interpreter.stack) == 128
        assert sum(interpreter.stack) == 0

    def test_initialize_correct_pointer(self):
        """Pointers are initialized correctly."""
        interpreter = BFInterpreter(128)
        assert interpreter.cp == 0
        assert interpreter.ip == 0
