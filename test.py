import rag
import asyncio


async def main():
    # crawler, crawl_config = cw.generate_crawler()

    url = "https://ai.pydantic.dev/examples/question-graph/"

    await rag.process_urls(urls=[url], source="test", debug_prn=True)


if __name__ == "__main__":
    asyncio.run(main())
