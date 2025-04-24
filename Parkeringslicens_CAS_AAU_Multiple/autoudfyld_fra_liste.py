import csv
import requests
from io import StringIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
 
CSV_URL = "https://dinweburl.dk/parkering.csv"  # <- erstat med din rigtige URL
LOG_FILE = "parkeringslog.txt"
 
def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
 
def fetch_csv_data(url):
    response = requests.get(url)
    response.raise_for_status()
    data = StringIO(response.text)
    reader = csv.DictReader(data)
    return [(row["telefonummer"], row["registrering"]) for row in reader]
 
def run_parking_registration(phone, plate):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
 
    driver = webdriver.Chrome(options=options)
 
    try:
        driver.get("https://online.mobilparkering.dk/12cdf204-d969-469a-9bd5-c1f1fc59ee34")
        wait = WebDriverWait(driver, 15)
 
        reg_input = wait.until(EC.presence_of_element_located((By.ID, "inline-full-name")))
        reg_input.send_keys(plate)
 
        phone_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="tel"]')))
        phone_input.send_keys(phone)
 
        checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.form-checkbox.rounded.p-3')))
        if not checkbox.is_selected():
            checkbox.click()
 
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Fortsæt"]')))
        submit_button.click()
 
        confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Bekræft og opret"]')))
        confirm_button.click()
 
        log(f"✅ SUCCES: Parkering oprettet for {plate} ({phone})")
    except Exception as e:
        log(f"❌ FEJL: {plate} ({phone}) — {e}")
    finally:
        driver.quit()
 
try:
    entries = fetch_csv_data(CSV_URL)
    for phone, plate in entries:
        run_parking_registration(phone, plate)
except Exception as e:
    log(f"❌ Kunne ikke hente CSV: {e}")
 