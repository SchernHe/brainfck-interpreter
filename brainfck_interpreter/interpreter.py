"""Implementation of the brainf*ck interpreter."""

import logging
from typing import List


logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)

VALID_VOCABULARY: List[str] = [">", "<", "+", "-", ".", ",", "[", "]"]


class BFInterpreter:
    def __init__(self, memory_size: int = 256) -> None:
        """Initialize the interpreter."""
        self.stack = [0] * memory_size
        self.cp = 0
        self.ip = 0

    def interpret(self, raw_input: str) -> str:
        """Interpret the BF command.

        Parameters
        ----------
        raw_input : str
            Command sequence to-be interpreted.

        Returns
        -------
        str
            Interpretation of the command sequence (sys.out).
        """
        return ""

    def extract_sequence(self, raw_input: str) -> List[str]:
        """Extract the commands from the raw input string.

        Parameters
        ----------
        raw_input : str
            Raw brainf*ck command sequence. This might contain comments and other non-bf
            characters.

        Returns
        -------
        List[str]
            Parsed sequence of bf commands.
        """
        cmd_sequence: List[str] = []

        for cmd_char in raw_input:
            if cmd_char not in VALID_VOCABULARY:
                logger.debug(f"Skipped: {cmd_char}")
            else:
                cmd_sequence.append(cmd_char)

        return cmd_sequence
