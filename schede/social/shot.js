const {chromium}=require('playwright');const fs=require('fs'),path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
const d=__dirname;fs.mkdirSync(path.join(d,'png'),{recursive:true});
for(const f of fs.readdirSync(d).filter(f=>/^\d.*\.html$/.test(f))){await p.goto('file://'+path.join(d,f));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(200);
await p.screenshot({path:path.join(d,'png',f.replace('.html','.png'))});console.log(f);}
await b.close();})();
