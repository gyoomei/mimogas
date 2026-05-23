#!/usr/bin/env python3
"""Take GitHub repo screenshot"""
import asyncio
import nodriver as uc

async def take_github():
    browser = await uc.start(
        headless=True,
        browser_args=['--window-size=1920,1080', '--no-sandbox', '--disable-gpu']
    )
    
    page = await browser.get('https://github.com/gyoomei/mimogas')
    await page.sleep(5)
    
    await page.save_screenshot('/home/ubuntu/mimogas/screenshots/05_github.png')
    print("✅ GitHub screenshot saved")
    
    browser.stop()

asyncio.run(take_github())
