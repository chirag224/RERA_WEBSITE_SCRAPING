import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    driver.get("https://hprera.nic.in/PublicDashboard")

    # Wait for the parent div "reg-Projects" to be visible
    parent_div = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.ID, "reg-Projects"))
    )

    # Find the form-row div within the parent div
    form_row_div = parent_div.find_element(By.XPATH, ".//div[contains(@class, 'form-row')]")

    # Find all the child divs "col-lg-6" within the form-row div
    child_divs = form_row_div.find_elements(By.XPATH, ".//div[contains(@class, 'col-lg-6')]")

    project_details = []

    # Iterate through the first six child divs
    for i in range(min(6, len(child_divs))):
        child_div = child_divs[i]

        # Find the RERA number link within the child div
        rera_number = child_div.find_element(By.XPATH, ".//a")

        # Click the RERA number link
        rera_number.click()

        try:
            # Wait for the new content modal to be visible
            new_content_modal = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "modal-content"))
            )

            # Find the desired link within the new content modal
            link_in_modal = WebDriverWait(new_content_modal, 10).until(
                EC.visibility_of_element_located((By.XPATH, ".//nav/a[1]"))
            )

            # Click the link within the new content modal
            link_in_modal.click()

            # Wait for the element with id "project-menu-html" to be visible
            WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.ID, "project-menu-html"))
            )

            # Increase wait time for the table to be present
            table = WebDriverWait(driver, 40).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table'))
            )

            table_body = table.find_element(By.CLASS_NAME, "lh-2")
            
            # Initialize variables to store data
            gstin_number = ""
            pan_number = ""
            name = ""
            permanent_address = ""

            # Iterate through rows and extract data
            rows = table_body.find_elements(By.TAG_NAME, "tr")
            for row in rows:
                tds = row.find_elements(By.TAG_NAME, "td")
                if len(tds) == 2:
                    label = tds[0].text.strip()
                    value_td = tds[1]
                    value = value_td.text.strip()

                    # Extracting specific information based on labels and styles/classes
                    if "GSTIN No." in label:
                        try:
                            gstin_number = value_td.find_element(By.TAG_NAME, "span").text.strip()
                        except NoSuchElementException:
                            pass
                    elif "PAN No." in label:
                        try:
                            pan_number = value_td.find_element(By.TAG_NAME, "span").text.strip()
                        except NoSuchElementException:
                            pass
                    elif "Name" in label:
                        name = value
                    elif "Permanent Address" in label:
                        permanent_address = value_td.find_element(By.TAG_NAME, "span").text.strip()

            project_details.append({
                "GSTIN No": gstin_number,
                "PAN No": pan_number,
                "Name": name,
                "Permanent Address": permanent_address
            })

            # Close the modal by clicking the close button
            close_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='close']"))
            )
            close_button.click()

        except TimeoutException:
            pass
        except NoSuchElementException:
            pass
        except NoSuchWindowException:
            pass

except TimeoutException:
    pass
except NoSuchElementException:
    pass
except NoSuchWindowException:
    pass
finally:
    # Close the WebDriver
    driver.quit()

    # Save project details to CSV
    with open("project_details.csv", "w", newline="") as csvfile:
        fieldnames = ["GSTIN No", "PAN No", "Name", "Permanent Address"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for project in project_details:
            writer.writerow(project)
