from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest
import HtmlTestRunner
import page

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        opt = Options()
        opt.add_argument("--disable-infobars")
        opt.add_argument("start-maximized")
        opt.add_argument("--disable-extensions")
        opt.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 0,
            "profile.default_content_setting_values.geolocation": 0,
            "profile.default_content_setting_values.notifications": 0
        })
        self.driver = webdriver.Chrome(options=opt)
        self.driver.get("http://localhost:5000/")

    def test_main_page_english_texts(self):
        mainPage = page.MainPage(self.driver)
        mainPage.select_english_language()

        # Anasayfa title'ı doğrulama
        assert mainPage.is_title_matches("Main Page", "ABE Technology Tunnel FM Brake-In Control")
        # container title'ı doğrulama
        assert mainPage.is_container_title_matches("TUNNEL FM BRAKE-IN CONTROL")
        # durum title'ini doğrulama
        assert mainPage.is_status_title_matches("FM BRAKE-IN STATUS")
        # fm radio title'ını doğrulama
        assert mainPage.is_fmradio_title_matches("FM RADIO")
        # fm radio title text'ini doğrulama
        assert mainPage.is_fmradio_title_text_matches("ACTIVE")
        # duyuru title'ını doğrulama
        assert mainPage.is_announcement_title_matches("ANNOUNCEMENT")
        # duyuru title text'ini doğrulama
        assert mainPage.is_announcement_title_text_matches("ON HOLD")
        # planlayıcı grup title'ini doğrulama
        assert mainPage.is_plannergroup_title_matches("PLANNER GROUP")
        # planlayıcı grup title text'ini doğrulama
        assert mainPage.is_plannergroup_title_text_matches("/ -")
        # live button text'ini doğrulama
        assert mainPage.is_livebutton_title_matches("Live")
        # planlayıcı sıralaması title'ini doğrulama
        assert mainPage.is_announcementqueue_title_matches("ANNOUNCEMENTS QUEUE")
        # planlayıcı sıralamasının duyuru title'ını doğrulama
        assert mainPage.is_announcementqueue_title_announcement_matches("Announcement")
        # planlayıcı sıralamasının radyo süresi title'ını doğrulama
        assert mainPage.is_radiotime_title_matches("Radio Time")
        # planlayıcı sıralamasının toplam süre title'ını doğrulama
        assert mainPage.is_totalduration_title_matches("Total Duration")
        # rds durum title'ını doğrulama
        assert mainPage.is_rdsstatus_title_matches("RDS STATUS")
        # TA title'ını doğrulama
        assert mainPage.is_ta_title_matches("Passive")

    def test_main_page_turkish_texts(self):
        mainPage = page.MainPage(self.driver)
        mainPage.select_turkish_language()

        # Anasayfa title'ı doğrulama
        assert mainPage.is_title_matches("Ana Sayfa", "ABE TEKNOLOJİ FM ARAYÜZÜ")
        # container title'ı doğrulama
        assert mainPage.is_container_title_matches("TÜNEL FM BRAKE-IN KONTROL")
        # durum title'ini doğrulama
        assert mainPage.is_status_title_matches("FM BRAKE-IN DURUMU")
        # fm radio title'ını doğrulama
        assert mainPage.is_fmradio_title_matches("FM RADYO")
        # fm radio title text'ini doğrulama
        assert mainPage.is_fmradio_title_text_matches("AKTİF")
        # duyuru title'ını doğrulama
        assert mainPage.is_announcement_title_matches("ANONS")
        # duyuru title text'ini doğrulama
        assert mainPage.is_announcement_title_text_matches("BEKLEMEDE")
        # planlayıcı grup title'ini doğrulama
        assert mainPage.is_plannergroup_title_matches("PLANLAYICI GRUP")
        # planlayıcı grup title text'ini doğrulama
        assert mainPage.is_plannergroup_title_text_matches("/ -")
        # live button text'ini doğrulama
        assert mainPage.is_livebutton_title_matches("Canlı")
        # planlayıcı sıralaması title'ini doğrulama
        assert mainPage.is_announcementqueue_title_matches("")
        # planlayıcı sıralamasının duyuru title'ını doğrulama
        assert mainPage.is_announcementqueue_title_announcement_matches("Anons")
        # planlayıcı sıralamasının radyo süresi title'ını doğrulama
        assert mainPage.is_radiotime_title_matches("Radyo Süresi")
        # planlayıcı sıralamasının toplam süre title'ını doğrulama
        assert mainPage.is_totalduration_title_matches("Toplam Süre")
        # rds durum title'ını doğrulama
        assert mainPage.is_rdsstatus_title_matches("RDS DURUMU")
        # TA title'ını doğrulama
        assert mainPage.is_ta_title_matches("PASİF")

    def test_main_page_portuguese_texts(self):
        mainPage = page.MainPage(self.driver)
        mainPage.select_portuguese_language()

        # Anasayfa title'ı doğrulama
        #assert mainPage.is_title_matches("", "")
        # container title'ı doğrulama
        assert mainPage.is_container_title_matches("")
        # durum title'ini doğrulama
        assert mainPage.is_status_title_matches("")
        # fm radio title'ını doğrulama
        assert mainPage.is_fmradio_title_matches("")
        # fm radio title text'ini doğrulama
        assert mainPage.is_fmradio_title_text_matches("")
        # duyuru title'ını doğrulama
        assert mainPage.is_announcement_title_matches("")
        # duyuru title text'ini doğrulama
        assert mainPage.is_announcement_title_text_matches("")
        # planlayıcı grup title'ini doğrulama
        assert mainPage.is_plannergroup_title_matches("")
        # planlayıcı grup title text'ini doğrulama
        assert mainPage.is_plannergroup_title_text_matches("/ -")
        # live button text'ini doğrulama
        assert mainPage.is_livebutton_title_matches("")
        # planlayıcı sıralaması title'ini doğrulama
        assert mainPage.is_announcementqueue_title_matches("")
        # planlayıcı sıralamasının duyuru title'ını doğrulama
        assert mainPage.is_announcementqueue_title_announcement_matches("")
        # planlayıcı sıralamasının radyo süresi title'ını doğrulama
        assert mainPage.is_radiotime_title_matches("")
        # planlayıcı sıralamasının toplam süre title'ını doğrulama
        assert mainPage.is_totalduration_title_matches("")
        # rds durum title'ını doğrulama
        assert mainPage.is_rdsstatus_title_matches("")
        # TA title'ını doğrulama
        assert mainPage.is_ta_title_matches("")

    def test_main_page_japanese_texts(self):
        mainPage = page.MainPage(self.driver)
        mainPage.select_japanese_language()

        # Anasayfa title'ı doğrulama
        assert mainPage.is_title_matches("メインページ", "ABE テクノロジーFMインターフェース")
        # container title'ı doğrulama
        assert mainPage.is_container_title_matches("")
        # durum title'ini doğrulama
        assert mainPage.is_status_title_matches("FMブレーキインステータス")
        # fm radio title'ını doğrulama
        assert mainPage.is_fmradio_title_matches("FMラジオ")
        # fm radio title text'ini doğrulama
        assert mainPage.is_fmradio_title_text_matches("アクティブ")
        # duyuru title'ını doğrulama
        assert mainPage.is_announcement_title_matches("発表")
        # duyuru title text'ini doğrulama
        assert mainPage.is_announcement_title_text_matches("保留")
        # planlayıcı grup title'ini doğrulama
        assert mainPage.is_plannergroup_title_matches("")
        # planlayıcı grup title text'ini doğrulama
        assert mainPage.is_plannergroup_title_text_matches("/ -")
        # live button text'ini doğrulama
        assert mainPage.is_livebutton_title_matches("ライブ")
        # planlayıcı sıralaması title'ini doğrulama
        assert mainPage.is_announcementqueue_title_matches("")
        # planlayıcı sıralamasının duyuru title'ını doğrulama
        assert mainPage.is_announcementqueue_title_announcement_matches("発表")
        # planlayıcı sıralamasının radyo süresi title'ını doğrulama
        assert mainPage.is_radiotime_title_matches("ラジオタイム")
        # planlayıcı sıralamasının toplam süre title'ını doğrulama
        assert mainPage.is_totalduration_title_matches("合計期間")
        # rds durum title'ını doğrulama
        assert mainPage.is_rdsstatus_title_matches("RDSステータス")
        # TA title'ını doğrulama
        assert mainPage.is_ta_title_matches("パッシブ")

    def test_main_page_to_live_page(self):
        mainPage = page.MainPage(self.driver)
        mainPage.click_live_button()

    def test_device_page_frequency_process(self):
        devicePage = page.DevicePage(self.driver)
        devicePage.click_device_button.click()

        devicePage.frequency_proccess()

    def test_planner_page_announcement_files_process(self):
        plannerPage = page.PlannerPage(self.driver)
        plannerPage.click_planner_button.click()

        plannerPage.planner_announcement_files_proccess()

    def test_planner_accordion_process(self):
        plannerPage = page.PlannerPage(self.driver)
        plannerPage.click_planner_button.click()

        plannerPage.planner_accordion_proccess()

    def test_planner_new_group_process(self):
        pass

    def test_planner_page_edit_process(self):
        pass

    def test_planner_page_delete_process(self):
        pass

    def test_emergency_page_announcement_files_process(self):
        emergencyPage = page.EmergencyPage(self.driver)
        emergencyPage.click_emergency_button.click()

        emergencyPage.emergency_announcement_files_proccess()

    def test_emergency_accordion_process(self):
        emergencyPage = page.EmergencyPage(self.driver)
        emergencyPage.click_emergency_button.click()

        emergencyPage.emergency_accordion_proccess()

    def test_emergency_new_group_process(self):
        pass

    def test_emergency_page_select_process(self):
        pass

    def test_emergency_page_edit_process(self):
        pass

    def test_emergency_page_delete_process(self):
        pass

    def test_livePage(self):
        pass

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/01/GLSM/ABE/Selenium/fm-tx-interface/fm-tx-interface_testcase/reports'))