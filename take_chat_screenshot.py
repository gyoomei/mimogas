#!/usr/bin/env python3
"""Take chat screenshot using JS click"""
import asyncio
import nodriver as uc

async def take_chat_screenshot():
    browser = await uc.start(
        headless=True,
        browser_args=['--window-size=1920,1080', '--no-sandbox', '--disable-gpu']
    )
    
    page = await browser.get('https://gyoomei.github.io/mimogas/')
    await page.sleep(5)
    
    # Click chat FAB via JavaScript
    await page.evaluate("document.getElementById('chatFab').click()")
    await page.sleep(2)
    
    await page.save_screenshot('/home/ubuntu/mimogas/screenshots/04_chat.png')
    print("✅ Chat screenshot saved")
    
    browser.stop()

asyncio.run(take_chat_screenshot())
