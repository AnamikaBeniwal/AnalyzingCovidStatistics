from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from bs4 import BeautifulSoup


def getAllData(dataPath):
    """This function will fecth data from the URL using Selenium Webdriver.
    This function takes in the URL, from where data needs to be fetched, as the argument.
    It returns the table soup.
    """
    # Initialize the Chrome driver
    driver = webdriver.Chrome()

    # Open the WHO COVID-19 dashboard page
    driver.get(dataPath)

    # Wait for up to 20 seconds for elements to be available
    wait = WebDriverWait(driver, 20)

    try:
        # Wait for the cumulative button to be clickable
        cumulativeButton = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="covid19-overview"]/div/div[1]/ul[1]/li[3]/label/input')))
        
        # Scroll the element into view and click it using JavaScript to avoid interception issues
        driver.execute_script("arguments[0].scrollIntoView(true);", cumulativeButton)
        driver.execute_script("arguments[0].click();", cumulativeButton)
        
        # Repeatedly click the 'Show more' button until it is no longer found
        WebDriverWait(driver, 5)
        showMoreButton = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="covid19-overview"]/div/div[2]/div[2]/div[2]/div[2]/div/div[4]/div/div/table/tbody/tr[4]/td/button')))
                
        # Scroll the element into view and click it using JavaScript to avoid interception issues
        driver.execute_script("arguments[0].scrollIntoView(true);", showMoreButton)
        driver.execute_script("arguments[0].click();", showMoreButton)        
    except ElementClickInterceptedException as e:
        print("ElementClickInterceptedException occurred:", e)

    # Get the page source
    page_source = driver.page_source

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, "html5lib")

    # Find the table containing the data
    table = soup.find("table", attrs={'class': 'svelte-1xil9mb', 'data-testid': 'dataDotViz-collapsibleTable'})

    # Close the browser
    driver.quit()
    
    # Return the table or print it if not found
    if table:
        return table
    else:
        print("Table not found")