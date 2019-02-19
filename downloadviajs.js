const fs = require('fs');
const webdriver = require('selenium-webdriver');
const chromedriver = require('chromedriver');

const chromeCapabilities = webdriver.Capabilities.chrome();
//chromeCapabilities.set('chromeOptions', {args: ['--headless']});

const driver = new webdriver.Builder()
  .forBrowser('chrome')
  .withCapabilities(chromeCapabilities)
  .build();

// Navigate to google.com, enter a search.
driver.get('https://www.nseindia.com/products/content/equities/equities/archieve_eq.htm');
//driver.findElement({name: 'q'}).sendKeys('webdriver');
selectElem=driver.findElement({id: 'h_filetype'});// select dropdown element you wish to select
selectElem.click()
selectElem.findElement(webdriver.By.css("option[value='eqbhav']")).click()
driver.findElement({id: 'date'}).sendKeys('15-02-2019');
#driver.findElement({id: 'date'}).sendKeys('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[6]/a')
driver.findElement({id: 'date'}).sendKeys(webdriver.Key.ENTER);

driver.findElement({className:'getdata-button'}).click()

/*driver.wait(webdriver.until.titleIs('webdriver - Google Search'), 1000);

// Take screenshot of results page. Save to disk.
driver.takeScreenshot().then(base64png => {
  fs.writeFileSync('screenshot.png', new Buffer(base64png, 'base64'));
});

driver.quit();*/
