import chess

def evaluate_board(board, weights_dict):
    if board.is_checkmate():
        if board.turn == chess.WHITE:
            return -float('inf') # Đen thắng (Trắng bị chiếu hết)
        else:
            return float('inf')  # Trắng thắng (Đen bị chiếu hết)
    
    if board.is_stalemate() or board.is_insufficient_material():
        return 0

    # Tính điểm vật chất cơ bản
    score = 0
    
    # Đếm và tính điểm cho từng loại quân
    piece_types = {
        chess.PAWN: "pawn",
        chess.KNIGHT: "knight", 
        chess.BISHOP: "bishop",
        chess.ROOK: "rook",
        chess.QUEEN: "queen",
        chess.KING: "king"
    }
    
    for piece_type, weight_key in piece_types.items():
        white_pieces = len(board.pieces(piece_type, chess.WHITE))
        black_pieces = len(board.pieces(piece_type, chess.BLACK))
        score += weights_dict[weight_key] * (white_pieces - black_pieces)
    
    # Thêm bonus cho vị trí trung tâm
    center_squares = [chess.D4, chess.D5, chess.E4, chess.E5]
    for square in center_squares:
        piece = board.piece_at(square)
        if piece:
            if piece.color == chess.WHITE:
                score += 1
            else:
                score -= 1
    
    # Bonus cho di chuyển (mobility)
    current_turn = board.turn
    
    # Đếm số nước đi hợp lệ cho trắng
    if current_turn == chess.WHITE:
        white_mobility = len(list(board.legal_moves))
        board.turn = chess.BLACK
        black_mobility = len(list(board.legal_moves))
        board.turn = chess.WHITE
    else:
        black_mobility = len(list(board.legal_moves))
        board.turn = chess.WHITE
        white_mobility = len(list(board.legal_moves))
        board.turn = chess.BLACK
    
    score += (white_mobility - black_mobility) * 0.1
    
    # Hàm phải trả về điểm từ góc nhìn của Trắng
    return score