

import time
import traceback


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.dto.property_dto import PropertyDTO
from src.util import checkpoint, logger, proxy_manager
from src.config import TIMEOUT
from src.driver import driver as driver_init

SITE_NAME = "hepsiemlak"
BASE_URL = "https://www.hepsiemlak.com/satilik"  # URL for the 'for sale' section


def click_search_and_filters_scrap_category(driver):

    try:
        """
           the first stage, which is to list houses for sale also this is done to see if the ‘Search’ button is pressed for confirmation purposes
        """
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/aside/div[1]/section/div/section[30]/a[1]'))).click()

        search_button_results_first_stage = driver
        logger.scapper_service_logger.info("Clicked the 'Ara' button.")

        search_button_results_first_stage_page_holder = search_button_results_first_stage.find_element(By.XPATH, "//div[contains(@class, 'list')]")

        while True:
            try:
                property_li_tag_list= search_button_results_first_stage_page_holder.find_element(By.XPATH, "//ul[contains(@class, 'list-items-container')]").find_elements(By.TAG_NAME,"li")

                for property_li_tag_iterator in property_li_tag_list:
                    property_li_tag_iterator.find_element(By.XPATH, "//div[contains(@class, 'links')]").find_element(By.TAG_NAME,"a").click()
                    
                    fill_property_dto(driver)

                WebDriverWait(search_button_results_first_stage_page_holder, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.he-pagination__navigate-text.he-pagination__navigate-text--next"))).click()
            except Exception as e:
                print("Next button couldn't find this is End of paging.")
                break

        """
            second
        """

    except Exception as e:
        logger.scapper_service_logger.error(f"Error setting search and filters: {e}")
        traceback.print_exc()


def fill_property_dto(driver_property):
    try:
        if(driver_property is not None):
            property_dto_final=PropertyDTO()

            driver_property.back()
        else:
            logger.scapper_service_logger.warning("Invalıd property data")
    except Exception as e:
        logger.scapper_service_logger.warning(e)
        return None


def scrape_site():
    """
    Main workflow for scraping Hepsiemlak:
      1. Opens the 'satılık' section.
      2. Clicks the search button and sets filters.
      3. Iterates through listing pages.
      4. Extracts property links from each page.
      5. (Placeholder) Detailed parsing and DTO creation for each property.
      6. Updates checkpoint with the last scraped page.
    """
    driver = driver_init.gen_driver()
    driver.get(BASE_URL)
    time.sleep(TIMEOUT)

    #TODO
    # Load checkpoint to determine starting page
    """
    cp = checkpoint.load_checkpoint(SITE_NAME)
    current_page = cp.get("last_page", 0) + 1
    logger.scapper_service_logger.info(f"Starting scraping from page {current_page}.")
    """

    # Set filters (adjust selectors in the function as needed)
    click_search_and_filters_scrap_category(driver)



if __name__ == "__main__":
    scrape_site()
