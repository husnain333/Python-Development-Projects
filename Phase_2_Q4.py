import sounddevice as sd
import numpy as np
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

class VoiceRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Recorder")

        self.is_recording = False
        self.recording_data = []
        self.fs = 44100  # Sample rate

        # GUI components
        self.record_button = tk.Button(root, text="Record", command=self.toggle_recording)
        self.save_button = tk.Button(root, text="Save", command=self.save_recording)
        self.record_button.pack(pady=10)
        self.save_button.pack(pady=10)

        # Configure sounddevice
        sd.default.samplerate = self.fs
        sd.default.channels = 1

    def start_recording(self):
        self.is_recording = True
        self.recording_data = []

        def callback(indata, frames, time, status):
            if status:
                print('Error:', status)
            if self.is_recording:
                self.recording_data.extend(indata.copy())

        with sd.InputStream(callback=callback):
            self.root.wait_variable(self.is_recording_var)

    def stop_recording(self):
        self.is_recording = False

    def toggle_recording(self):
        if not self.is_recording:
            self.is_recording_var = tk.BooleanVar()
            self.is_recording_var.set(True)
            self.record_button.configure(text="Stop Recording", command=self.stop_recording)
            self.save_button.configure(state="disabled")
            self.start_recording()
        else:
            self.is_recording_var.set(False)
            self.record_button.configure(text="Record", command=self.toggle_recording)
            self.save_button.configure(state="normal")

    def save_recording(self):
        if not self.recording_data:
            return

        filename = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])

        if filename:
            sd.write(filename, np.vstack(self.recording_data))

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceRecorderApp(root)
    root.mainloop()
