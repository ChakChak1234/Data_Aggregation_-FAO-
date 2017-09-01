import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

#directories
link = 'http://www.gaez.iiasa.ac.at/w/ctrl?_flow=Vwr&_view=Welcome&idAS=0&idFS=0&fieldmain=main_&idPS=0'

## Access Chrome Driver to use selenium
# Define Download Directory
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'C:/Users/chakw/OneDrive/Documents/Github/Data_Aggregation_(FAO)/Download'}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(executable_path='C:/Users/Dpad.Intern3/Desktop/Projects/Data_Aggregation_(FAO)/Chrome-Driver/chromedriver.exe',
                          chrome_options=chrome_options)
driver.get(link)

# Please provide username and password
username = input('\n\nPlease provide username')
driver.find_element_by_name('_username').send_keys(username)

password = input('\n\nPlease provide password')
driver.find_element_by_name('_password').send_keys(password)

driver.find_element_by_id('buttonSubmit__login').click()

# Click on Suitability and Potential Yield link
driver.find_element_by_name('_targetfieldmain=main_py&_passChanged=true&_eventtype').click()

# Click on Agro-ecological suitability and productivity link
driver.find_element_by_name('&fieldmain=main_py&idPS=0&idAS=0&idFS=0&_targetfieldmain=main_py_six&_passChanged=true&_eventtype').click()

# Click on Total production capacity (t/ha) link
driver.find_element_by_xpath('//*[@id="buttonSubmit__type_fieldmain=main_py_six_qdns&idPS=0&idAS=0&idFS=0"]').click()

# Click on crop link
driver.find_element_by_xpath('//*[@id="buttonSubmit__dim_dimType=crp2&fieldmain=main_py_six_qdns&idPS=1e1d6e7d7ec3368cf13a68fc523d1ed4870e8b45&idAS=0&idFS=0"]').click()
# Select crop
crop = input('\n\nSelect a crop: Wheat, Wetland rice, Dryland rice, Maize, Barley, Sorghum, Rye, Pearl millet, '
             'Foxtail millet, Oat, Buckwheat, White potato, Sweet potato, Cassava, \n Yam and Cocoyam, Sugarcane, Sugarbeet,'
             ' Phaseolus bean, Chickpea, Cowpea, Dry pea, Gram, Pigeonpea, Soybean, Sunflower, Rapeseed, Groundnut, Oilpalm, '
             'Olive, Jatropha, \n Cabbage, Carrot, Onion, Tomato, Banana, Citrus, Coconut, Cocoa, Cotton, Flax, Coffee, Tea, '
             'Tobacco, Alfalfa, Pasture, Miscanthus, Switchgrass, Reed canary grass')
driver.find_element_by_css_selector('input[value="{}"]'.format(crop)).click()

# Click on Water Supply Link
driver.find_element_by_name('dimType=ws2&fieldmain=main_py_six_qdns&idPS=df3e8d7240adfa83a14d5403e1d7591397192999&idAS=0&idFS=0&_passChanged=true&_eventdim').click()
# Select Water Supply
water_supply = input('\n\nSelect a water supply: Rain-fed, Irrigation, Gravity irrigation, Sprinkler irrigation, Drip irrigation')
driver.find_element_by_css_selector('input[value="{}"]'.format(water_supply)).click()

# Click on Input Level Link
driver.find_element_by_xpath('//*[@id="buttonSubmit__dim_dimType=il&fieldmain=main_py_six_qdns&idPS=0162375c181ac4615a35319789f81f56dbc10d60&idAS=0&idFS=0"]').click()
# Select Input Level
input_level = input('\n\nSelect an input level: High, Intermediate, Low')
driver.find_element_by_css_selector('input[value="{}"]'.format(input_level)).click()

# Click on Time Period and Select Baseline
driver.find_element_by_xpath('//*[@id="buttonSubmit__time_fieldmain=main_py_six_qdns&idPS=4687fb524c22ff463ba2b0d053147834c8f91251&idAS=0&idFS=0"]').click()
driver.find_element_by_xpath('//*[@id="buttonSubmit__time_fieldtime=6190&fieldmain=main_py_six_qdns&idPS=4687fb524c22ff463ba2b0d053147834c8f91251&idAS=0&idFS=0"]').click()

# Click on Geographic Areas Link
driver.find_element_by_xpath('//*[@id="buttonSubmit__area_fieldmain=main_py_six_qdns&idPS=a47a9bc7221c13d4db466f293980338012d79774&idAS=0&idFS=0"]').click()
# Unselect all countries
driver.find_element_by_xpath('//*[@id="fieldareaList__pln-1"]').click()
# Select a Geographic Area
geographic_area = input('\n\n\Select a geographic area: Caribbean, Central America, South America, Austrailia and New Zealand,'
                        'Pacific Islands, Eastern Africa, Central Africa, Southern Africa, \n Sudano-Sahelian Africa, Gulf of Guinea,'
                        'Northern Africa, Western Asia, Southern Asia, Eastern Asia, Central Asia')

driver.find_element_by_css_selector('input[value="{}"]'.form‌​at(geographic_area)).click()