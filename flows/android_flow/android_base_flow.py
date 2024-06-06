import time


class AndroidBaseFlow:
    def __init__(self, driver):
        self.driver = driver  # Driver obyektini saqlaydi

    def install_application(self, login=True):
        if login:  # Agar login qiymati True bo'lsa
            self.driver.remove_app('trastpay.uz')  # Ilovani olib tashlaydi
            self.driver.install_app(
                "C:\\Users\\User\\Desktop\\ish\\Trastpay_Automation_testing\\apps\\payme_2.47.1")
                # Ilovani kompyuterning ko'rsatilgan joylashuvidan o'rnatadi
            self.driver.activate_app('trastpay.uz')  # Ilovani ishga tushiradi
            time.sleep(5)  # Ilovaning yuklanishi uchun 5 soniya kutadi
            return True  # True qiymatini qaytaradi
        else:  # Agar login qiymati False bo'lsa
            self.driver.install_app(
                "C:\\Users\\User\\Desktop\\ish\\Trastpay_Automation_testing\\apps\\payme_2.47.1")
                # Ilovani kompyuterning ko'rsatilgan joylashuvidan o'rnatadi
            self.driver.activate_app('trastpay.uz')  # Ilovani ishga tushiradi
            time.sleep(5)  # Ilovaning yuklanishi uchun 5 soniya kutadi
            return True  # True qiymatini qaytaradi
