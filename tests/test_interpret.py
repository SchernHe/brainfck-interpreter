from brainfck_interpreter.interpret import interpret_command


def test_interpret_returns_hello_world():
    """Interpreter returns `Hello!` correctly."""
    cmd_sequence = (
        "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++.>+.+++++++..+++.<<+++."
    )
    expected_result = "Hello!"
    assert interpret_command(cmd_sequence) == expected_result
