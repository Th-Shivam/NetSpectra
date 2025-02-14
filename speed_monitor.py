import tkinter as tk
from tkinter import ttk
import speedtest
import threading
import time

class SpeedMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Internet Speed Monitor")
        self.root.geometry("400x200")
        self.root.resizable(False, False)

        # Initialize variables
        self.download_speed = tk.StringVar()
        self.upload_speed = tk.StringVar()
        self.ping = tk.StringVar()

        # Set default values
        self.download_speed.set("0.00 Mbps")
        self.upload_speed.set("0.00 Mbps")
        self.ping.set("0.00 ms")

        # Create GUI elements
        self.create_widgets()

        # Start the speed monitoring thread
        self.monitor_speed()

    def create_widgets(self):
        # Title Label
        title_label = tk.Label(self.root, text="Real-Time Internet Speed", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # Download Speed Label
        download_label = tk.Label(self.root, text="Download Speed:", font=("Arial", 12))
        download_label.pack(anchor="w", padx=20)
        download_value = tk.Label(self.root, textvariable=self.download_speed, font=("Arial", 12, "bold"))
        download_value.pack(anchor="w", padx=20)

        # Upload Speed Label
        upload_label = tk.Label(self.root, text="Upload Speed:", font=("Arial", 12))
        upload_label.pack(anchor="w", padx=20)
        upload_value = tk.Label(self.root, textvariable=self.upload_speed, font=("Arial", 12, "bold"))
        upload_value.pack(anchor="w", padx=20)

        # Ping Label
        ping_label = tk.Label(self.root, text="Ping:", font=("Arial", 12))
        ping_label.pack(anchor="w", padx=20)
        ping_value = tk.Label(self.root, textvariable=self.ping, font=("Arial", 12, "bold"))
        ping_value.pack(anchor="w", padx=20)

    def monitor_speed(self):
        def update_speed():
            while True:
                try:
                    st = speedtest.Speedtest()
                    st.get_best_server()

                    # Measure download speed
                    download = st.download() / 1_000_000  # Convert to Mbps
                    self.download_speed.set(f"{download:.2f} Mbps")

                    # Measure upload speed
                    upload = st.upload() / 1_000_000  # Convert to Mbps
                    self.upload_speed.set(f"{upload:.2f} Mbps")

                    # Measure ping
                    ping = st.results.ping
                    self.ping.set(f"{ping:.2f} ms")
                except Exception as e:
                    self.download_speed.set("Error")
                    self.upload_speed.set("Error")
                    self.ping.set("Error")

                # Wait for 5 seconds before updating again
                time.sleep(5)

        # Run the speed test in a separate thread to avoid freezing the GUI
        threading.Thread(target=update_speed, daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedMonitorApp(root)
    root.mainloop()