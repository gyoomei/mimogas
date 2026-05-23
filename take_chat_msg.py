#!/usr/bin/env python3
"""Take chat screenshot with a message visible"""
import asyncio
import nodriver as uc

async def take_chat_with_message():
    browser = await uc.start(
        headless=True,
        browser_args=['--window-size=1920,1080', '--no-sandbox', '--disable-gpu']
    )
    
    page = await browser.get('https://gyoomei.github.io/mimogas/')
    await page.sleep(6)
    
    # Open chat
    await page.evaluate("document.getElementById('chatFab').click()")
    await page.sleep(1)
    
    # Type and send a message
    await page.evaluate("""
        const input = document.getElementById('chatInput');
        input.value = 'Which chain has the cheapest gas right now?';
        sendChat();
    """)
    await page.sleep(8)  # Wait for AI response
    
    await page.save_screenshot('/home/ubuntu/mimogas/screenshots/04_chat.png')
    print("✅ Chat with message screenshot saved")
    
    browser.stop()

asyncio.run(take_chat_with_message())
