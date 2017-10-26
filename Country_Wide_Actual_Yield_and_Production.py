import os
from selenium import webdriver
import zipfile
import pandas as pd
import time
import itertools

#directories
link = 'http://www.gaez.iiasa.ac.at/w/ctrl?_flow=Vwr&_view=Welcome&idAS=0&idFS=0&fieldmain=main_&idPS=0'

## Access Chrome Driver to use selenium
# Define Download Directory
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'C:/Users/dpad.intern3/Desktop/Projects/Data_Aggregation_(FAO)/Download'}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(executable_path='C:/Users/Dpad.Intern3/Desktop/Projects/Data_Aggregation_(FAO)/Chrome-Driver/chromedriver.exe',
                          chrome_options=chrome_options)
driver.get(link)

# Please provide username and password
username = input('\n\nPlease provide username')
password = input('\n\nPlease provide password')

# Function to store 'no data' element for the For Loop
driver.find_element_by_name('_username').send_keys(username)
driver.find_element_by_name('_password').send_keys(password)
driver.find_element_by_id('buttonSubmit__login').click()

# Click on Suitability and Potential Yield link
driver.find_element_by_name('_targetfieldmain=main_py&_passChanged=true&_eventtype').click()

# Click on Agro-ecological suitability and productivity link
driver.find_element_by_name('&fieldmain=main_py&idPS=0&idAS=0&idFS=0&_targetfieldmain=main_py_six&_passChanged=true&_eventtype').click()
# Click on Agro-ecological suitability and productivity list
driver.find_element_by_css_selector('input[value="{}"]'.format("Crop suitability index (value)")).click()
# Click on crop link
driver.find_element_by_css_selector("input.linksubmit[value=\"▸ Crop\"]").click()

driver.find_element_by_css_selector('input[value="{}"]'.format("Wheat")).click()
# Click on Water Supply Link
driver.find_element_by_css_selector("input.linksubmit[value=\"▸ Water Supply\"]").click()

driver.find_element_by_css_selector('input[value="{}"]'.format("Irrigation")).click()
# Click on Input Level Link
driver.find_element_by_css_selector("input.linksubmit[value=\"▸ Input Level\"]").click()

driver.find_element_by_css_selector('input[value="{}"]'.format("Intermediate")).click()

# Click on Time Period and Select Baseline
driver.find_element_by_css_selector("input.linksubmit[value=\"▸ Time Period\"]").click()
driver.find_element_by_css_selector("input.linksubmit[value=\"1961-1990\"]").click()
# Click on Geographic Areas Link
driver.find_element_by_css_selector("input.linksubmit[value=\"▸ Geographic Areas\"]").click()

data_check = driver.find_element_by_xpath("//span[contains(text(),'No data')]")
driver.find_element_by_css_selector("input.linksubmit[value=\"Logout\"]").click()

# Crop List
Crop_List = ["Wheat", "Rice", "Maize", "Sorghum", "Millet", "Other cereals",
             "White potato, Sweet potato", "Cassava, Yam and Cocoyam", "Sugarcane", "Sugarbeet", "Pulses",
             "Soybean", "Sunflower", "Rapeseed", "Groundnut", "Oilpalm", "Olive", "Vegetables", "Banana, Coconut",
             "Cotton", "Cocoa, Coffee and Tea", "Fodder crops", "Other crops"]

# Water Supply List ** Removed "Irrigation"**
Water_Supply_List = ["Rain-fed", "Irrigation"]

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
                        "Western Asia": ["Armenia", "Azerbaijan", "Cyprus", "Georgia", "Iran, Islamic Rep.", "Iraq", "Israel", "Jordan", "Kuwait", "Lebanon", "Oman", "Qatar", "Saudi Arabia", "Syrian Arab Republic", "Turkey", "United Arab Emirates", "Yemen"],
                        "South-eastern Asia": ["Cambodia", "Indonesia", "Lao PDR", "Malaysia", "Myanmar", "Papua New Guinea", "Philippines", "Thailand", "Timor-Leste", "Viet Nam"],
                        "Southern Asia": ["Bangladesh", "Bhutan", "India", "Nepal", "Pakistan", "Sri Lanka"],
                        "Eastern Asia": ["China", "Korea DPR", "Japan", "Mongolia", "Korea Rep."],
                        "Central Asia": ["Afghanistan", "Kazakhstan",  "Kyrgyzstan", "Tajikistan", "Turkmenistan", "Uzbekistan"]}

geographic_area = input('\n\nSelect a geographic area: Caribbean, Central America, South America, Australia and New Zealand,'
                        'Pacific Islands, Eastern Africa, Central Africa, Southern Africa, \n Sudano-Sahelian Africa, Gulf of Guinea, '
                        'Northern Africa, Western Asia, Southern Asia, Eastern Asia, Central Asia')
country = input('\n\n\Select a country: %s' % ",".join(continents_countries[geographic_area]))

to_loop = itertools.product(Crop_List, Water_Supply_List)


# Function that downloads all data from a country
for i in to_loop:
    driver.get(link)

    # Enter username and password
    driver.find_element_by_name('_username').send_keys(username)
    driver.find_element_by_name('_password').send_keys(password)
    driver.find_element_by_id('buttonSubmit__login').click()

    # Click on Actual Yield and Production link
    driver.find_element_by_css_selector("input.linksubmit[value=\"Actual Yield and Production\"]").click()

    # Click on Crop harvested area, yield, and production
    driver.find_element_by_css_selector("input.linksubmit[value=\"Crop harvested area, yield, and production\"]").click()
    # Click on Yield
    driver.find_element_by_css_selector("input.linksubmit[value=\"Yield\"]").click()

    # Click on crop link
    driver.find_element_by_css_selector("input.linksubmit[value=\"▸ Crop\"]").click()
    driver.find_element_by_css_selector('input[value="{}"]'.format(i[0])).click()
    Crop = i[0]

    # Click on Water Supply Link
    driver.find_element_by_css_selector("input.linksubmit[value=\"▸ Water Supply\"]").click()
    driver.find_element_by_css_selector('input[value="{}"]'.format(i[1])).click()
    Water_Supply = i[1]

    # Click on Geographic Areas Link
    driver.find_element_by_css_selector("input.linksubmit[value=\"▸ Geographic Areas\"]").click()
    # Unselect all countries
    driver.find_element_by_xpath('//*[@id="fieldareaList__pln-1"]').click()
    # Close tab for Northern Africa
    driver.find_element_by_xpath('//*[@id="rg1-66-Northern Africa"]/span').click()
    # Wait 1 second
    time.sleep(1)
    # Click geographic area then country
    driver.find_element_by_xpath('//label[text()="{}"]/following-sibling::span'.format(geographic_area)).click()
    driver.find_element_by_xpath('//label[text()="{}"]'.format(country)).click()
    # Click on Map Link
    driver.find_element_by_css_selector("input.linksubmit[value=\"▸ Map\"]").click()

    try:
        d = driver.find_elements_by_xpath("//span[contains(text(),'Cannot produce results.')]")
        if len(d) != 0:
            # log out
            driver.find_element_by_css_selector("input.linksubmit[value=\"Logout\"]").click()
            continue
    except Exception as e:
        pass

    # Download Data
    driver.find_element_by_xpath('//*[@id="buttons"]/a[4]/img').click()

    # Wait 1 second
    time.sleep(1)
    # Download blah blah
    path = 'C:/Users/dpad.intern3/Desktop/Projects/Data_Aggregation_(FAO)/Download'
    destination_folder = 'C:/Users/dpad.intern3/Desktop/Projects/Data_Aggregation_(FAO)/CSV_Files'
    # Wait 1 second
    time.sleep(1)
    file_list = [os.path.join(path, f) for f in os.listdir(path)]
    time_sorted_list = sorted(file_list, key=os.path.getmtime)
    file_name = time_sorted_list[-1]
    # decompress the zipped file here
    myzip = zipfile.ZipFile(file_name)

    # Wait 1 second
    time.sleep(1)
    # Extract data.asc file from folder
    myzip.extract('data.asc', destination_folder)

    # Save data.asc file as .csv and rename reflects download selections
    newfilename = country + Crop + Water_Supply
    df = pd.read_table(os.path.join(destination_folder, 'data.asc'), sep="\s+", skiprows=6, header=None)
    df.to_csv(os.path.join(destination_folder, '{}.csv'.format(newfilename)))

    # Delete downloaded data.asc file
    delete_data_file = "C:/Users/dpad.intern3/Desktop/Projects/Data_Aggregation_(FAO)/CSV_Files/data.asc"
    # if file exists, delete it
    if os.path.isfile(delete_data_file):
        os.remove(delete_data_file)
    else:  # Show error
        print("Error: %s file not found" % delete_data_file)

    # log out
    driver.find_element_by_css_selector("input.linksubmit[value=\"Logout\"]").click()