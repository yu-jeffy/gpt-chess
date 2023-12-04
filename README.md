# gpt-chess
play chess with gpt-4! 💫


## Info

This program allows you to play a game of chess against GPT-4 or watch GPT-4 play against itself, complete with clever commentary on each move. It utilizes the `python-chess` library for managing the chess game state and the OpenAI API to interact with GPT-4.

## Features

- Play chess against GPT-4 in the terminal.
- Watch GPT-4 play against itself with amusing commentary.
- Terminal-based board display using Standard Algebraic Notation (SAN).
- Error handling for invalid moves.

## Installation

Before running the program, ensure you have Python installed on your system. Then, install the required Python packages using pip:

```bash
pip install python-chess openai python-dotenv
```

You'll also need to obtain an API key from OpenAI and set it in an `.env` file in the same directory as the script:

```plaintext
OPENAI_API_KEY='your_api_key_here'
```

## Usage

To play a game against GPT-4, run the `gptchess.py` script:

```bash
python gptchess.py
```

To watch GPT-4 play against itself, run the `gptchess-inception.py` script:

```bash
python gptchess-inception.py
```

During your turn, input your move in SAN when prompted. The board will update, and then GPT-4 will make its move.

## Notes

- Ensure your terminal window is wide enough to display the entire board.
- The program assumes familiarity with chess notation and rules.
- Each interaction with GPT-4 via the OpenAI API may incur costs, so monitor your usage accordingly.

## License

This project is open-source and available under the [MIT License](LICENSE).

Enjoy your game of chess with GPT-4!