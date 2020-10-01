# WeatherViz
Create maps to visualize average weather conditions of given cities on a given month.

## Quick overview 
If you know that you want to travel on a given month and you are looking for good (or specific) climatic conditions, then use this project to create your own map whith all the cities that you are interested in and visualize very quickly where you are more likely to have the weather you love. 

#### Sources
The data displayed on the map are scraped from Google wheather service, whose the source is NOAA (https://www.ncdc.noaa.gov/)

## 1. Configuration

To run this project, you need to download ChromeDriver (used for the web scraping).

### 1.1 Download ChromeDriver

Below are the steps to chose the adequate version of ChromeDriver and to download it :

- First, find out which version of Chrome you are using. Let's say you have Chrome 72.0.3626.81.

- Take the Chrome version number, remove the last part, and append the result to URL "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_". For example, with Chrome version 72.0.3626.81, you'd get a URL "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_72.0.3626".

- Use the URL created in the last step to retrieve a small file containing the version of ChromeDriver to use. For example, the above URL will get your a file containing "72.0.3626.69". (The actual number may change in the future, of course.)

- Use the version number retrieved from the previous step to construct the URL to download ChromeDriver. With version 72.0.3626.69, the URL would be "https://chromedriver.storage.googleapis.com/index.html?path=72.0.3626.69/".

- After the initial download, it is recommended that you occasionally go through the above process again to see if there are any bug fix releases.

*(tutorial source: https://chromedriver.chromium.org/downloads/version-selection)*

### 1.2 Set the ChromeDriver path

Once you downloaded the adequate Chromedriver, you need to specify its path in the project constants. 
For that you just need to edit the constants file (**WeatherViz/src/common/constants.py**) and to set the **CHROMEDRIVER_PATH** variable to your ChromeDriver path. *(example : "C:\Program Files\chromedriver_win32_v85\chromedriver.exe")*

You're ready to use WeatherViz. 

## 2. Utilisation

The utilisation of the application goes through a Notebook: **WeatherViz/notebooks/map_creation_and_export.ipynb**.

The instructions below are also described on the Notebook.

### 2.1 Specify your project path

You need to specify the path of the project root.

*example : "C:/Users/marc-/WeatherViz"*

### 2.2 Chose your month of interest

All the data are given according to a month. Chose your month of interest. 

### 2.3 Chose your cities of interest 

Edit the cities list. This list must contain all the cities you want to know about the average climatic conditions during the chosen month. 

- Be aware that if the city has some namesakes, it can entails errors. In this case you might want specify the country. 

- Moreover, try to give not too small cities because smallest cities will not have informations. If you do so it is not a problem, it will work, but don't be surprise if you don't have informations about the concerned cities in the result map.

### 2.4 Visualisation and export

You can display your map directly in the notebook and also export it in HTML.

When you export it, you need to define the path where you want to export it. 
You also need to chose a region name that describe the cities chosen and which will be used in the file name.

**I HOPE YOU WILL FIND YOUR DREAM DESTINATION !**
