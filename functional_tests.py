from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://langestrst01.pythonanywhere.com/')

assert 'Django' in browser.title