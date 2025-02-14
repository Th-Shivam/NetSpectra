# 📡 NetSpectra: Real-Time Internet Speed Monitor

**Stay connected, stay informed.**

NetSpectra is a lightweight, real-time internet speed monitoring app built with Python. Track your download speed, upload speed, and ping without opening a single browser tab.

## 🚀 Features

- ⚡ **Real-Time Monitoring**: Get instant insights into your internet performance.
- 🎯 **Minimal Interface**: Clean and straightforward design.
- 🛠️ **Auto-Refresh Every 5 Seconds**: No manual checks required.
- 🧠 **Python-Powered**: Built using Tkinter and Speedtest.

## 🛠️ Installation

```bash
# Clone this repository
git clone https://github.com/th-shivam/netspectra.git
cd netspectra

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 📋 Requirements

- Python 3.x
- Tkinter (comes with Python)
- Speedtest CLI

**`requirements.txt`**

```
speedtest-cli==2.1.3
```

## 🚀 Usage

```bash
# Run the application
python speed_monitor.py
```

## 📊 How It Works

1. **Download Speed**: Measures download speed in Mbps.
2. **Upload Speed**: Measures upload speed in Mbps.
3. **Ping**: Tracks network latency in milliseconds.

The app automatically updates every 5 seconds, giving you real-time insights without interruptions.

## ⚠️ Troubleshooting

- If you encounter `externally-managed-environment` errors on Linux, use a virtual environment or `pipx` as recommended.
- Ensure your internet connection is active while running the app.

## 🙌 Contributing

Feel free to fork the repo, open issues, and submit PRs to enhance the app.

## 📖 License

This project is licensed under the MIT License.

**Created with ❤️ by SHIVAM **

---

*Monitor your internet like a pro with NetSpectra.*

