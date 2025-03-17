from typing import List
import requests
from xml.etree import ElementTree
import asyncio
import agent_mafia.implementations.scrape_urls as scu
import sys

sys.path.append(".")


async def main():
    # Get URLs from Pydantic AI docs

    url = input("enter url:")
    source = input("enter source:")

    await scu.process_urls(urls=[url], source=source, debug_prn=True)


if __name__ == "__main__":
    asyncio.run(main())
