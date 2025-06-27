from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time
from webdriver_manager.firefox import GeckoDriverManager

link = None
options = ["Origins", "Odyssey", "Valhalla", "Shadows"]

# Prompt user to select the game version
print("Select the Assassin's Creed game version for photo mode:")
for i, option in enumerate(options, 1):
    print(f"{i}. Assassin's Creed - {option}")

while True:
    choice = input("Select an option (1-4): ")
    if choice in [str(i) for i in range(1, len(options) + 1)]:
        break
    print("Invalid choice. Please select a valid option.")

link = f"https://www.ubisoft.com/en-us/game/assassins-creed/{options[int(choice) - 1].lower()}/photomode/my-photo"
download_dir = os.path.abspath(f"Assassin's Creed {options[int(choice) - 1]} - My Photos")
os.makedirs(download_dir, exist_ok=True)

# Firefox browser setup
options = webdriver.FirefoxOptions()
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", download_dir)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "image/jpeg")
options.set_preference("pdfjs.disabled", True)
options.set_preference("browser.download.manager.showWhenStarting", False)

driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install()),
    options=options
)

# Login
driver.get(link)
input("Please sign in in the opened browser window. Once you're signed in, press Enter here to continue...")
driver.get(link) # reload the page after login

# Load all photos by clicking "Load More" buttons
wait = WebDriverWait(driver, 10)
while True:
    try:
        load_more = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-innertext="Load More"]')))
        load_more.click()
        time.sleep(2)
    except:
        break

# Collect photo URLs from the page
hrefs = []
try:
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "photo-list")))
    container = driver.find_element(By.CLASS_NAME, "photo-list")
    items = container.find_elements(By.CLASS_NAME, "photo-list__photo-item")
    for item in items:
        a = item.find_element(By.TAG_NAME, "a")
        href = a.get_attribute("href")
        if href:
            hrefs.append("https://www.ubisoft.com" + href if not href.startswith("http") else href)
except Exception as e:
    print(f"Could not locate the photo list container: {e}")
    driver.quit()
    exit(1)

if len(hrefs) == 0:
    print("No photos found. Please check if you are logged in and have photos available.")
    driver.quit()
    exit(1)

print(f"Collected {len(hrefs)} photo URLs, downloading...")

# Download images from the collected URLs
for url in hrefs:
    driver.get(url)
    try:
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.photomode-download__link[data-ccm-m='buttonMaster']"))).click()
        print(f"Downloaded from: {url}")
    except Exception as e:
        print(f"Failed to download: {url}")
    time.sleep(1)

print("Done.")
driver.quit()
