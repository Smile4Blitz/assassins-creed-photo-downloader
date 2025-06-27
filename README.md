# Assassin's Creed Photo Mode Downloader

Download all your **Assassin's Creed Photo Mode** images from the Ubisoft website.

## 🛠 Requirements

- [Python](https://www.python.org/downloads/)
- [Firefox](https://www.firefox.com/)

## 💻 Windows Executable (No Python Needed)

If you don't want to install Python, you can use the standalone .exe:

1. Download & run the latest .exe from the Releases page.
2. A Firefox window will open - log in to your Ubisoft account.
3. Once logged in, return to the terminal and press Enter.
4. The script will reload the page and download each photo.

📁 The photos will be saved in a folder named:
```
Assassin's Creed <Game Name> - My Photos
```

Note: If any photo fails to download, its URL will be printed so you can download it manually.

## ⚙️ Manual Setup

1. **Clone the repo**

```bash
git clone https://github.com/smile4blitz/assassins-creed-photo-downloader.git
cd assassins-creed-photo-downloader
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv

# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

3. **Install the dependencies**

```bash
pip install -r requirements.txt
```

4. Run the script:

```bash
python assassins-creed-photo-downloader.py
```

5. A Firefox window will open - log in to your Ubisoft account.
6. Once logged in, return to the terminal and press Enter.
7. The script will reload the page and download each photo.

📁 The photos will be saved in a folder named:
```
Assassin's Creed <Game Name> - My Photos
```

Note: If any photo fails to download, its URL will be printed so you can download it manually.

## 🧾 License

MIT License

## Note

Disclaimer: This tool is unofficial and not affiliated with or endorsed by Ubisoft. All trademarks and logos are the property of their respective owners.
