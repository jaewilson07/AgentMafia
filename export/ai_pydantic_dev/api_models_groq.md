---
url: https://ai.pydantic.dev/api/models/groq/
session_id: pydantic_ai_docs
updated_dt: 2025-03-14T09:20:46.906029
---
[ Skip to content ](https://ai.pydantic.dev/api/models/groq/#pydantic_aimodelsgroq)
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI")
PydanticAI 
pydantic_ai.models.groq 
Type to start searching
[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI") PydanticAI 
[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")
  * [ Introduction  ](https://ai.pydantic.dev/)
  * [ Installation  ](https://ai.pydantic.dev/install/)
  * [ Getting Help  ](https://ai.pydantic.dev/help/)
  * [ Contributing  ](https://ai.pydantic.dev/contributing/)
  * [ Troubleshooting  ](https://ai.pydantic.dev/troubleshooting/)
  * Documentation  Documentation 
    * [ Agents  ](https://ai.pydantic.dev/agents/)
    * [ Models  ](https://ai.pydantic.dev/models/)
    * [ Dependencies  ](https://ai.pydantic.dev/dependencies/)
    * [ Function Tools  ](https://ai.pydantic.dev/tools/)
    * [ Common Tools  ](https://ai.pydantic.dev/common_tools/)
    * [ Results  ](https://ai.pydantic.dev/results/)
    * [ Messages and chat history  ](https://ai.pydantic.dev/message-history/)
    * [ Testing and Evals  ](https://ai.pydantic.dev/testing-evals/)
    * [ Debugging and Monitoring  ](https://ai.pydantic.dev/logfire/)
    * [ Multi-agent Applications  ](https://ai.pydantic.dev/multi-agent-applications/)
    * [ Graphs  ](https://ai.pydantic.dev/graph/)
    * [ Image, Audio & Document Input  ](https://ai.pydantic.dev/input/)
    * [ Command Line Interface (CLI)  ](https://ai.pydantic.dev/cli/)
  * [ Examples  ](https://ai.pydantic.dev/examples/)
Examples 
    * [ Pydantic Model  ](https://ai.pydantic.dev/examples/pydantic-model/)
    * [ Weather agent  ](https://ai.pydantic.dev/examples/weather-agent/)
    * [ Bank support  ](https://ai.pydantic.dev/examples/bank-support/)
    * [ SQL Generation  ](https://ai.pydantic.dev/examples/sql-gen/)
    * [ Flight booking  ](https://ai.pydantic.dev/examples/flight-booking/)
    * [ RAG  ](https://ai.pydantic.dev/examples/rag/)
    * [ Stream markdown  ](https://ai.pydantic.dev/examples/stream-markdown/)
    * [ Stream whales  ](https://ai.pydantic.dev/examples/stream-whales/)
    * [ Chat App with FastAPI  ](https://ai.pydantic.dev/examples/chat-app/)
    * [ Question Graph  ](https://ai.pydantic.dev/examples/question-graph/)
  * API Reference  API Reference 
    * [ pydantic_ai.agent  ](https://ai.pydantic.dev/api/agent/)
    * [ pydantic_ai.tools  ](https://ai.pydantic.dev/api/tools/)
    * [ pydantic_ai.common_tools  ](https://ai.pydantic.dev/api/common_tools/)
    * [ pydantic_ai.result  ](https://ai.pydantic.dev/api/result/)
    * [ pydantic_ai.messages  ](https://ai.pydantic.dev/api/messages/)
    * [ pydantic_ai.exceptions  ](https://ai.pydantic.dev/api/exceptions/)
    * [ pydantic_ai.settings  ](https://ai.pydantic.dev/api/settings/)
    * [ pydantic_ai.usage  ](https://ai.pydantic.dev/api/usage/)
    * [ pydantic_ai.format_as_xml  ](https://ai.pydantic.dev/api/format_as_xml/)
    * [ pydantic_ai.models  ](https://ai.pydantic.dev/api/models/base/)
    * [ pydantic_ai.models.openai  ](https://ai.pydantic.dev/api/models/openai/)
    * [ pydantic_ai.models.anthropic  ](https://ai.pydantic.dev/api/models/anthropic/)
    * [ pydantic_ai.models.bedrock  ](https://ai.pydantic.dev/api/models/bedrock/)
    * [ pydantic_ai.models.cohere  ](https://ai.pydantic.dev/api/models/cohere/)
    * [ pydantic_ai.models.gemini  ](https://ai.pydantic.dev/api/models/gemini/)
    * [ pydantic_ai.models.vertexai  ](https://ai.pydantic.dev/api/models/vertexai/)
    * pydantic_ai.models.groq  [ pydantic_ai.models.groq  ](https://ai.pydantic.dev/api/models/groq/) Table of contents 
      * [ Setup  ](https://ai.pydantic.dev/api/models/groq/#setup)
        * [ groq  ](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq)
        * [ LatestGroqModelNames  ](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.LatestGroqModelNames)
        * [ GroqModelName  ](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.GroqModelName)
        * [ GroqModelSettings  ](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.GroqModelSettings)
        * [ GroqModel  ](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.GroqModel)
          * [ __init__  ](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.GroqModel.__init__)
          * [ model_name  ](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.GroqModel.model_name)
          * [ system  ](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.GroqModel.system)
        * [ GroqStreamedResponse  ](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.GroqStreamedResponse)
          * [ model_name  ](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.GroqStreamedResponse.model_name)
          * [ timestamp  ](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.GroqStreamedResponse.timestamp)
    * [ pydantic_ai.models.mistral  ](https://ai.pydantic.dev/api/models/mistral/)
    * [ pydantic_ai.models.test  ](https://ai.pydantic.dev/api/models/test/)
    * [ pydantic_ai.models.function  ](https://ai.pydantic.dev/api/models/function/)
    * [ pydantic_ai.models.fallback  ](https://ai.pydantic.dev/api/models/fallback/)
    * [ pydantic_ai.providers  ](https://ai.pydantic.dev/api/providers/)
    * [ pydantic_graph  ](https://ai.pydantic.dev/api/pydantic_graph/graph/)
    * [ pydantic_graph.nodes  ](https://ai.pydantic.dev/api/pydantic_graph/nodes/)
    * [ pydantic_graph.state  ](https://ai.pydantic.dev/api/pydantic_graph/state/)
    * [ pydantic_graph.mermaid  ](https://ai.pydantic.dev/api/pydantic_graph/mermaid/)
    * [ pydantic_graph.exceptions  ](https://ai.pydantic.dev/api/pydantic_graph/exceptions/)


Table of contents 
  * [ Setup  ](https://ai.pydantic.dev/api/models/groq/#setup)
    * [ groq  ](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq)
    * [ LatestGroqModelNames  ](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.LatestGroqModelNames)
    * [ GroqModelName  ](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.GroqModelName)
    * [ GroqModelSettings  ](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.GroqModelSettings)
    * [ GroqModel  ](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.GroqModel)
      * [ __init__  ](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.GroqModel.__init__)
      * [ model_name  ](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.GroqModel.model_name)
      * [ system  ](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.GroqModel.system)
    * [ GroqStreamedResponse  ](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.GroqStreamedResponse)
      * [ model_name  ](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.GroqStreamedResponse.model_name)
      * [ timestamp  ](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.GroqStreamedResponse.timestamp)


# `pydantic_ai.models.groq`
## Setup
For details on how to set up authentication with this model, see [model configuration for Groq](https://ai.pydantic.dev/models/#groq).
###  LatestGroqModelNames `module-attribute`
```
LatestGroqModelNames = Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")[
  "llama-3.3-70b-versatile",
  "llama-3.3-70b-specdec",
  "llama-3.1-8b-instant",
  "llama-3.2-1b-preview",
  "llama-3.2-3b-preview",
  "llama-3.2-11b-vision-preview",
  "llama-3.2-90b-vision-preview",
  "llama3-70b-8192",
  "llama3-8b-8192",
  "mixtral-8x7b-32768",
  "gemma2-9b-it",
]

```

Latest Groq models.
###  GroqModelName `module-attribute`
```
GroqModelName = Union[](https://docs.python.org/3/library/typing.html#typing.Union "typing.Union")[str[](https://docs.python.org/3/library/stdtypes.html#str), LatestGroqModelNames[](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.LatestGroqModelNames "pydantic_ai.models.groq.LatestGroqModelNames")]

```

Possible Groq model names.
Since Groq supports a variety of date-stamped models, we explicitly list the latest models but allow any name in the type hints. See [the Groq docs](https://console.groq.com/docs/models) for a full list.
###  GroqModelSettings
Bases: `ModelSettings[](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings "pydantic_ai.settings.ModelSettings")`
Settings used for a Groq model request.
Source code in `pydantic_ai_slim/pydantic_ai/models/groq.py`
```
73
74
```
| ```
classGroqModelSettings(ModelSettings):
"""Settings used for a Groq model request."""

```
  
---|---  
###  GroqModel `dataclass`
Bases: `Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "pydantic_ai.models.Model")`
A model that uses the Groq API.
Internally, this uses the [Groq Python client](https://github.com/groq/groq-python) to interact with the API.
Apart from `__init__`, all methods are private or match those of the base class.
Source code in `pydantic_ai_slim/pydantic_ai/models/groq.py`
```
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
```
| ```
@dataclass(init=False)
classGroqModel(Model):
"""A model that uses the Groq API.
  Internally, this uses the [Groq Python client](https://github.com/groq/groq-python) to interact with the API.
  Apart from `__init__`, all methods are private or match those of the base class.
  """
  client: AsyncGroq = field(repr=False)
  _model_name: GroqModelName = field(repr=False)
  _system: str | None = field(default='groq', repr=False)
  @overload
  def__init__(
    self,
    model_name: GroqModelName,
    *,
    provider: Literal['groq'] | Provider[AsyncGroq] = 'groq',
  ) -> None: ...
  @deprecated('Use the `provider` parameter instead of `api_key`, `groq_client`, and `http_client`.')
  @overload
  def__init__(
    self,
    model_name: GroqModelName,
    *,
    provider: None = None,
    api_key: str | None = None,
    groq_client: AsyncGroq | None = None,
    http_client: AsyncHTTPClient | None = None,
  ) -> None: ...
  def__init__(
    self,
    model_name: GroqModelName,
    *,
    provider: Literal['groq'] | Provider[AsyncGroq] | None = None,
    api_key: str | None = None,
    groq_client: AsyncGroq | None = None,
    http_client: AsyncHTTPClient | None = None,
  ):
"""Initialize a Groq model.
    Args:
      model_name: The name of the Groq model to use. List of model names available
        [here](https://console.groq.com/docs/models).
      provider: The provider to use for authentication and API access. Can be either the string
        'groq' or an instance of `Provider[AsyncGroq]`. If not provided, a new provider will be
        created using the other parameters.
      api_key: The API key to use for authentication, if not provided, the `GROQ_API_KEY` environment variable
        will be used if available.
      groq_client: An existing
        [`AsyncGroq`](https://github.com/groq/groq-python?tab=readme-ov-file#async-usage)
        client to use, if provided, `api_key` and `http_client` must be `None`.
      http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.
    """
    self._model_name = model_name
    if provider is not None:
      if isinstance(provider, str):
        self.client = infer_provider(provider).client
      else:
        self.client = provider.client
    elif groq_client is not None:
      assert http_client is None, 'Cannot provide both `groq_client` and `http_client`'
      assert api_key is None, 'Cannot provide both `groq_client` and `api_key`'
      self.client = groq_client
    elif http_client is not None:
      self.client = AsyncGroq(api_key=api_key, http_client=http_client)
    else:
      self.client = AsyncGroq(api_key=api_key, http_client=cached_async_http_client())
  @property
  defbase_url(self) -> str:
    return str(self.client.base_url)
  async defrequest(
    self,
    messages: list[ModelMessage],
    model_settings: ModelSettings | None,
    model_request_parameters: ModelRequestParameters,
  ) -> tuple[ModelResponse, usage.Usage]:
    check_allow_model_requests()
    response = await self._completions_create(
      messages, False, cast(GroqModelSettings, model_settings or {}), model_request_parameters
    )
    return self._process_response(response), _map_usage(response)
  @asynccontextmanager
  async defrequest_stream(
    self,
    messages: list[ModelMessage],
    model_settings: ModelSettings | None,
    model_request_parameters: ModelRequestParameters,
  ) -> AsyncIterator[StreamedResponse]:
    check_allow_model_requests()
    response = await self._completions_create(
      messages, True, cast(GroqModelSettings, model_settings or {}), model_request_parameters
    )
    async with response:
      yield await self._process_streamed_response(response)
  @property
  defmodel_name(self) -> GroqModelName:
"""The model name."""
    return self._model_name
  @property
  defsystem(self) -> str | None:
"""The system / model provider."""
    return self._system
  @overload
  async def_completions_create(
    self,
    messages: list[ModelMessage],
    stream: Literal[True],
    model_settings: GroqModelSettings,
    model_request_parameters: ModelRequestParameters,
  ) -> AsyncStream[chat.ChatCompletionChunk]:
    pass
  @overload
  async def_completions_create(
    self,
    messages: list[ModelMessage],
    stream: Literal[False],
    model_settings: GroqModelSettings,
    model_request_parameters: ModelRequestParameters,
  ) -> chat.ChatCompletion:
    pass
  async def_completions_create(
    self,
    messages: list[ModelMessage],
    stream: bool,
    model_settings: GroqModelSettings,
    model_request_parameters: ModelRequestParameters,
  ) -> chat.ChatCompletion | AsyncStream[chat.ChatCompletionChunk]:
    tools = self._get_tools(model_request_parameters)
    # standalone function to make it easier to override
    if not tools:
      tool_choice: Literal['none', 'required', 'auto'] | None = None
    elif not model_request_parameters.allow_text_result:
      tool_choice = 'required'
    else:
      tool_choice = 'auto'
    groq_messages = list(chain(*(self._map_message(m) for m in messages)))
    try:
      return await self.client.chat.completions.create(
        model=str(self._model_name),
        messages=groq_messages,
        n=1,
        parallel_tool_calls=model_settings.get('parallel_tool_calls', NOT_GIVEN),
        tools=tools or NOT_GIVEN,
        tool_choice=tool_choice or NOT_GIVEN,
        stream=stream,
        max_tokens=model_settings.get('max_tokens', NOT_GIVEN),
        temperature=model_settings.get('temperature', NOT_GIVEN),
        top_p=model_settings.get('top_p', NOT_GIVEN),
        timeout=model_settings.get('timeout', NOT_GIVEN),
        seed=model_settings.get('seed', NOT_GIVEN),
        presence_penalty=model_settings.get('presence_penalty', NOT_GIVEN),
        frequency_penalty=model_settings.get('frequency_penalty', NOT_GIVEN),
        logit_bias=model_settings.get('logit_bias', NOT_GIVEN),
      )
    except APIStatusError as e:
      if (status_code := e.status_code) >= 400:
        raise ModelHTTPError(status_code=status_code, model_name=self.model_name, body=e.body) frome
      raise
  def_process_response(self, response: chat.ChatCompletion) -> ModelResponse:
"""Process a non-streamed response, and prepare a message to return."""
    timestamp = datetime.fromtimestamp(response.created, tz=timezone.utc)
    choice = response.choices[0]
    items: list[ModelResponsePart] = []
    if choice.message.content is not None:
      items.append(TextPart(content=choice.message.content))
    if choice.message.tool_calls is not None:
      for c in choice.message.tool_calls:
        items.append(ToolCallPart(tool_name=c.function.name, args=c.function.arguments, tool_call_id=c.id))
    return ModelResponse(items, model_name=response.model, timestamp=timestamp)
  async def_process_streamed_response(self, response: AsyncStream[chat.ChatCompletionChunk]) -> GroqStreamedResponse:
"""Process a streamed response, and prepare a streaming response to return."""
    peekable_response = _utils.PeekableAsyncStream(response)
    first_chunk = await peekable_response.peek()
    if isinstance(first_chunk, _utils.Unset):
      raise UnexpectedModelBehavior('Streamed response ended without content or tool calls')
    return GroqStreamedResponse(
      _response=peekable_response,
      _model_name=self._model_name,
      _timestamp=datetime.fromtimestamp(first_chunk.created, tz=timezone.utc),
    )
  def_get_tools(self, model_request_parameters: ModelRequestParameters) -> list[chat.ChatCompletionToolParam]:
    tools = [self._map_tool_definition(r) for r in model_request_parameters.function_tools]
    if model_request_parameters.result_tools:
      tools += [self._map_tool_definition(r) for r in model_request_parameters.result_tools]
    return tools
  def_map_message(self, message: ModelMessage) -> Iterable[chat.ChatCompletionMessageParam]:
"""Just maps a `pydantic_ai.Message` to a `groq.types.ChatCompletionMessageParam`."""
    if isinstance(message, ModelRequest):
      yield from self._map_user_message(message)
    elif isinstance(message, ModelResponse):
      texts: list[str] = []
      tool_calls: list[chat.ChatCompletionMessageToolCallParam] = []
      for item in message.parts:
        if isinstance(item, TextPart):
          texts.append(item.content)
        elif isinstance(item, ToolCallPart):
          tool_calls.append(self._map_tool_call(item))
        else:
          assert_never(item)
      message_param = chat.ChatCompletionAssistantMessageParam(role='assistant')
      if texts:
        # Note: model responses from this model should only have one text item, so the following
        # shouldn't merge multiple texts into one unless you switch models between runs:
        message_param['content'] = '\n\n'.join(texts)
      if tool_calls:
        message_param['tool_calls'] = tool_calls
      yield message_param
    else:
      assert_never(message)
  @staticmethod
  def_map_tool_call(t: ToolCallPart) -> chat.ChatCompletionMessageToolCallParam:
    return chat.ChatCompletionMessageToolCallParam(
      id=_guard_tool_call_id(t=t, model_source='Groq'),
      type='function',
      function={'name': t.tool_name, 'arguments': t.args_as_json_str()},
    )
  @staticmethod
  def_map_tool_definition(f: ToolDefinition) -> chat.ChatCompletionToolParam:
    return {
      'type': 'function',
      'function': {
        'name': f.name,
        'description': f.description,
        'parameters': f.parameters_json_schema,
      },
    }
  @classmethod
  def_map_user_message(cls, message: ModelRequest) -> Iterable[chat.ChatCompletionMessageParam]:
    for part in message.parts:
      if isinstance(part, SystemPromptPart):
        yield chat.ChatCompletionSystemMessageParam(role='system', content=part.content)
      elif isinstance(part, UserPromptPart):
        yield cls._map_user_prompt(part)
      elif isinstance(part, ToolReturnPart):
        yield chat.ChatCompletionToolMessageParam(
          role='tool',
          tool_call_id=_guard_tool_call_id(t=part, model_source='Groq'),
          content=part.model_response_str(),
        )
      elif isinstance(part, RetryPromptPart):
        if part.tool_name is None:
          yield chat.ChatCompletionUserMessageParam(role='user', content=part.model_response())
        else:
          yield chat.ChatCompletionToolMessageParam(
            role='tool',
            tool_call_id=_guard_tool_call_id(t=part, model_source='Groq'),
            content=part.model_response(),
          )
  @staticmethod
  def_map_user_prompt(part: UserPromptPart) -> chat.ChatCompletionUserMessageParam:
    content: str | list[chat.ChatCompletionContentPartParam]
    if isinstance(part.content, str):
      content = part.content
    else:
      content = []
      for item in part.content:
        if isinstance(item, str):
          content.append(chat.ChatCompletionContentPartTextParam(text=item, type='text'))
        elif isinstance(item, ImageUrl):
          image_url = ImageURL(url=item.url)
          content.append(chat.ChatCompletionContentPartImageParam(image_url=image_url, type='image_url'))
        elif isinstance(item, BinaryContent):
          base64_encoded = base64.b64encode(item.data).decode('utf-8')
          if item.is_image:
            image_url = ImageURL(url=f'data:{item.media_type};base64,{base64_encoded}')
            content.append(chat.ChatCompletionContentPartImageParam(image_url=image_url, type='image_url'))
          else:
            raise RuntimeError('Only images are supported for binary content in Groq.')
        elif isinstance(item, DocumentUrl): # pragma: no cover
          raise RuntimeError('DocumentUrl is not supported in Groq.')
        else: # pragma: no cover
          raise RuntimeError(f'Unsupported content type: {type(item)}')
    return chat.ChatCompletionUserMessageParam(role='user', content=content)

```
  
---|---  
####  __init__
```
__init__(
  model_name: GroqModelName[](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.GroqModelName "pydantic_ai.models.groq.GroqModelName"),
  *,
  provider: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")["groq"] | Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncGroq] = "groq"
) -> None

```

```
__init__(
  model_name: GroqModelName[](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.GroqModelName "pydantic_ai.models.groq.GroqModelName"),
  *,
  provider: None = None,
  api_key: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
  groq_client: AsyncGroq | None = None,
  http_client: AsyncClient | None = None
) -> None

```

```
__init__(
  model_name: GroqModelName[](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.GroqModelName "pydantic_ai.models.groq.GroqModelName"),
  *,
  provider: (
    Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")["groq"] | Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncGroq] | None
  ) = None,
  api_key: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
  groq_client: AsyncGroq | None = None,
  http_client: AsyncClient | None = None
)

```

Initialize a Groq model.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`model_name` |  `GroqModelName[](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.GroqModelName "pydantic_ai.models.groq.GroqModelName")` |  The name of the Groq model to use. List of model names available [here](https://console.groq.com/docs/models). |  _required_  
`provider` |  `Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['groq'] | Provider[](https://ai.pydantic.dev/api/providers/#pydantic_ai.providers.Provider "pydantic_ai.providers.Provider")[AsyncGroq] | None` |  The provider to use for authentication and API access. Can be either the string 'groq' or an instance of `Provider[AsyncGroq]`. If not provided, a new provider will be created using the other parameters. |  `None`  
`api_key` |  `str[](https://docs.python.org/3/library/stdtypes.html#str) | None` |  The API key to use for authentication, if not provided, the `GROQ_API_KEY` environment variable will be used if available. |  `None`  
`groq_client` |  `AsyncGroq | None` |  An existing [`AsyncGroq`](https://github.com/groq/groq-python?tab=readme-ov-file#async-usage) client to use, if provided, `api_key` and `http_client` must be `None`. |  `None`  
`http_client` |  `AsyncClient | None` |  An existing `httpx.AsyncClient` to use for making HTTP requests. |  `None`  
Source code in `pydantic_ai_slim/pydantic_ai/models/groq.py`
```
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
```
| ```
def__init__(
  self,
  model_name: GroqModelName,
  *,
  provider: Literal['groq'] | Provider[AsyncGroq] | None = None,
  api_key: str | None = None,
  groq_client: AsyncGroq | None = None,
  http_client: AsyncHTTPClient | None = None,
):
"""Initialize a Groq model.
  Args:
    model_name: The name of the Groq model to use. List of model names available
      [here](https://console.groq.com/docs/models).
    provider: The provider to use for authentication and API access. Can be either the string
      'groq' or an instance of `Provider[AsyncGroq]`. If not provided, a new provider will be
      created using the other parameters.
    api_key: The API key to use for authentication, if not provided, the `GROQ_API_KEY` environment variable
      will be used if available.
    groq_client: An existing
      [`AsyncGroq`](https://github.com/groq/groq-python?tab=readme-ov-file#async-usage)
      client to use, if provided, `api_key` and `http_client` must be `None`.
    http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.
  """
  self._model_name = model_name
  if provider is not None:
    if isinstance(provider, str):
      self.client = infer_provider(provider).client
    else:
      self.client = provider.client
  elif groq_client is not None:
    assert http_client is None, 'Cannot provide both `groq_client` and `http_client`'
    assert api_key is None, 'Cannot provide both `groq_client` and `api_key`'
    self.client = groq_client
  elif http_client is not None:
    self.client = AsyncGroq(api_key=api_key, http_client=http_client)
  else:
    self.client = AsyncGroq(api_key=api_key, http_client=cached_async_http_client())

```
  
---|---  
####  model_name `property`
```
model_name: GroqModelName[](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.GroqModelName "pydantic_ai.models.groq.GroqModelName")

```

The model name.
####  system `property`
```
system: str[](https://docs.python.org/3/library/stdtypes.html#str) | None

```

The system / model provider.
###  GroqStreamedResponse `dataclass`
Bases: `StreamedResponse[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.StreamedResponse "pydantic_ai.models.StreamedResponse")`
Implementation of `StreamedResponse` for Groq models.
Source code in `pydantic_ai_slim/pydantic_ai/models/groq.py`
```
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
```
| ```
@dataclass
classGroqStreamedResponse(StreamedResponse):
"""Implementation of `StreamedResponse` for Groq models."""
  _model_name: GroqModelName
  _response: AsyncIterable[chat.ChatCompletionChunk]
  _timestamp: datetime
  async def_get_event_iterator(self) -> AsyncIterator[ModelResponseStreamEvent]:
    async for chunk in self._response:
      self._usage += _map_usage(chunk)
      try:
        choice = chunk.choices[0]
      except IndexError:
        continue
      # Handle the text part of the response
      content = choice.delta.content
      if content is not None:
        yield self._parts_manager.handle_text_delta(vendor_part_id='content', content=content)
      # Handle the tool calls
      for dtc in choice.delta.tool_calls or []:
        maybe_event = self._parts_manager.handle_tool_call_delta(
          vendor_part_id=dtc.index,
          tool_name=dtc.function and dtc.function.name,
          args=dtc.function and dtc.function.arguments,
          tool_call_id=dtc.id,
        )
        if maybe_event is not None:
          yield maybe_event
  @property
  defmodel_name(self) -> GroqModelName:
"""Get the model name of the response."""
    return self._model_name
  @property
  deftimestamp(self) -> datetime:
"""Get the timestamp of the response."""
    return self._timestamp

```
  
---|---  
####  model_name `property`
```
model_name: GroqModelName[](https://ai.pydantic.dev/api/models/groq/#pydantic_ai.models.groq.GroqModelName "pydantic_ai.models.groq.GroqModelName")

```

Get the model name of the response.
####  timestamp `property`
```
timestamp: datetime[](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")

```

Get the timestamp of the response.
© Pydantic Services Inc. 2024 to present 
