from pages.main_page import *

click = click_check()

# В зависимости от задачи разбивка по количеству тестов и шагов в них может быть разными.
# Для регресса я бы использовал меньше тестов, больше шагов в них.
# Для функционального тестирования по блокам, больше тестов, меньше шагов в них.

def test_top_column():
    click.main_page()
    click.top_bar()

def test_about_us():
    click.main_page()
    click.about_us()

def test_projects():
    click.main_page()
    click.projects()

def test_consultation():
    click.main_page()
    click.consultation()

def test_custumer_reviews():
    click.main_page()
    click.customer_reviews()

def test_contacts():
    click.main_page()
    click.contacts()
