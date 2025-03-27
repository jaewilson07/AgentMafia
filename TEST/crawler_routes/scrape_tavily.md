---
url: https://docs.tavily.com/sdk/python/quick-start
session_id: tavily_docs
updated_dt: 2025-03-27T00:16:49.181948
---
[Tavily Docs home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/tavilyai/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/tavilyai/logo/dark.svg)](https://tavily.com/)
Search or ask...
Ctrl K
  * Support
  * [Get an API key](https://app.tavily.com)
  * [Get an API key](https://app.tavily.com)


Search...
Navigation
Python
Quickstart
[Home](https://docs.tavily.com/welcome)[Documentation](https://docs.tavily.com/documentation/about)[SDKs](https://docs.tavily.com/sdk/python/quick-start)[Examples](https://docs.tavily.com/examples/use-cases/data-enrichment)
* [API Playground](https://app.tavily.com/playground)
* [Community](https://community.tavily.com)
* [Blog](https://blog.tavily.com)
##### Python
  * [Quickstart](https://docs.tavily.com/sdk/python/quick-start)
  * [SDK Reference](https://docs.tavily.com/sdk/python/reference)


##### JavaScript
  * [Quickstart](https://docs.tavily.com/sdk/javascript/quick-start)
  * [SDK Reference](https://docs.tavily.com/sdk/javascript/reference)


Python
# Quickstart
Integrate Tavily’s powerful APIs natively in your Python apps.
Looking for the Python SDK Reference? Head to our [Python SDK Reference](https://docs.tavily.com/sdk/python/reference) and learn how to use `tavily-python`.
## 
[​](https://docs.tavily.com/sdk/python/quick-start#introduction)
Introduction
The Python SDK allows for easy interaction with the Tavily API, offering the full range of our search functionality directly from your Python programs. Easily integrate smart search capabilities into your applications, harnessing Tavily’s powerful search features.
## [GitHub`/tavily-ai/tavily-python`![GitHub Repo stars](https://img.shields.io/github/stars/tavily-ai/tavily-python?style=social)](https://github.com/tavily-ai/tavily-python)## [PyPI`tavily-python`![PyPI downloads](https://img.shields.io/pypi/dm/tavily-python)](https://pypi.org/project/tavily-python)
## 
[​](https://docs.tavily.com/sdk/python/quick-start#quickstart)
Quickstart
Get started with our Python SDK in less than 5 minutes!
## [Get your free API keyYou get 1,000 free API Credits every month. **No credit card required.**](https://app.tavily.com)
### 
[​](https://docs.tavily.com/sdk/python/quick-start#installation)
Installation
You can install the Tavily Python SDK using the following:
Copy
```
pip install tavily-python

```

### 
[​](https://docs.tavily.com/sdk/python/quick-start#usage)
Usage
With Tavily’s Python SDK, you can search the web in only 4 lines of code:
Copy
```
from tavily import TavilyClient
tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
response = tavily_client.search("Who is Leo Messi?")
print(response)

```

You can also easily extract content from URLs:
Copy
```
from tavily import TavilyClient
tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
response = tavily_client.extract("https://en.wikipedia.org/wiki/Lionel_Messi")
print(response)

```

These examples are very simple, and you can do so much more with Tavily!
## 
[​](https://docs.tavily.com/sdk/python/quick-start#features)
Features
Our Python SDK supports the full feature range of our [REST API](https://docs.tavily.com/api-reference), and more. We offer both a synchronous and an asynchronous client, for increased flexibility.
  * The `search` function lets you harness the full power of Tavily Search.
  * The `extract` function allows you to easily retrieve web content with Tavily Extract.


For more details, head to the [Python SDK Reference](https://docs.tavily.com/sdk/python/reference).
[SDK Reference](https://docs.tavily.com/sdk/python/reference)
[x](https://x.com/tavilyai)[github](https://github.com/tavily-ai)[linkedin](https://linkedin.com/company/tavily)[website](https://tavily.com)
[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=docs&utm_source=docs.tavily.com)
On this page
  * [Introduction](https://docs.tavily.com/sdk/python/quick-start#introduction)
  * [Quickstart](https://docs.tavily.com/sdk/python/quick-start#quickstart)
  * [Installation](https://docs.tavily.com/sdk/python/quick-start#installation)
  * [Usage](https://docs.tavily.com/sdk/python/quick-start#usage)
  * [Features](https://docs.tavily.com/sdk/python/quick-start#features)


