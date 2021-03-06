# Peipsi Bird Scraper

This project is a web scraper that scrapes data about birds from Pskov region and saves it to database.

To run the scraper, you need to: 
- clone the repository
- go to the directory of the project
- create .env file and add the following line:
```
DRIVER_PATH = "path to chromedriver"
```
> where "path to chromedriver" is the path to the chromedriver.exe file.
- create vertual environment
- install dependencies
- run the scraper

For example:
```
git clone 'https://github.com/Brze0x/peipsi-birds-data.git'
cd ..\peipsi-birds-data
echo 'DRIVER_PATH = "F:\driver\chromedriver.exe"' > .env
python.exe -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

> Or you can just take the database from the 'data' directory and use it in your projects.
> You can download ChromeDriver from:  https://chromedriver.chromium.org/downloads