#!/usr/bin/env python3
import asyncio, nodriver as uc

async def check():
    b = await uc.start(headless=True, browser_args=['--window-size=1920,1080','--no-sandbox','--disable-gpu'])
    p = await b.get('https://gyoomei.github.io/mimogas/')
    await p.send(uc.cdp.emulation.set_device_metrics_override(width=1920, height=1080, device_scale_factor=1, mobile=False))
    await p.sleep(20)
    
    result = await p.evaluate('''
        Array.from(document.querySelectorAll(".chain-card")).map(c => {
            const title = c.querySelector(".chain-title")?.textContent || "?";
            const hasError = c.textContent.includes("unreachable");
            // Get gas price specifically (first data-value in chain-data)
            const gasEl = c.querySelector(".chain-data .data-value");
            const gas = gasEl ? gasEl.textContent.trim() : "no data";
            return (hasError ? "❌" : "✅") + " " + title + ": " + (hasError ? "FAILED" : gas);
        }).join("\\n")
    ''')
    print(result)
    
    await p.save_screenshot('/home/ubuntu/mimogas/screenshots/final_check.png')
    b.stop()

asyncio.run(check())
