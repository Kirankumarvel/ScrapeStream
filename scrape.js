// scrape.js
const puppeteer = require('puppeteer');
const fs = require('fs');

const SCRAPE_URL = process.env.SCRAPE_URL || 'https://example.com';

(async () => {
  try {
    const browser = await puppeteer.launch({
      headless: 'new',
      args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    const page = await browser.newPage();
    await page.goto(SCRAPE_URL, { waitUntil: 'networkidle2' });

    const scrapedData = await page.evaluate(() => {
      const title = document.querySelector('title')?.innerText || 'No title found';
      const heading = document.querySelector('h1')?.innerText || 'No heading found';
      return { title, heading };
    });

    fs.writeFileSync('scraped_data.json', JSON.stringify(scrapedData, null, 2));
    console.log('Data scraped successfully:', scrapedData);

    await browser.close();
  } catch (error) {
    console.error('Error scraping:', error);
  }
})();
