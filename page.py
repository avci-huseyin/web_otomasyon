import time
from locator import *
from element import BasePageElement
from function import BasePageFunction

class MainPageButton(BasePageElement):
    locator = "//*[@id='navbarNav']/div/a[1]"

class DevicePageButton(BasePageElement):
    locator = "//*[@id='navbarNav']/div/a[2]"

class PlannerPageButton(BasePageElement):
    locator = "//*[@id='navbarNav']/div/a[3]"

class EmergencyPageButton(BasePageElement):
    locator = "//*[@id='navbarNav']/div/a[4]"

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def select_english_language(self):
        BasePageFunction.select_english_language(self)

    def select_turkish_language(self):
        BasePageFunction.select_turkish_language(self)

    def select_portuguese_language(self):
        BasePageFunction.select_portuguese_language(self)

    def select_japanese_language(self):
        BasePageFunction.select_japanese_language(self)

    def is_title_matches(self, pageName, titleName):
        return BasePageFunction.is_title_matches(self, pageName, titleName)

    def is_container_title_matches(self, containerTitle):
        return BasePageFunction.is_container_title_mathces(self, containerTitle)

BasePageFunction(BasePage)

class MainPage(BasePage):

    def is_status_title_matches(self, statusTitle):
        return statusTitle in str(self.driver.find_element_by_xpath("//*[@id='app']/section[1]/div/div/div[2]/div[1]/div/h3").text)

    def is_fmradio_title_matches(self, fmradioTitle):
        return fmradioTitle in str(self.driver.find_element_by_xpath("//*[@id='app']/section[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/h4/strong").text)

    def is_fmradio_title_text_matches(self, fmradioTitlesText):
        return fmradioTitlesText in str(self.driver.find_element_by_xpath("//*[@id='radioBlink']").text)

    def is_announcement_title_matches(self, announcementTitle):
        return announcementTitle in str(self.driver.find_element_by_xpath("//*[@id='app']/section[1]/div/div/div[2]/div[2]/div/div[1]/div[2]/h4/strong").text)

    def is_announcement_title_text_matches(self, announcementTitlesText):
        return announcementTitlesText in str(self.driver.find_element_by_xpath("//*[@id='announcementOnHold']").text)

    def is_plannergroup_title_matches(self, plannergroupTitle):
        return plannergroupTitle in str(self.driver.find_element_by_xpath("//*[@id='app']/section[1]/div/div/div[2]/div[2]/div/div[1]/div[3]/h4/strong").text)

    def is_plannergroup_title_text_matches(self, plannergroupTitlesText):
        return plannergroupTitlesText in str(self.driver.find_element_by_xpath("//*[@id='app']/section[1]/div/div/div[2]/div[2]/div/div[1]/div[3]/h5").text)

    def is_livebutton_title_matches(self, livebuttonTitle):
        return livebuttonTitle in str(self.driver.find_element_by_xpath("//*[@id='app']/section[1]/div/div/div[2]/div[2]/div/div[1]/div[4]/a[2]").text)

    def is_announcementqueue_title_matches(self, announcementqueueTitle):
        return announcementqueueTitle in str(self.driver.find_element_by_xpath("//*[@id='app']/section[1]/div/div/div[2]/div[2]/div/div[2]/div[3]/h4").text)

    def is_announcementqueue_title_announcement_matches(self, announcementqueuetitleAnnouncement):
        return announcementqueuetitleAnnouncement in str(self.driver.find_element_by_xpath("//*[@id='app']/section[1]/div/div/div[2]/div[2]/div/div[2]/div[3]/table/thead/tr/th[1]").text)

    def is_radiotime_title_matches(self, radiotimeTitle):
        return radiotimeTitle in str(self.driver.find_element_by_xpath("//*[@id='app']/section[1]/div/div/div[2]/div[2]/div/div[2]/div[3]/table/thead/tr/th[2]").text)

    def is_totalduration_title_matches(self, totaldurationTitle):
        return totaldurationTitle in str(self.driver.find_element_by_xpath("//*[@id='app']/section[1]/div/div/div[2]/div[2]/div/div[2]/div[3]/table/thead/tr/th[3]").text)

    def is_rdsstatus_title_matches(self, rdsstatusTitle):
        return rdsstatusTitle in str(self.driver.find_element_by_xpath("//*[@id='app']/section[1]/div/div/div[3]/div/h3").text)

    def is_ta_title_matches(self, taTitle):
        return taTitle in str(self.driver.find_element_by_xpath("//*[@id='app']/section[1]/div/div/div[3]/div/div/div[4]/div/div/h4[2]").text)

    def click_live_button(self):
        liveButton = self.driver.find_element(*MainPageLocators.LIVE_BUTTON)
        liveButton.click()

class DevicePage(BasePage):

    click_device_button = DevicePageButton()

    def frequency_proccess(self):
        frequency_groups = self.driver.find_elements_by_xpath("//*[@id='app']/section[1]/div[2]/div[1]/div/div")
        frequency_channels = self.driver.find_elements_by_xpath("//*[@id='new_frequency']/option")
        acceptButton = self.driver.find_element(*DevicePageLocators.SELECT_CHANNEL_ALLOW_BUTTON)

        for i in range(1, len(frequency_groups)):
            frequency_group = self.driver.find_element_by_xpath(f"//*[@id='app']/section[1]/div[2]/div[1]/div[{i}]/button")
            for j in range(1, len(frequency_group)):
                frequencyButton = self.driver.find_element_by_xpath(f"//*[@id='app']/section[1]/div[2]/div[1]/div[{i}]/button[{j}]")
                frequencyButton.click()
                for z in range(1, len(frequency_channels)):
                    frequencyChannel = self.driver.find_element_by_xpath(f"//*[@id='new_frequency']/option[{z}]")
                    frequencyChannel.click()
                    acceptButton.click()

class PlannerPage(BasePage):

    click_planner_button = PlannerPageButton()

    def planner_announcement_files_proccess(self):
        announcementFilesButton = self.driver.find_element(*PlannerPageLocators.ANNOUNCEMENT_FILES)
        announcementFilesButton.click()

        announcement_files_lenght = self.driver.find_elements_by_xpath("//*[@id='filesModal']/div/div/div[2]/section/div/div/div/table/tbody/tr")

        for i in range(1, len(announcement_files_lenght)):
            selectAnnouncementFiles = (f"document.querySelector('#filesModal > div > div > div.modal-body > section > div > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(3) > audio')")
            self.driver.execute_script(f"{selectAnnouncementFiles}.play()")

            accordionPlayTime = int(self.driver.find_element_by_xpath(f"//*[@id='filesModal']/div/div/div[2]/section/div/div/div/table/tbody/tr[{i}]/td[3]").text)
            time.sleep(accordionPlayTime)

        announcementFilesExitButton = self.driver.find_element(*PlannerPageLocators.ANNOUNCEMENT_FILES_EXIT_BUTTON)
        announcementFilesExitButton.click()

    def planner_accordion_proccess(self):

        scroll_ilk = self.driver.execute_script("return document.documentElement.scrollHeight")

        planner_accordion_lenght = len(self.driver.find_elements_by_xpath("//*[@id='plannerAccordion']/div"))

        bayrak = 0

        for i in range(planner_accordion_lenght):

            if bayrak == 0:
                self.driver.execute_script(f"window.scrollTo((document.querySelector('#plannerAccordion > div:nth-child(1)')).clientHeight * {i}, (document.querySelector('#plannerAccordion > div:nth-child(1)')).clientHeight * {i + 1});")

            scroll_son = self.driver.execute_script("return document.documentElement.scrollHeight")

            if scroll_son == scroll_ilk:
                bayrak = 1

            scroll_ilk = scroll_son

    def planner_create_new_group_proccess(self):
        pass

class EmergencyPage(BasePage):

    click_emergency_button = EmergencyPageButton()

    def emergency_announcement_files_proccess(self):
        announcementFilesButton = self.driver.find_element(*PlannerPageLocators.ANNOUNCEMENT_FILES)
        announcementFilesButton.click()

        announcement_files_lenght = self.driver.find_elements_by_xpath(
            "//*[@id='filesModal']/div/div/div[2]/section/div/div/div/table/tbody/tr")

        for i in range(1, len(announcement_files_lenght)):
            selectAnnouncementFiles = (
                f"document.querySelector('#filesModal > div > div > div.modal-body > section > div > div > div > table > tbody > tr:nth-child({i}) > td:nth-child(3) > audio')")
            self.driver.execute_script(f"{selectAnnouncementFiles}.play()")

            accordionPlayTime = int(self.driver.find_element_by_xpath(
                f"//*[@id='filesModal']/div/div/div[2]/section/div/div/div/table/tbody/tr[{i}]/td[3]").text)
            time.sleep(accordionPlayTime)

        announcementFilesExitButton = self.driver.find_element(*PlannerPageLocators.ANNOUNCEMENT_FILES_EXIT_BUTTON)
        announcementFilesExitButton.click()

    def emergency_accordion_proccess(self):
        scroll_ilk = self.driver.execute_script("return document.documentElement.scrollHeight")

        emergency_accordion_lenght = len(self.driver.find_elements_by_xpath("//*[@id='emergencyAccordion']/div"))

        bayrak = 0

        for i in range(emergency_accordion_lenght):

            if bayrak == 0:
                self.driver.execute_script(
                    f"window.scrollTo((document.querySelector('#emergencyAccordion > div:nth-child(1)')).clientHeight * {i}, (document.querySelector('#emergencyAccordion > div:nth-child(1)')).clientHeight * {i + 1});")

            scroll_son = self.driver.execute_script("return document.documentElement.scrollHeight")

            if scroll_son == scroll_ilk:
                bayrak = 1

            scroll_ilk = scroll_son

    def emergency_create_new_rds_package_proccess(self):
        pass

class LivePage(BasePage):
    pass

