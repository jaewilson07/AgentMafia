import rag
import asyncio


async def main():
    # crawler, crawl_config = cw.generate_crawler()

    url = "https://ai.pydantic.dev/logfire/"

    await rag.process_urls(
        urls=[url], source="test", is_replace_llm_metadata=True, debug_prn=True
    )


if __name__ == "__main__":
    asyncio.run(main())
