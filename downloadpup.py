import asyncio
from pyppeteer import launch

async def main():
    browser = await launch({"headless": False})
    page = await browser.newPage()
    await page.goto('https://www.nseindia.com/products/content/equities/equities/archieve_eq.htm')
    
    await page.select('#h_filetype', 'eqbhav')
    await page.type('#date', '18-02-2019')
    await page.keyboard.press('Enter')
    #await page.click('input[class="getdata-button')
    #await asyncio.gather(
    #page.waitForNavigation(waitOptions),
    #page.click('input[class="getdata-button'),
    #)
    await page.click('input[class="getdata-button')
    #await page.click("//input[contains(text(), 'Get Data')]");
    await page.waitFor(10000)
 
   # print(dimensions)
    # >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}
    #await browser.close()
    await page.screenshot({'path': 'example.png'})

asyncio.get_event_loop().run_until_complete(main())