---
url: https://ai.pydantic.dev/api/pydantic_graph/state/
session_id: pydantic_ai_docs
updated_dt: 2025-03-14T09:20:52.038088
---
[ Skip to content ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graphstate)
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI")
PydanticAI 
pydantic_graph.state 
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
    * [ pydantic_ai.models.groq  ](https://ai.pydantic.dev/api/models/groq/)
    * [ pydantic_ai.models.mistral  ](https://ai.pydantic.dev/api/models/mistral/)
    * [ pydantic_ai.models.test  ](https://ai.pydantic.dev/api/models/test/)
    * [ pydantic_ai.models.function  ](https://ai.pydantic.dev/api/models/function/)
    * [ pydantic_ai.models.fallback  ](https://ai.pydantic.dev/api/models/fallback/)
    * [ pydantic_ai.providers  ](https://ai.pydantic.dev/api/providers/)
    * [ pydantic_graph  ](https://ai.pydantic.dev/api/pydantic_graph/graph/)
    * [ pydantic_graph.nodes  ](https://ai.pydantic.dev/api/pydantic_graph/nodes/)
    * pydantic_graph.state  [ pydantic_graph.state  ](https://ai.pydantic.dev/api/pydantic_graph/state/) Table of contents 
      * [ state  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state)
      * [ StateT  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.StateT)
      * [ deep_copy_state  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.deep_copy_state)
      * [ NodeStep  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.NodeStep)
        * [ state  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.NodeStep.state)
        * [ node  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.NodeStep.node)
        * [ start_ts  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.NodeStep.start_ts)
        * [ duration  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.NodeStep.duration)
        * [ kind  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.NodeStep.kind)
        * [ snapshot_state  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.NodeStep.snapshot_state)
        * [ data_snapshot  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.NodeStep.data_snapshot)
      * [ EndStep  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.EndStep)
        * [ result  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.EndStep.result)
        * [ ts  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.EndStep.ts)
        * [ kind  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.EndStep.kind)
        * [ data_snapshot  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.EndStep.data_snapshot)
      * [ HistoryStep  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.HistoryStep)
    * [ pydantic_graph.mermaid  ](https://ai.pydantic.dev/api/pydantic_graph/mermaid/)
    * [ pydantic_graph.exceptions  ](https://ai.pydantic.dev/api/pydantic_graph/exceptions/)


Table of contents 
  * [ state  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state)
  * [ StateT  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.StateT)
  * [ deep_copy_state  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.deep_copy_state)
  * [ NodeStep  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.NodeStep)
    * [ state  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.NodeStep.state)
    * [ node  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.NodeStep.node)
    * [ start_ts  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.NodeStep.start_ts)
    * [ duration  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.NodeStep.duration)
    * [ kind  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.NodeStep.kind)
    * [ snapshot_state  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.NodeStep.snapshot_state)
    * [ data_snapshot  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.NodeStep.data_snapshot)
  * [ EndStep  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.EndStep)
    * [ result  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.EndStep.result)
    * [ ts  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.EndStep.ts)
    * [ kind  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.EndStep.kind)
    * [ data_snapshot  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.EndStep.data_snapshot)
  * [ HistoryStep  ](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.HistoryStep)


# `pydantic_graph.state`
###  StateT `module-attribute`
```
StateT = TypeVar('StateT', default=None)

```

Type variable for the state in a graph.
###  deep_copy_state
```
deep_copy_state(state: StateT[](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.StateT "pydantic_graph.state.StateT")) -> StateT[](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.StateT "pydantic_graph.state.StateT")

```

Default method for snapshotting the state in a graph run, uses [`copy.deepcopy`](https://docs.python.org/3/library/copy.html#copy.deepcopy).
Source code in `pydantic_graph/pydantic_graph/state.py`
```
24
25
26
27
28
29
```
| ```
defdeep_copy_state(state: StateT) -> StateT:
"""Default method for snapshotting the state in a graph run, uses [`copy.deepcopy`][copy.deepcopy]."""
  if state is None:
    return state
  else:
    return copy.deepcopy(state)

```
  
---|---  
###  NodeStep `dataclass`
Bases: `Generic[](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.StateT "pydantic_graph.state.StateT"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "pydantic_graph.nodes.RunEndT")]`
History step describing the execution of a node in a graph.
Source code in `pydantic_graph/pydantic_graph/state.py`
```
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
```
| ```
@dataclass
classNodeStep(Generic[StateT, RunEndT]):
"""History step describing the execution of a node in a graph."""
  state: StateT
"""The state of the graph after the node has been run."""
  node: Annotated[BaseNode[StateT, Any, RunEndT], CustomNodeSchema()]
"""The node that was run."""
  start_ts: datetime = field(default_factory=_utils.now_utc)
"""The timestamp when the node started running."""
  duration: float | None = None
"""The duration of the node run in seconds."""
  kind: Literal['node'] = 'node'
"""The kind of history step, can be used as a discriminator when deserializing history."""
  # TODO waiting for https://github.com/pydantic/pydantic/issues/11264, should be an InitVar
  snapshot_state: Annotated[Callable[[StateT], StateT], pydantic.Field(exclude=True, repr=False)] = field(
    default=deep_copy_state, repr=False
  )
"""Function to snapshot the state of the graph."""
  def__post_init__(self):
    # Copy the state to prevent it from being modified by other code
    self.state = self.snapshot_state(self.state)
  defdata_snapshot(self) -> BaseNode[StateT, Any, RunEndT]:
"""Returns a deep copy of [`self.node`][pydantic_graph.state.NodeStep.node].
    Useful for summarizing history.
    """
    return copy.deepcopy(self.node)

```
  
---|---  
####  state `instance-attribute`
```
state: StateT[](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.StateT "pydantic_graph.state.StateT")

```

The state of the graph after the node has been run.
####  node `instance-attribute`
```
node: Annotated[](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated")[
  BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "pydantic_graph.nodes.BaseNode")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.StateT "pydantic_graph.state.StateT"), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "pydantic_graph.nodes.RunEndT")], CustomNodeSchema()
]

```

The node that was run.
####  start_ts `class-attribute` `instance-attribute`
```
start_ts: datetime[](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") = field[](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field")(default_factory=now_utc)

```

The timestamp when the node started running.
####  duration `class-attribute` `instance-attribute`
```
duration: float[](https://docs.python.org/3/library/functions.html#float) | None = None

```

The duration of the node run in seconds.
####  kind `class-attribute` `instance-attribute`
```
kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['node'] = 'node'

```

The kind of history step, can be used as a discriminator when deserializing history.
####  snapshot_state `class-attribute` `instance-attribute`
```
snapshot_state: Annotated[](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated")[
  Callable[](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable")[[StateT[](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.StateT "pydantic_graph.state.StateT")], StateT[](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.StateT "pydantic_graph.state.StateT")],
  Field[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "pydantic.Field")(exclude=True, repr=False),
] = field[](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field")(default=deep_copy_state[](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.deep_copy_state "pydantic_graph.state.deep_copy_state"), repr=False)

```

Function to snapshot the state of the graph.
####  data_snapshot
```
data_snapshot() -> BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "pydantic_graph.nodes.BaseNode")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.StateT "pydantic_graph.state.StateT"), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "pydantic_graph.nodes.RunEndT")]

```

Returns a deep copy of [`self.node`](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.NodeStep.node).
Useful for summarizing history.
Source code in `pydantic_graph/pydantic_graph/state.py`
```
56
57
58
59
60
61
```
| ```
defdata_snapshot(self) -> BaseNode[StateT, Any, RunEndT]:
"""Returns a deep copy of [`self.node`][pydantic_graph.state.NodeStep.node].
  Useful for summarizing history.
  """
  return copy.deepcopy(self.node)

```
  
---|---  
###  EndStep `dataclass`
Bases: `Generic[](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "pydantic_graph.nodes.RunEndT")]`
History step describing the end of a graph run.
Source code in `pydantic_graph/pydantic_graph/state.py`
```
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
```
| ```
@dataclass
classEndStep(Generic[RunEndT]):
"""History step describing the end of a graph run."""
  result: End[RunEndT]
"""The result of the graph run."""
  ts: datetime = field(default_factory=_utils.now_utc)
"""The timestamp when the graph run ended."""
  kind: Literal['end'] = 'end'
"""The kind of history step, can be used as a discriminator when deserializing history."""
  defdata_snapshot(self) -> End[RunEndT]:
"""Returns a deep copy of [`self.result`][pydantic_graph.state.EndStep.result].
    Useful for summarizing history.
    """
    return copy.deepcopy(self.result)

```
  
---|---  
####  result `instance-attribute`
```
result: End[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "pydantic_graph.nodes.End")[RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "pydantic_graph.nodes.RunEndT")]

```

The result of the graph run.
####  ts `class-attribute` `instance-attribute`
```
ts: datetime[](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") = field[](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field")(default_factory=now_utc)

```

The timestamp when the graph run ended.
####  kind `class-attribute` `instance-attribute`
```
kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['end'] = 'end'

```

The kind of history step, can be used as a discriminator when deserializing history.
####  data_snapshot
```
data_snapshot() -> End[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "pydantic_graph.nodes.End")[RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "pydantic_graph.nodes.RunEndT")]

```

Returns a deep copy of [`self.result`](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.EndStep.result).
Useful for summarizing history.
Source code in `pydantic_graph/pydantic_graph/state.py`
```
75
76
77
78
79
80
```
| ```
defdata_snapshot(self) -> End[RunEndT]:
"""Returns a deep copy of [`self.result`][pydantic_graph.state.EndStep.result].
  Useful for summarizing history.
  """
  return copy.deepcopy(self.result)

```
  
---|---  
###  HistoryStep `module-attribute`
```
HistoryStep = Union[](https://docs.python.org/3/library/typing.html#typing.Union "typing.Union")[
  NodeStep[](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.NodeStep "pydantic_graph.state.NodeStep")[StateT[](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.StateT "pydantic_graph.state.StateT"), RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "pydantic_graph.nodes.RunEndT")], EndStep[](https://ai.pydantic.dev/api/pydantic_graph/state/#pydantic_graph.state.EndStep "pydantic_graph.state.EndStep")[RunEndT[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.RunEndT "pydantic_graph.nodes.RunEndT")]
]

```

A step in the history of a graph run.
[`Graph.run`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph.run) returns a list of these steps describing the execution of the graph, together with the run return value.
© Pydantic Services Inc. 2024 to present 
