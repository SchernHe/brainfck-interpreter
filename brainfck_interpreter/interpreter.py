class BFInterpreter:
    def __init__(self, memory_size: int = 256) -> None:
        """Initialize the interpreter."""
        self.stack = [0] * memory_size
        self.cp = 0
        self.ip = 0

    def interpret(self, cmd_sequence: str) -> str:
        """Interpret the BF command.

        Parameters
        ----------
        cmd_sequence : str
            Command sequence to-be interpreted.

        Returns
        -------
        str
            Interpretation of the command sequence (sys.out).
        """
        return ""
