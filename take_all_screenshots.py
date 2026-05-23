#!/usr/bin/env python3
"""Take all 5 screenshots at exactly 1920x1080 using CDP viewport override"""
import asyncio
import nodriver as uc
import os

OUTPUT = '/home/ubuntu/mimogas/screenshots'
os.makedirs(OUTPUT, exist_ok=True)

async def main():
    browser = await uc.start(
        headless=True,
        browser_args=[
            '--window-size=1920,1200',  # Oversize, we'll override viewport
            '--no-sandbox',
            '--disable-gpu',
            '--disable-dev-shm-usage',
            '--force-device-scale-factor=1',
        ]
    )
    
    # ---- Project Screenshots ----
    page = await browser.get('https://gyoomei.github.io/mimogas/')
    
    # Override viewport to exact 1920x1080 via CDP
    await page.send(uc.cdp.emulation.set_device_metrics_override(
        width=1920, height=1080, device_scale_factor=1, mobile=False
    ))
    await page.sleep(6)
    
    # Screenshot 1: Dashboard overview
    await page.save_screenshot(f'{OUTPUT}/01_dashboard.png')
    print("✅ 01_dashboard.png")
    
    # Screenshot 2: Chain cards
    await page.scroll_down(500)
    await page.sleep(1)
    await page.save_screenshot(f'{OUTPUT}/02_chains.png')
    print("✅ 02_chains.png")
    
    # Screenshot 3: AI + ranking
    await page.scroll_down(700)
    await page.sleep(1)
    await page.save_screenshot(f'{OUTPUT}/03_ai_ranking.png')
    print("✅ 03_ai_ranking.png")
    
    # Screenshot 4: Chat with MiMo
    await page.evaluate("document.getElementById('chatFab').click()")
    await page.sleep(1)
    await page.evaluate("""
        const input = document.getElementById('chatInput');
        input.value = 'Which chain has the cheapest gas right now?';
        sendChat();
    """)
    await page.sleep(8)
    await page.save_screenshot(f'{OUTPUT}/04_chat.png')
    print("✅ 04_chat.png")
    
    # ---- GitHub Screenshot ----
    page2 = await browser.get('https://github.com/gyoomei/mimogas')
    await page2.send(uc.cdp.emulation.set_device_metrics_override(
        width=1920, height=1080, device_scale_factor=1, mobile=False
    ))
    await page.sleep(5)
    await page2.save_screenshot(f'{OUTPUT}/05_github.png')
    print("✅ 05_github.png")
    
    browser.stop()
    print(f"\nDone! 5 screenshots in {OUTPUT}/")

asyncio.run(main())
