from tavily import TavilyClient, AsyncTavilyClient


# Setup the Tavily Client
tavily_client = AsyncTavilyClient(api_key=os.environ["TAVILY_API_KEY"])


def process_response(tavily_response: dict):
    print(tavily_response)
    print(tavily_response.keys())
    # url = tavily_response["url"]
    # content = tavily_response["content"]
    # answer = tavily_response.get("answer")


# Simple Search
async def tavily_search(
    search_term,
    max_results=3,
    include_raw_content: bool = False,
    include_images: bool = True,
):
    res = await tavily_client.search(
        search_term,
        max_results=max_results,
        include_raw_content=include_raw_content,
        include_images=True,
    )


print(response["results"])
