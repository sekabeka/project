from playwright.async_api import async_playwright, BrowserContext
from proxies import proxys

import asyncio
import json




async def _cookies(context:BrowserContext, proxy:dict):
    page = await context.new_page()
    try:
        await page.goto(
            url='https://www.auchan.ru',
            wait_until='load'
        )
    except:
        pass
    await page.wait_for_timeout(10 * 1000)

    cookies = await context.cookies()

    return cookies, f"http://{proxy['username']}:{proxy['password']}@{proxy['server']}"


async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch()
        contexts = [
            (await browser.new_context(proxy=proxy), proxy) for proxy in proxys()
        ]
        result = await asyncio.gather(
            *[_cookies(*context) for context in contexts]
        )
    return result
        

def run():
    return asyncio.run(main())


