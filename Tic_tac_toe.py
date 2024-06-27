import random

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(cell == player for cell in board[i]):  # Check rows
            return True
        if all(board[j][i] == player for j in range(3)):  # Check columns
            return True
    if all(board[i][i] == player for i in range(3)):  # Check diagonal (top-left to bottom-right)
        return True
    if all(board[i][2 - i] == player for i in range(3)):  # Check diagonal (top-right to bottom-left)
        return True
    return False

def available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, maximizing_player):
    if check_winner(board, "O"):  # AI wins
        return 10 - depth
    elif check_winner(board, "X"):  # Human wins
        return depth - 10
    elif not available_moves(board):  # Draw
        return 0

    if maximizing_player:
        max_eval = float("-inf")
        for i, j in available_moves(board):
            board[i][j] = "O"
            eval = minimax(board, depth + 1, False)
            board[i][j] = " "
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i, j in available_moves(board):
            board[i][j] = "X"
            eval = minimax(board, depth + 1, True)
            board[i][j] = " "
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_score = float("-inf")
    best_move = None
    for i, j in available_moves(board):
        board[i][j] = "O"
        score = minimax(board, 0, False)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are playing as 'X'.")
    print_board(board)

    while True:
        # Human player's turn
        while True:
            row, col = map(int, input("Enter row and column (e.g., 1 1 for top-left): ").split())
            if board[row - 1][col - 1] == " ":
                board[row - 1][col - 1] = "X"
                break
            else:
                print("That cell is already occupied. Try again.")
        print_board(board)

        # Check if human player wins or the game ends in a draw
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break
        elif not available_moves(board):
            print("It's a draw!")
            break

        # AI player's turn
        print("AI is making a move...")
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = "O"
        print_board(board)

        # Check if AI player wins or the game ends in a draw
        if check_winner(board, "O"):
            print("AI wins! Better luck next time.")
            break
        elif not available_moves(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
