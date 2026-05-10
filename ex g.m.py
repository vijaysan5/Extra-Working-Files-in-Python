import tkinter as tk
from tkinter import messagebox
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)

root = tk.Tk()
root.title("Tic Tac Toe")

player = "X"
board = [""] * 9

def win():
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]

    for a,b,c in wins:
        if board[a] == board[b] == board[c] != "":
            return board[a]

    if "" not in board:
        return "Tie"

def click(i):
    global player
    if board[i] == "":
        board[i] = player
        btns[i]["text"] = player

        w = win()

        if w:
            messagebox.showinfo("Result", "Tie!" if w == "Tie" else f"{w} Wins!")
            reset()
            return

        player = "O" if player == "X" else "X"
        status["text"] = f"{player}'s Turn"

def reset():
    global player, board
    player = "X"
    board = [""] * 9

    for b in btns:
        b["text"] = ""
    status["text"] = "X's Turn"

btns = []

for i in range(9):
    b = tk.Button(root, font=("Arial",20), width=5, height=2, command=lambda i=i: click(i))
    b.grid(row=i//3, column=i%3)
    btns.append(b)

status = tk.Label(root, text="X's Turn", font=("Arial",14))
status.grid(row=3, column=0, columnspan=3)

tk.Button(root, text="Restart", command=reset)\
    .grid(row=4, column=0, columnspan=3)

class Login(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Player Entry")
        self.setGeometry(500, 200, 300, 200)

        QLabel("Name:", self).move(30, 40)
        self.name = QLineEdit(self)
        self.name.move(100, 40)

        QLabel("Age:", self).move(30, 80)
        self.age = QLineEdit(self)
        self.age.move(100, 80)

        btn = QPushButton("Enter", self)
        btn.move(100, 130)
        btn.clicked.connect(self.check_age)

    def check_age(self):
        name = self.name.text()
        age = self.age.text()

        if not age.isdigit():
            QMessageBox.warning(self, "Error", "Enter valid age")
            return
        if int(age) >= 10:
            QMessageBox.information(self, "Welcome", f"Welcome {name}")
            self.close()
            root.mainloop()

        else:
            QMessageBox.warning(self, "Invalid", "Age is not valid")

app = QApplication(sys.argv)

window = Login()
window.show()
sys.exit(app.exec_())