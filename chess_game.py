import chess

def print_board_with_border(board):
    board_str = str(board)
    rows = board_str.split('\n')

    print("    a   b   c   d   e   f   g   h")
    print("  +---+---+---+---+---+---+---+---+")
    
    for i in range(8):
        row_number = 8 - i
        row = rows[i].split(" ")
        print(f"{row_number} | " + " | ".join(row) + " |")
        print("  +---+---+---+---+---+---+---+---+")

def main():
    board = chess.Board()

    print("♟️ Welcome to Console Chess Game ♟️")
    print("Moves should be in UCI format (e.g., e2e4, g1f3)")
    print("Type 'quit' to exit the game.\n")

    print_board_with_border(board)

    while not board.is_game_over():
        print(f"\n{board.turn and 'White' or 'Black'}'s turn:")
        move_input = input("Enter your move: ").strip()

        if move_input.lower() == 'quit':
            print("Game ended by user.")
            break

        try:
            move = chess.Move.from_uci(move_input)
            if move in board.legal_moves:
                board.push(move)
                print_board_with_border(board)
            else:
                print("❌ Illegal move. Try again.")
        except:
            print("❌ Invalid input. Use UCI format (e.g., e2e4).")

    if board.is_game_over():
        print("\n🏁 Game Over!")
        print(f"Result: {board.result()}")
        if board.is_checkmate():
            print("Checkmate!")
        elif board.is_stalemate():
            print("Stalemate!")
        elif board.is_insufficient_material():
            print("Draw: Insufficient material.")
        elif board.is_seventyfive_moves():
            print("Draw: 75-move rule.")
        elif board.is_fivefold_repetition():
            print("Draw: Fivefold repetition.")

if __name__ == "__main__":
    main()
