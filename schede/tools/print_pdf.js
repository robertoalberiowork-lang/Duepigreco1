// Stampa html/*.html in pdf/*.pdf (A4) e, con --png, le anteprime in preview/.
// Uso: NODE_PATH=$(npm root -g) node tools/print_pdf.js [--png]
const {chromium} = require('playwright');
const fs = require('fs'), path = require('path');
const root = path.resolve(__dirname, '..');
(async () => {
  const png = process.argv.includes('--png');
  const browser = await chromium.launch();
  const page = await browser.newPage({viewport: {width: 794, height: 1123}, deviceScaleFactor: 2});
  fs.mkdirSync(path.join(root, 'pdf'), {recursive: true});
  if (png) fs.mkdirSync(path.join(root, 'preview'), {recursive: true});
  for (const f of fs.readdirSync(path.join(root, 'html')).filter(f => f.endsWith('.html')).sort()) {
    const name = f.replace(/\.html$/, '');
    await page.goto('file://' + path.join(root, 'html', f), {waitUntil: 'networkidle'});
    await page.evaluate(() => document.fonts.ready);
    await page.emulateMedia({media: 'print'});
    await page.pdf({path: path.join(root, 'pdf', name + '.pdf'), width: '210mm', height: '297mm', margin: {top: 0, right: 0, bottom: 0, left: 0}, printBackground: true});
    if (png) {
      const pages = await page.$$('.page');
      for (let i = 0; i < pages.length; i++)
        await pages[i].screenshot({path: path.join(root, 'preview', `${name}_p${i + 1}.png`)});
    }
    await page.emulateMedia({media: 'screen'});
    console.log('ok', name);
  }
  await browser.close();
})();
