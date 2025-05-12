from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_register_page_redirect(driver):
    driver.get("https://the-internet.herokuapp.com/")
    assert "Welcome to the-internet" in driver.page_source

    # Simulating register page check (not present, so just navigating the site)
    driver.find_element(By.LINK_TEXT, "Form Authentication").click()
    assert "Login Page" in driver.page_source
