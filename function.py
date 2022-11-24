class BasePageFunction(object):
    def __init__(self, driver):
        self.driver = driver

    def is_title_matches(self, pageName, titleName):
        return f"{pageName} / {titleName}" in self.driver.title

    def is_container_title_mathces(self, containerTitle):
        return containerTitle in str(self.driver.find_element_by_xpath("//*[@id='app']/nav/div[1]/span").text)

    def select_english_language(self):
        languageButton = self.driver.find_element_by_xpath("//*[@id='navbarNav']/div/div/button")
        languageButton.click()

        englishLanguageButton = self.driver.find_element_by_xpath("//*[@id='navbarNav']/div/div/div/a[1]")
        englishLanguageButton.click()

    def select_turkish_language(self):
        languageButton = self.driver.find_element_by_xpath("//*[@id='navbarNav']/div/div/button")
        languageButton.click()

        turkishLanguageButton = self.driver.find_element_by_xpath("//*[@id='navbarNav']/div/div/div/a[2]")
        turkishLanguageButton.click()

    def select_portuguese_language(self):
        languageButton = self.driver.find_element_by_xpath("//*[@id='navbarNav']/div/div/button")
        languageButton.click()

        portugueseLanguageButton = self.driver.find_element_by_xpath("//*[@id='navbarNav']/div/div/div/a[3]")
        portugueseLanguageButton.click()

    def select_japanese_language(self):
        languageButton = self.driver.find_element_by_xpath("//*[@id='navbarNav']/div/div/button")
        languageButton.click()

        japaneseLanguageButton = self.driver.find_element_by_xpath("//*[@id='navbarNav']/div/div/div/a[4]")
        japaneseLanguageButton.click()
