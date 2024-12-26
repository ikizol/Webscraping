import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

# Initialize Safari WebDriver (this should automatically use the built-in SafariDriver)
driver = webdriver.Safari()

# Open a website
driver.get("https://www.yearupalumni.org/s/1841/interior.aspx?sid=1841&gid=2&pgid=440")

results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content)
# Close the browser
driver.quit()

for element in soup.findAll(attrs='title'):
    name = element.find('a')
    if name not in results:
        results.append(name.text)

df = pd.DataFrame({ 'Names': results})
df.to_csv('names.csv', index=False, encoding='utf-8')
