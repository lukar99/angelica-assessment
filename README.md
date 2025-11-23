# Polkadot Score Calculator

This project calculates the "Polkadot Score" based on the contents of a text file (`angelica.txt`). The score is determined by counting occurrences of the character `O` in the file, with special rules applied to certain sections of the text.

## Features

- Reads the input file `angelica.txt`.
- Identifies a specific substring (`~~~~~~'`) referred to as "lips".
- Counts occurrences of the character `O`:
  - `O` within the "lips" section counts as 2 points.
  - `O` outside the "lips" section counts as 1 point.
- Outputs the total Polkadot Score.
