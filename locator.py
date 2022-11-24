from selenium.webdriver.common.by import By
import random

class MainPageLocators(object):

    LIVE_BUTTON = (By.XPATH, ("//*[@id='app']/section[1]/div/div/div[2]/div[2]/div/div[1]/div[4]/a[2]"))

class DevicePageLocators(object):

    SELECT_CHANNEL_ALLOW_BUTTON = (By.XPATH, ("//*[@id='changeFrequencyModal']/div/div/div[3]/button[2]"))

    SELECT_CHANNEL_DENY_BUTTON = (By.XPATH, ("//*[@id='changeFrequencyModal']/div/div/div[3]/button[1]"))

class PlannerPageLocators(object):

    ANNOUNCEMENT_FILES = (By.XPATH, ("//*[@id='app']/section/div[1]/div/div/div/button[1]"))
    ANNOUNCEMENT_FILES_EXIT_BUTTON = (By.XPATH, ("//*[@id='filesModal']/div/div/div[1]/button"))

    CREATE_NEW_GROUP_BUTTON = (By.XPATH, ("//*[@id='app']/section/div[1]/div/div/div/button[2]"))
    CREATE_NEW_GROUP_EXIT = (By.XPATH, ("//*[@id='newGroup']/div/div/div[1]/button"))
    CREATE_NEW_GROUP_NAME = (By.XPATH, ("//*[@id='newGroupName']"))
    CREATE_NEW_GROUP_START_TIME = (By.XPATH, ("//*[@id='newGroupStartTime']"))
    CREATE_NEW_GROUP_END_TIME = (By.XPATH, ("//*[@id='newGroupEndTime']"))
    CREATE_NEW_GROUP_RDS_ID = (By.XPATH, ("//*[@id='rdsID']"))

    create_new_rds_channels = (By.XPATH, ("//*[@id='rdsID']/option"))
    create_new_rds_channels_random = random.randint(1, len(create_new_rds_channels))
    SELECT_CREATE_NEW_GROUP_RDS_ID = (By.XPATH, (f"//*[@id='rdsID']/option[{create_new_rds_channels_random}]"))

    CREATE_NEW_GROUP_SAVE_BUTTON = (By.XPATH, ("//*[@id='newGroup']/div/div/div[3]/button[2]"))
    CREATE_NEW_GROUP_CANCEL_BUTTON = (By.XPATH, ("//*[@id='newGroup']/div/div/div[3]/button[1]"))

    EDIT_GROUP_EXIT = (By.XPATH, (f"//*[@id='editGroupModal']/div/div/div[1]/button"))
    EDIT_GROUP_NAME = (By.XPATH, ("//*[@id='editGroupName']"))
    EDIT_GROUP_START_TIME = (By.XPATH, ("//*[@id='editGroupStartTime']"))
    EDIT_GROUP_END_TIME = (By.XPATH, ("//*[@id='editGroupEndTime']"))
    EDIT_RDS_ID = (By.XPATH, ("//*[@id='editrdsID']"))

class EmergencyPageLocators(object):

    ANNOUNCEMENT_FILES = (By.XPATH, ("//*[@id='app']/section/div[1]/div/div/div/button[1]"))
    ANNOUNCEMENT_FILES_EXIT_BUTTON = (By.XPATH, ("//*[@id='filesModal']/div/div/div[1]/button"))

class LivePageLocators(object):
    pass
