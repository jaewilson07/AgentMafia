from typing import Union, List


def chunk_calc_end_codeblock(chunk, chunk_size, start) -> Union[int, bool]:
  code_block = chunk.rfind('```')
  if code_block == -1 or code_block <= chunk_size * .3:
    return False

  return start + code_block

def chunk_calk_end_paragraph(chunk, chunk_size, start) -> Union[int, bool]:
  last_break = chunk.rfind('\n\n')

  if last_break == -1 or last_break <= chunk_size * .3:
    return False 

  return start + last_break

def calc_end_sentence(chunk,chunk_size, start) -> Union[int, bool]:
  last_period = chunk.rfind('. ')

  if last_period == -1 or last_period <= chunk_size * .3:
    return False

  return start + last_period + 1

def chunk_text(text: str, # text to chunk
               chunk_size: int = 5000) -> List[str]:
  chunks = []
  start = 0
  text_length = len(text)

  while start < text_length:
    end = start + chunk_size

    if end >= text_length:
      chunks.append(text[start:].strip())
      break

    # handle code block
    chunk = text[start  : end]
    end = chunk_calc_end_codeblock(chunk, chunk_size, start)

