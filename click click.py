import os
from io import StringIO
import time
import zipfile
import csv
import pandas as pd
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
driver = webdriver.Chrome(executable_path='C:/Users/chakw/OneDrive/Documents/Github/Data_Aggregation_(FAO)/Chrome-Driver/chromedriver.exe',
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
driver.find_element_by_css_selector("input.linksubmit[value=\"▸ Water Supply\"]").click()
# Select Water Supply
water_supply = input('\n\nSelect a water supply: Rain-fed, Irrigation, Gravity irrigation, Sprinkler irrigation, Drip irrigation')
driver.find_element_by_css_selector('input[value="{}"]'.format(water_supply)).click()

# Click on Input Level Link
driver.find_element_by_css_selector("input.linksubmit[value=\"▸ Input Level\"]").click()
# Select Input Level
input_level = input('\n\nSelect an input level: High, Intermediate, Low')
driver.find_element_by_css_selector('input[value="{}"]'.format(input_level)).click()

# Click on Time Period and Select Baseline
driver.find_element_by_css_selector("input.linksubmit[value=\"▸ Time Period\"]").click()
driver.find_element_by_css_selector("input.linksubmit[value=\"1961-1990\"]").click()

# Click on Geographic Areas Link
driver.find_element_by_css_selector("input.linksubmit[value=\"▸ Geographic Areas\"]").click()
# Unselect all countries
driver.find_element_by_xpath('//*[@id="fieldareaList__pln-1"]').click()
# Close tab for Northern Africa
driver.find_element_by_xpath('//*[@id="rg1-66-Northern Africa"]/span').click()
# Select a Geographic Area
continents_countries = {"Caribbean": ["Bahamas", "Cuba", "Dominican Republic", "Haiti", "Jamaica", "Puerto Rico"],
                        "Central America": ["Belize", "Costa Rica", "El Salvador", "Guatemala", "Honduras", "Mexico", "Nicaragua", "Panama"],
                        "South America": ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "French Guiana", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"],
                        "Australia and New Zealand": ["Australia", "New Zealand"],
                        "Pacific Islands": ["Fiji", "French Polynesia", "New Caledonia", "Solomon Islands", "Vanuatu"],
                        "Eastern Africa": ["Burundi", "Ethiopia", "Kenya", "Madagascar", "Rwanda", "Uganda", "Tanzania UR"],
                        "Central Africa": ["Angola", "Cameroon", "Central African Republic", "Congo, Rep.", "Congo, Dem. Rep.", "Equatorial Guinea", "Gabon"],
                        "Southern Africa": ["Botswana", "Lesotho", "Malawi", "Mozambique", "Namibia", "South Africa", "Swaziland", "Zambia", "Zimbabwe"],
                        "Sudano-Sahelian Africa": ["Burkina Faso", "Chad", "Djibouti", "Eritrea", "Gambia", "Mali", "Mauritania", "Niger", "Senegal", "Somalia", "Sudan", "South Sudan"],
                        "Gulf of Guinea": ["Benin", "Cote d'lvoire", "Ghana", "Guinea-Bissau", "Guinea", "Liberia", "Nigeria", "Sierra Leone", "Togo"],
                        "Northern Africa": ["Algeria", "Libyan Arab Jamahiriya", "Morocco", "Tunisia", "Egypt"],
                        "Western Asia": ["Armenia", "Azerbaijan", "Cyprus", "Georgia", "Iran, Islamic Rep.", "Iraq", "Israel", "Jordan", "Kuwait", "Lebanon", "Oman", "Qatar", "Saudi Arabia","Syrian Arab Republic", "Turkey", "United Arab Emirates", "Yemen"],
                        "South-eastern Asia": ["Cambodia", "Indonesia", "Lao PDR", "Malaysia", "Myanmar", "Papua New Guinea", "Philippines", "Thailand", "Timor-Leste", "Viet Nam"],
                        "Southern Asia": ["Bangladesh", "Bhutan", "India", "Nepal", "Pakistan", "Sri Lanka"],
                        "Eastern Asia": ["China", "Korea DPR", "Japan", "Mongolia", "Korea Rep."],
                        "Central Asia": ["Afghanistan", "Kazakhstan",  "Kyrgyzstan", "Tajikistan", "Turkmenistan", "Uzbekistan"]}

geographic_area = input('\n\nSelect a geographic area: Caribbean, Central America, South America, Australia and New Zealand,'
                        'Pacific Islands, Eastern Africa, Central Africa, Southern Africa, \n Sudano-Sahelian Africa, Gulf of Guinea,'
                        'Northern Africa, Western Asia, Southern Asia, Eastern Asia, Central Asia')
country = input('\n\n\Select a country: %s' % ",".join(continents_countries[geographic_area]))
driver.find_element_by_xpath('//label[text()="{}"]/following-sibling::span'.format(geographic_area)).click()
driver.find_element_by_xpath('//label[text()="{}"]'.format(country)).click()

# Click on Map Link
driver.find_element_by_css_selector("input.linksubmit[value=\"▸ Map\"]").click()
# Download Data
driver.find_element_by_xpath('//*[@id="buttons"]/a[4]/img').click()

# Unzip file
path = 'C:/Users/chakw/OneDrive/Documents/Github/Data_Aggregation_(FAO)/Download'
file_list = [os.path.join(path, f) for f in os.listdir(path)]
time_sorted_list = sorted(file_list, key=os.path.getmtime)
file_name = time_sorted_list[-1]
myzip = zipfile.ZipFile(file_name)
for data in myzip.namelist():
    new_name = os.rename(data, crop+country)
    myzip.namelist(new_name, path)
fh.close()

for data in myzip.namelist():
    myzip.namelist(data, path)


new_file_name = crop+country

for data in myzip.namelist():
    new_name = os.rename(data, new_file_name)
data_xls = pd.read_excel('data.asc', index_col=None)
data_xls.to_csv('exceltocsv.csv', encoding='utf-8')









folder = r'C:/Users/chakw/OneDrive/Documents/Github/Data_Aggregation_(FAO)/Download'
file_list = [os.path.join(path, f) for f in os.listdir(folder)]
time_sorted_list = sorted(file_list, key=os.path.getmtime)
file_name = time_sorted_list[-1]

files = os.listdir(folder)
for file in files:
    if file.endswith(".zip"):
        print(file + " " + time.ctime(os.path.getatime(os.path.join(folder,file))))





path = 'C:/Users/dpad.intern3/Desktop/Projects/Data_Aggregation_(FAO)/Download'
file_list = [os.path.join(path, f) for f in os.listdir(path)]
time_sorted_list = sorted(list, key=os.path.getmtime)
file_name = time_sorted_list[-1]



myzipfile = zipfile.Zipfile(StringIO(get_zip_data(file_name)))
for name in myzipfile.namelist():
    [ ... ]

zipdata = StringIO()
zipdata.write(get_zip_data())
myzipfile = zipfile.ZipFile(zipdata)
foofile = myzipfile.open('foo.txt')
print foofile.read()