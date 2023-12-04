import chess
import chess.svg
from io import StringIO
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()

# Create OpenAI client
client = OpenAI()
# Function to get a move from GPT-4
def get_gpt4_move(board, past_moves):
    # Convert the board to a string in a human-readable format
    board_s = board.epd # or board_s = str(board)
    #print(board_s)
    prompt = f"Chess game in progress. The past moves are: {' '.join(past_moves)}. Here is the current board in EPD:\n\n{board_s}\n\nGiven the current board, what should be the next move for {'white' if board.turn == chess.WHITE else 'black'} in Standard Algebraic Notation (SAN). Return NOTHING ELSE but the move in SAN in your response."
    try:
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a chess grandmaster."},
                {
                    "role": "user",
                    "content": prompt
                }
                    ],
            temperature=0.25,
            max_tokens=10
        )
        move = response.choices[0].message.content.strip()
        print(move)
        return move
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to make a move on the board
def make_move(board, move):
    try:
        board.push_san(move)
    except ValueError:
        print("Invalid move. Please try again.")
        return False
    return True

# Function to print the board to the console
def print_board(board):
    print()
    print(board)

# Main game loop
def play_game():
    board = chess.Board()
    past_moves = []

    while not board.is_game_over():
        # User's turn
        print_board(board)
        user_move = input("Your move: ")
        if make_move(board, user_move):
            past_moves.append(user_move)
        else:
            continue

        # GPT-4's turn
        gpt4_move = None
        while gpt4_move is None:
            gpt4_move = get_gpt4_move(board, past_moves)
            if gpt4_move and make_move(board, gpt4_move):
                past_moves.append(gpt4_move)
                print(f"GPT-4's move: {gpt4_move}")

                # funny comment
                board_s = board.epd
                prompt = f"Generate a brief, short competitive funny/clever comment. One sentence, 30 tokens max. You are playing me in a game of chess. This is the board: {board_s}. You have just made this move {gpt4_move}"
                response = client.chat.completions.create(
                    model="gpt-4-1106-preview",
                    messages=[
                        {"role": "system", "content": "You are a chess grandmaster."},
                        {
                            "role": "user",
                            "content": prompt
                        }
                            ],
                    temperature=1.2,
                    max_tokens=30
                )
                print(response.choices[0].message.content)
            else:
                print("GPT-4 made an invalid move, trying again...")
                gpt4_move = None

    print("Game over.")
    print("Result: " + board.result())

if __name__ == "__main__":
    play_game()