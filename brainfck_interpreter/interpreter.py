"""Implementation of the brainf*ck interpreter."""

import logging
from typing import List


logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)

VALID_VOCABULARY: List[str] = [">", "<", "+", "-", ".", ",", "[", "]"]


class BFInterpreter:
    def __init__(self, memory_size: int = 256) -> None:
        """Initialize the interpreter."""

        self.stack = [0] * memory_size
        """Memory stack."""

        self.cp = 0
        """Cell pointer."""

        self.ip = 0
        """Instructions pointer."""

        self.loop_open = False
        """Flag indicating whether pointer is currently within a loop."""

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
        sys_out: str = ""
        cmd_sequence = self.extract_instructions(raw_input)

        self._reset()

        while self.ip < len(cmd_sequence):
            cmd = cmd_sequence[self.ip]

            if cmd == "[":
                if self.stack[self.cp] == 0:
                    self.jump_forward(cmd_sequence)
                else:
                    self.loop_open = True
            elif cmd == "]":
                if self.stack[self.cp] > 0:
                    self.jump_backwards(cmd_sequence)
                else:
                    self.loop_open = False
            elif cmd == ">":
                self.cp += 1
            elif cmd == "<":
                self.cp -= 1
            elif cmd == "+":
                self.stack[self.cp] += 1
            elif cmd == "-":
                self.stack[self.cp] -= 1
            elif cmd == ".":
                sys_out += chr(self.stack[self.cp])
            elif cmd == ",":
                raise NotImplementedError("BF command `,` not implemented yet")

            self.ip += 1

        return sys_out

    def jump_forward(self, cmd_sequence: List[str]) -> None:
        """Jump forward to closing `]`.

        Parameters
        ----------
        cmd_sequence : List[str]
            Parsed sequence of bf commands.
        """
        cmd_subset = cmd_sequence[self.ip : :]
        increment = next((idx for idx, cmd in enumerate(cmd_subset) if cmd == "]"), -1)

        if increment < 0:
            raise ValueError("Missing closing bracket `]`!")

        self.ip += increment

    def jump_backwards(self, cmd_sequence: List[str]) -> None:
        """Jump backwards to opening `[`.

        Parameters
        ----------
        cmd_sequence : List[str]
            Parsed sequence of bf commands.
        """
        if not self.loop_open:
            raise ValueError("Missing opening bracket `[`!")

        cmd_subset = cmd_sequence[: (self.ip + 1)]
        decrement = next((idx for idx, cmd in enumerate(reversed(cmd_subset)) if cmd == "["), -1)

        self.ip -= decrement

    def extract_instructions(self, raw_input: str) -> List[str]:
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

    def _reset(self) -> None:
        """Reset memory stack and pointer."""
        self.stack = [0] * len(self.stack)
        self.ip = 0
        self.cp = 0
        self.loop_open = False
