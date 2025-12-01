# 🏆 Chess AI Project - Hoàn thiện với Minimax & Battle System

Dự án AI Cờ Vua sử dụng thuật toán **Minimax với Alpha-Beta Pruning** và **Neural Network** để tạo ra các AI agents có khả năng chơi cờ ở các mức độ khác nhau. Ngoài ra, dự án còn bao gồm hệ thống **AI Battle Arena** để so sánh giữa các agent.

## Cấu trúc Dự án

```
Chess-AI-Project/
├── 📁 assets/                    # Hình ảnh quân cờ
├── 📁 src/
│   ├── config.py                 # Cấu hình (trọng số, màu sắc, battle settings)
│   ├── evaluation.py             # Hàm đánh giá vị trí quân cờ
│   ├── engine.py                 # Minimax + Alpha-Beta + Quiescence
│   ├── game_view.py              # Giao diện game với Pygame
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
└── 📦 requirements.txt           # Dependencies
```

## Cài đặt

### 1. Cài đặt Python
Yêu cầu Python 3.

### 2. Cài đặt thư viện

```bash
python -m venv chess_game

pip install -r requirements.txt
```

## Sử dụng

**Tính năng:**
- Đấu Random Agent vs Minimax Agent hoặc Random Agent vs Machine Learning Agent
- Chọn độ sâu Minimax (1-3)
- Battle area giữa các Agent với nhiều ván đấu
- Thống kê chi tiết thắng/thua/hòa
- Đo thời gian thực thi
- Tùy chọn người chơi đấu với Minimax hay ML 

### 🤖 Huấn luyện AI
1. Mở file: src/chess_ML/Chess_ML.ipynb 
2. Nhấn "Run All" ở phía trên notebook
## Chạy chương trình

### Kích hoạt môi trường ảo
```bash
source chess_game/bin/activate   # Linux/MacOS
chess_game\Scripts\activate    # Windows
```

### 🚩 Chạy AI Battle Arena
```bash
python ai_battle.py
```

### 🎮 Chơi với AI
```bash
python play_game.py   #chơi với minimax agent

python play_game_ML.py #chơi với ML agent
```