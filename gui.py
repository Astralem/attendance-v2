from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from attendance import record_attendance

class AttendanceUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Attendance Scanner")
        self.setGeometry(0, 0, 500, 500)

        title = QLabel("📋 Attendance System")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 16, QFont.Bold))

        subtitle = QLabel("Scan your barcode to time in")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("color: gray;")

        self.input = QLineEdit()
        self.input.setPlaceholderText("Student ID")
        self.input.setAlignment(Qt.AlignCenter)
        self.input.setFont(QFont("Segoe UI", 12))
        self.input.returnPressed.connect(self.scan_id)

        self.result = QLabel("Waiting for scan...")
        self.result.setAlignment(Qt.AlignCenter)

        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background: white;
                border-radius: 12px;
                padding: 20px;
            }
        """)

        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(12)
        card_layout.addWidget(title)
        card_layout.addWidget(subtitle)
        card_layout.addSpacing(10)
        card_layout.addWidget(self.input)
        card_layout.addWidget(self.result)

        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(card)
        layout.addStretch()

        self.setLayout(layout)

        self.setStyleSheet("""
            QWidget { background: #f2f4f8; }
            QLineEdit {
                padding: 10px;
                border-radius: 8px;
                border: 1px solid #ccc;
            }
            QLineEdit:focus {
                border: 1px solid #4a90e2;
            }
        """)

    def scan_id(self):
        student_id = self.input.text().strip()

        if not student_id.isdigit():
            self.result.setText("❌ Invalid ID")
            self.result.setStyleSheet("color: red;")
            self.input.clear()
            return

        message = record_attendance(int(student_id))
        self.result.setText("✅ " + message)
        self.result.setStyleSheet("color: green;")
        self.input.clear()
