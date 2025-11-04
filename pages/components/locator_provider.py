

class LocatorProvider:
    def __init__(self, page_name):
        self.elements_locators = self._get_page_locators(page_name)

    # метод получения списка локаторов на странице
    # в случает отсутствия имени страницы в списке, выдаст ошибку
    def _get_page_locators(self, page_name):
        LOCATORS = {
            'ЛК ТКП'                                                : self.__LOGIN,
            'Главная страница'                                      : self.__MAIN,
        }
        try:
            return LOCATORS[page_name]
        except ValueError as e:
            raise e(f'Для страницы {page_name} не заведены локаторы в файле классе LocatorProvider')

        KEY_WORDS = {
            'ключевое слово в сценарии': 'ключи в объектах LocatorProvider',
            'поле ввода': 'input'
        }

        __LOGIN = {
            'Группа элемент или элемент': 'локатор или локатор с форматирование',
            'input': '//input[@placeholder="{}"]',
            'button': '//button[contains(text(),"{}")]',
            'link': '//button[contains(@class, "btn-link") and contains(text(), "{}")]',
            'error_message': '//div[@class="alert alert-danger"]//span[contains(text(), "")]',
        }

        __MAIN = {
            'Группа элемент или элемент': 'локатор или локатор с форматирование',
            'navigate_item': '(//div[contains(text(), "{}") and (@class="menu-text")])[1]',
            'title': '//h3[contains(text(), "{}")]',
        }