from appium import webdriver

desired_caps = {
  "platformName": "iOS",
  "platformVersion": "16.2",
  "deviceName": "iPhone 14 Pro",
  "app": "/Users/hwkim03/project/node/mma_data/builder/flutter-ios/builder-0/build/ios/iphonesimulator/Runner.app",
  "automationName": "XCUITest"
}

driver = webdriver.Remote( 'http://127.0.0.1:4723', desired_caps)

driver.quit()