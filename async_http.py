import asyncio
import aiohttp
import re
from bs4 import BeautifulSoup

async def get_first_sentence(text):
    match = re.match(r'([^\.!?]*[\.!?])', text)
    if match:
        return match.group(0).strip()
    else:
        return None

async def get_wikipedia_info(session, url):
    async with session.get(url) as response:
        try:
            response.raise_for_status()
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.find('h1', id='firstHeading').text
            parser_output_div = soup.find('div', {'class': 'mw-parser-output'})
            if parser_output_div:
                first_paragraph = parser_output_div.p
                if first_paragraph:
                    first_paragraph = first_paragraph.text.strip()
                    cleaned_paragraph = re.sub(r'(\[.*?\]|\([^()]*\))', '', first_paragraph)
                    first_sentence = await get_first_sentence(cleaned_paragraph)
                    return {'title': title, 'first_sentence': first_sentence, 'url': url}
        except Exception as e:
            return {'title': None, 'first_sentence': str(e), 'url': url}
    return {'title': None, 'first_sentence': "Failed to retrieve data from Wikipedia.", 'url': url}

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [get_wikipedia_info(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results
