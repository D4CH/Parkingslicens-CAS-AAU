from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Konfigurer headless Chrome med ekstra tilføjelser
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://online.mobilparkering.dk/12cdf204-d969-469a-9bd5-c1f1fc59ee34")

    wait = WebDriverWait(driver, 15)

    # Vent på inputfelter og udfyld dem
    reg_input = wait.until(EC.presence_of_element_located((By.ID, "inline-full-name")))
    reg_input.send_keys("") # <-- Her skal du skrive dit registreringsnummer

    phone_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="tel"]')))
    phone_input.send_keys("") # <-- Her skal du skrive dit telefonnummer

    # Checkbox
    checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.form-checkbox.rounded.p-3')))
    if not checkbox.is_selected():
        checkbox.click()

    # Fortsæt
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Fortsæt"]')))
    submit_button.click()

    # Bekræft og opret
    confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Bekræft og opret"]')))
    confirm_button.click()

    print("Parkering oprettet!")

except Exception as e:
    print("Noget gik galt:", e)

finally:
    driver.quit()
