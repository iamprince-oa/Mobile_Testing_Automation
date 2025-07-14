from appium import webdriver
from appium.options.android import UiAutomator2Options

# Set up desired capabilities and pass the Android app-activity and app-package to Appium
options = UiAutomator2Options()
options.platformName = "Android"
options.deviceName = "1B271FDF6007B8"
options.automationName = "UiAutomator2"
options.appPackage = "com.mtngh.mymtn"
#options.appActivity = "com.mtngh.mymtn.MainActivity"
options.autoGrantPermissions = True
options.app = "C:\Users\owusu\Desktop\mtnapp.apk"
#options.noReset = True
#.ensureWebviewsHavePages = True

# Initialize the driver
app = webdriver.Remote("http://localhost:4723", options=options)

# Implicit wait for 30 seconds
app.implicitly_wait(30)

# Find the first action button and click on it
first_action = app.find_element("id", "com.android.permissioncontroller:id/permission_allow_button")
first_action.click()

# Find the second action button and click on it
second_action = app.find_element("xpath", '//android.view.ViewGroup[@content-desc="get_started_btn"]/android.view.ViewGroup')
second_action.click()

inputing_number = app.find_element("xpath", '//android.widget.EditText[@content-desc="login_input_msisdn"]')
inputing_number.send_keys("0593130530")

checkbox = app.find_element("class name", "android.widget.CheckBox")
checkbox.click()

verify_number = app.find_element("xpath", '//android.view.ViewGroup[@content-desc="login_btn_verify_number"]/android.view.ViewGroup')
verify_number.click()

#End the session
app.quit()

