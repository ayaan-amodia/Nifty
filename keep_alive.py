from playwright.sync_api import sync_playwright
import time

URL = "https://niftybs.streamlit.app/"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(URL, timeout=120000)
    time.sleep(15)

    # If the app is asleep, click the wake-up button
    try:
        button = page.get_by_text("Yes, get this app back up!")
        if button.count() > 0:
            button.first.click()
            print("App was asleep - clicked wake-up button")
            time.sleep(60)
    except Exception as e:
        print("Wake check error:", e)

    # Stay on the page so Streamlit registers a real session
    time.sleep(30)
    print("Visit complete")
    browser.close()
