
import allure
from playwright.sync_api import sync_playwright, expect

browser=sync_playwright().start().chromium.launch(headless=True)
page = browser.new_page()

class click_check:
    @staticmethod
    def main_page():
        with allure.step("Open main page"):
            page.goto("https://effective-mobile.ru/")
            expect(page).to_have_title('Effective Mobile | Разработка мобильных приложений')

    @allure.step("Checking for clickable elements on the top bar")
    def top_bar(self):
        with allure.step("Click О нас"):
            page.locator("//a[@class='tn-atom' and normalize-space(text())='[ О нас ]']").click()
        with allure.step("Click Услуги"):
            page.locator("//a[@class='tn-atom' and normalize-space(text())='[ Услуги ]']").click()
        with allure.step("Click Проекты"):
            page.locator("//a[@class='tn-atom' and normalize-space(text())='[ Проекты ]']").click()
        with allure.step("Click Отзывы"):
            page.locator("//a[@class='tn-atom' and normalize-space(text())='[ Отзывы ]']").click()
        with allure.step("Click Контакты"):
            page.locator("//a[@class='tn-atom' and normalize-space(text())='[ Контакты ]']").click()
        with allure.step("Выбрать специалиста"):
            page.locator("//a[@class='tn-atom' and normalize-space(text())='Выбрать специалиста']").click()

    @allure.step("Checking clickable elements in section О нас")
    def about_us(srlf):
        with allure.step("Click Оставить заявку на сотрудничество"):
            page.locator("#sbs-572374517-1680509731311").get_by_role("link").click()

    @allure.step("Checking clickable objects in section Проекты")
    def projects(self):
        with allure.step("Click button Подробнее"):
            page.get_by_role("button", name="Подробнее").click()
        with allure.step("Click close dialog box"):
            page.get_by_role("button", name="Закрыть диалоговое окно").click()
        with allure.step("Click next slide"):
            page.locator("#rec572838727").get_by_role("button", name="Следующий слайд").click()
            page.wait_for_load_state("networkidle")
        with allure.step("Click next slide"):
            page.locator("#rec572838727").get_by_role("button", name="Следующий слайд").click()

    @allure.step("Click Оставить заявку на консультацию")
    def consultation(self):
        with allure.step("Click Оставить заявку на консультацию"):
            page.locator("//a[@class='tn-atom' and @href='#popup:myform' and @role='button']").click()
        with allure.step("Click close dialog box"):
            page.get_by_role("button", name="Закрыть диалоговое окно").click()

    @allure.step("Checking clickable elements in section Отзывы клиентов")
    def customer_reviews(self):
        with allure.step("Click next slide"):
            page.get_by_label("Слайдер").get_by_role("button", name="Следующий слайд").click()
            page.wait_for_load_state("networkidle")
        with allure.step("Click next slide"):
            page.get_by_label("Слайдер").get_by_role("button", name="Следующий слайд").click()

    @allure.step("Checking clickable elements in section Контакты")
    def contacts(self):
        with allure.step("Click Поддержка"):
            page.locator("//a[@class='tn-atom js-click-zero-stat' and @href='https://t.me/assistant_em']").click()
        with allure.step("Click Telegram"):
            page.locator("//a[@class='tn-atom js-click-zero-stat' and @href='https://t.me/krasnikova_d']").click()
        with allure.step("Click e-mail"):
            page.locator("//a[@class='tn-atom' and @href='mailto:dariia.krasnikova@effectivemobile.ru']").click()
        with allure.step("Click submit Отправить"):
            page.get_by_role("button", name="Отправить").click()
        with allure.step("Click политику конфиденциальности"):
            page.locator("//a[@href='https://effective-mobile.ru/privacy' and @rel='noreferrer noopener']").click()
        with allure.step("Click Политика конфиденциальности"):
            page.locator("//a[@href='https://effective-mobile.ru/privacy' and @rel='noopener']").click()

    