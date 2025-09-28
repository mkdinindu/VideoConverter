import sys, subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QComboBox, QProgressBar

class VideoConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("buntu video")
        self.layout = QVBoxLayout()

        self.file_label = QLabel("No file selected")
        self.layout.addWidget(self.file_label)

        self.select_button = QPushButton("Select Video")
        self.select_button.clicked.connect(self.select_file)
        self.layout.addWidget(self.select_button)

        self.format_box = QComboBox()
        self.format_box.addItems(["mp4", "avi", "mkv", "mov"])
        self.layout.addWidget(self.format_box)

        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.convert_video)
        self.layout.addWidget(self.convert_button)

        self.progress = QProgressBar()
        self.layout.addWidget(self.progress)

        self.setLayout(self.layout)

    def select_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select Video")
        if file:
            self.file_path = file
            self.file_label.setText(file)

    def convert_video(self):
        output_format = self.format_box.currentText()
        output_file = self.file_path.rsplit(".", 1)[0] + f".{output_format}"
        command = ["ffmpeg", "-i", self.file_path,
    "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2",
    output_file]
        subprocess.run(command)
        self.progress.setValue(100)
        self.file_label.setText(f"Converted: {output_file}")

app = QApplication(sys.argv)
window = VideoConverter()
window.show()
sys.exit(app.exec_())