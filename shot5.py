import asyncio
from playwright.async_api import async_playwright
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist'])
    pg=await b.new_page(viewport={'width':412,'height':860},device_scale_factor=2)
    logs=[];pg.on('pageerror',lambda e:logs.append('ERR '+str(e)))
    await pg.goto('http://localhost:8765/index.html');await pg.wait_for_timeout(1500)
    await pg.click('.tabs [data-tab="stack"]');await pg.wait_for_timeout(300)
    await pg.click('[data-stack="0"]');await pg.wait_for_timeout(1500)
    await pg.click('#bSheet');await pg.wait_for_timeout(4000)
    await pg.screenshot(path='e_pet.png')
    await pg.click('#bSheet');await pg.wait_for_timeout(500)
    await pg.screenshot(path='e_panel.png')
    pg2=await b.new_page(viewport={'width':412,'height':860},device_scale_factor=2)
    await pg2.goto('http://localhost:8765/index.html#tools=frontend:Svelte,data:SQLite,ai:Claude%20API,plumbing:Quantum%20Pigeon,infra:Fly.io&title=Test%20App');await pg2.wait_for_timeout(4000)
    print(await pg2.inner_text('#hint'))
    await pg2.screenshot(path='e_link.png')
    await b.close();print(logs)
asyncio.run(main())
