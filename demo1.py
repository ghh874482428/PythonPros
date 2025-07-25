import undetected_chromedriver as uc
from time import sleep
from selenium.webdriver.common.by import By

chrome_driver = uc.Chrome()
chrome_driver.get("https://apixnh.xnhkfpt.com/api/miguauth/orderIndexBy?buyerid=7406fff082394fadaa205ab12fe143a0&mobileuid=77a4a7e6ac354599b23102bc1e6bd4e6&producetype=qwvedio&source=douyin")
sleep(20);
chrome_driver.switch_to.frame("frame");
elem_getcode=chrome_driver.find_element(By.ID,"sms-get-code");
elem_getcode.click();
sleep(5);
elem_sms_input=chrome_driver.find_element(By.ID,"sms-sms-input");
#elem_sms_input.send_keys("111222");
sleep(40);
elem_sms_okPay=chrome_driver.find_element(By.ID,"sms-okPay");
elem_sms_okPay.click();
sleep(1000);