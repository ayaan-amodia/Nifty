import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Fetch URL from GitHub Secrets or environment variable
URL = os.environ.get("STREAMLIT_APP_URL")

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    print(f"Visiting {URL}...")
    driver.get(URL)
    time.sleep(5)  # Wait for page elements to load
    
    # Search for the "Wake up app" button text or selector
    # Streamlit buttons typically use standard button classes or text matches
    buttons = driver.find_elements(By.TAG_NAME, "button")
    wake_button = None
    
    for btn in buttons:
        if "Wake up" in btn.text or "Wake" in btn.text:
            wake_button = btn
            break
            
    if wake_button:
        wake_button.click()
        print("Success: Clicked the 'Wake up' button!")
        time.sleep(10)  # Wait for boot up sequence
    else:
        print("App is already awake or button wasn't found.")
        
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
