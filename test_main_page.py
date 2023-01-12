from selenium.webdriver.common.by import By
import time

class MainPage:

    def test_shop_item(self, browser):
        link =  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/";
        browser.get(link);
        time.sleep(5);

        btn_basket_add = browser.find_element(By.CLASS_NAME, "btn-add-to-basket");
        btn_basket_add.click();
        time.sleep(5);

        alert_window = browser.find_element(By.CLASS_NAME, "alertinner ");
        alert_window_text = alert_window.text;

        assert "Coders at Work has been added to your basket." == alert_window_text;

# не забываем оставить пустую строку в конце файла