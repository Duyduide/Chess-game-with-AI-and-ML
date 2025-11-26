# 🏆 Chess AI Project - Hoàn thiện với Minimax & Battle System

Dự án AI Cờ Vua sử dụng thuật toán **Minimax với Alpha-Beta Pruning** và **AI Battle System** để so sánh hiệu suất các AI agents.

## Cấu trúc Dự án

```
Chess-AI-Project/
├── 📁 assets/                    # Hình ảnh quân cờ (đã có demo)
├── 📁 src/
│   ├── config.py                 # Cấu hình (trọng số, màu sắc, battle settings)
│   ├── evaluation.py             # Hàm đánh giá thông minh
│   ├── engine.py                 # Minimax + Alpha-Beta + Quiescence
│   ├── game_view.py              # UI Pygame với highlights
│   └── ai_battle.py              # Battle system
│   ├── 📁 chess_ML/                    # Module Machine Learning cho Chess Engine
│   │   ├── auxiliary_func.py           # Tiền xử lý nước đi, encode vị trí
│   │   ├── dataset.py                  # class Dataset
│   │   ├── model.py                    # Mô hình Neural Network dự đoán nước đi
│   │   ├── Chess_ML.ipynb              # Notebook huấn luyện / thử nghiệm
│   │   ├── 📁 data/                   # Dữ liệu PGN của các kỳ thủ top thế giới
│   │   ├── 📁 models/                 # Mô hình đã train
├── 🎮 play_game.py               # Game người vs AI minimax
├── 🎮 play_game_ML.py            # Game người vs ML agent
├── ⚔️ ai_battle.py               # AI Battle Arena
├── 🧪 test_engine.py             # Test Minimax engine
├── 🧪 test_battle.py             # Test battle system
└── 📦 requirements.txt           # Dependencies
```

## Cài đặt

### 1. Cài đặt Python
Yêu cầu Python 3.10 trở lên.

### 2. Cài đặt thư viện

```bash
python -m venv chess_game

pip install -r requirements.txt
```

### 3. Chuẩn bị hình ảnh quân cờ
Bạn cần cung cấp 12 file PNG trong thư mục `assets/`:
- `wP.png`, `wN.png`, `wB.png`, `wR.png`, `wQ.png`, `wK.png` (quân trắng)
- `bP.png`, `bN.png`, `bB.png`, `bR.png`, `bQ.png`, `bK.png` (quân đen)

## Sử dụng


**Tính năng:**
- Đấu Random AI vs Minimax AI và random AI vs ML AI
- Chọn độ sâu Minimax (1-3)
- Tournament với nhiều ván đấu
- Thống kê chi tiết thắng/thua/hòa
- Đo thời gian thực thi
- Tùy chọn người chơi đấu với Minimax hay ML 
### 🧪 Test hệ thống
```bash
python test_engine.py      # Test Minimax engine hoạt động tốt
python test_battle.py      # Test battle system  
```

### 🤖 Huấn luyện AI
1. Mở file: src/chess_ML/Chess_ML.ipynb 
2. Nhấn "Run All" ở phía trên notebook
## Chạy chương trình

### Chạy ngay để đấu giữa các AI:
```bash
python ai_battle.py
```

### 🎮 Chơi với AI
```bash
.\chess_game\Scripts\activate

python play_game.py   #chơi với minimax agent

python play_game_ML.py #chơi với ML agent
```
