# Brainfck-Interpreter

Python implementation of the brainf*ck interpreter first published by Urban Müller.

## About the interpreter

- Consists of ...
  - 8 commands
  - data pointer
  - instruction pointer
- Turing-complete i.e. can be used to write any program, but unhandy becasue little abstraction

## Commands

- `>` Move ponter to the right
- `<` Move pointer to the left
- `+` Increment memory cell at the pointer
- `-` Decrement memory cell at the pointer
- `.` Output the character signified by the cell at the pointer
- `,` Input a character and store it in the cell a the pointer
- `[` Jump past the matching `]`if the cell at the pointer is `0`
- `]` Jump back to the matching `]` if the cell at the pointer is nonzero

Any other characters are considered to be comments and ignored.

## Links

- <https://codingchallenges.fyi/challenges/challenge-brainfuck>
- <https://en.wikipedia.org/wiki/Brainfuck>
- <https://gist.github.com/rdebath/0ca09ec0fdcf3f82478f>
- <https://github.com/CodingChallengesFYI/SharedSolutions>

## Credits

This repository is a result of [Coding Challenges](https://codingchallenges.fyi/) by John Crickett.
