#!/usr/bin/env python3
"""Take screenshots of MiMoGas at 1920x1080"""
import asyncio
import sys
import os

# Try nodriver first (lightweight, no browser install)
try:
    import nodriver as uc
    USE_NODRIVER = True
except ImportError:
    USE_NODRIVER = False

async def take_screenshots():
    output_dir = '/home/ubuntu/mimogas/screenshots'
    os.makedirs(output_dir, exist_ok=True)
    
    if USE_NODRIVER:
        browser = await uc.start(
            headless=True,
            browser_args=[
                '--window-size=1920,1080',
                '--no-sandbox',
                '--disable-gpu',
                '--disable-dev-shm-usage',
            ]
        )
        
        # Screenshot 1: Full page overview
        page = await browser.get('https://gyoomei.github.io/mimogas/')
        await page.sleep(5)  # Wait for data to load
        await page.save_screenshot(f'{output_dir}/01_dashboard.png', full_page=False)
        print("✅ Screenshot 1: Dashboard overview")
        
        # Screenshot 2: Scroll to show chain cards
        await page.scroll_down(600)
        await page.sleep(1)
        await page.save_screenshot(f'{output_dir}/02_chains.png', full_page=False)
        print("✅ Screenshot 2: Chain cards")
        
        # Screenshot 3: Scroll to AI recommendations + ranking
        await page.scroll_down(800)
        await page.sleep(1)
        await page.save_screenshot(f'{output_dir}/03_ai_ranking.png', full_page=False)
        print("✅ Screenshot 3: AI recommendations & ranking")
        
        # Screenshot 4: Open chat panel
        chat_btn = await page.find('💬', timeout=5)
        if chat_btn:
            await chat_btn.click()
            await page.sleep(2)
            await page.save_screenshot(f'{output_dir}/04_chat.png', full_page=False)
            print("✅ Screenshot 4: Chat with MiMo")
        else:
            # Fallback: scroll to bottom for chat
            await page.scroll_down(2000)
            await page.sleep(1)
            await page.save_screenshot(f'{output_dir}/04_chat.png', full_page=False)
            print("✅ Screenshot 4: Footer (chat button not found)")
        
        browser.stop()
    else:
        # Fallback to Playwright
        from playwright.async_api import async_playwright
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=True,
                args=['--no-sandbox', '--disable-gpu']
            )
            context = await browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                device_scale_factor=1
            )
            page = await context.new_page()
            
            # Screenshot 1: Full page overview
            await page.goto('https://gyoomei.github.io/mimogas/', wait_until='networkidle', timeout=30000)
            await page.wait_for_timeout(5000)
            await page.screenshot(path=f'{output_dir}/01_dashboard.png')
            print("✅ Screenshot 1: Dashboard overview")
            
            # Screenshot 2: Chain cards
            await page.evaluate('window.scrollBy(0, 600)')
            await page.wait_for_timeout(1000)
            await page.screenshot(path=f'{output_dir}/02_chains.png')
            print("✅ Screenshot 2: Chain cards")
            
            # Screenshot 3: AI + ranking
            await page.evaluate('window.scrollBy(0, 800)')
            await page.wait_for_timeout(1000)
            await page.screenshot(path=f'{output_dir}/03_ai_ranking.png')
            print("✅ Screenshot 3: AI recommendations & ranking")
            
            # Screenshot 4: Chat panel
            try:
                await page.click('text=💬', timeout=5000)
                await page.wait_for_timeout(2000)
            except:
                await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
                await page.wait_for_timeout(1000)
            await page.screenshot(path=f'{output_dir}/04_chat.png')
            print("✅ Screenshot 4: Chat with MiMo")
            
            await browser.close()
    
    print(f"\nAll screenshots saved to {output_dir}/")

asyncio.run(take_screenshots())
