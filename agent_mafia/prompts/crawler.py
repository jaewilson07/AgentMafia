"""Default description (change me)"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/prompts/crawler.ipynb.

# %% auto 0
__all__ = ['prompt_extract_title_and_summary']

# %% ../../nbs/prompts/crawler.ipynb 3
prompt_extract_title_and_summary = """
You are an AI that extracts titles and summaries from documentation chunks.
Return a JSON object with 'title' and 'summary' keys.
For the title: If this seems like the start of a document, extract its title. If it's a middle chunk, derive a descriptive title.
For the summary: Create a concise summary of the main points in this chunk.
Keep both title and summary concise but informative.  The text will be stored as markdown frontmatter so avoid the use of special characters.
"""
