---
url: https://ai.pydantic.dev/examples/question-graph/
session_id: pydantic_ai_docs
updated_dt: 2025-03-14T09:20:55.940750
---
[ Skip to content ](https://ai.pydantic.dev/examples/question-graph/#question-graph)
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI")
PydanticAI 
Question Graph 
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
    * Question Graph  [ Question Graph  ](https://ai.pydantic.dev/examples/question-graph/) Table of contents 
      * [ Running the Example  ](https://ai.pydantic.dev/examples/question-graph/#running-the-example)
      * [ Example Code  ](https://ai.pydantic.dev/examples/question-graph/#example-code)
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
    * [ pydantic_graph.state  ](https://ai.pydantic.dev/api/pydantic_graph/state/)
    * [ pydantic_graph.mermaid  ](https://ai.pydantic.dev/api/pydantic_graph/mermaid/)
    * [ pydantic_graph.exceptions  ](https://ai.pydantic.dev/api/pydantic_graph/exceptions/)


Table of contents 
  * [ Running the Example  ](https://ai.pydantic.dev/examples/question-graph/#running-the-example)
  * [ Example Code  ](https://ai.pydantic.dev/examples/question-graph/#example-code)


# Question Graph
Example of a graph for asking and evaluating questions.
Demonstrates:
  * [`pydantic_graph`](https://ai.pydantic.dev/graph/)


## Running the Example
With [dependencies installed and environment variables set](https://ai.pydantic.dev/examples/#usage), run:
[pip](https://ai.pydantic.dev/examples/question-graph/#__tabbed_1_1)[uv](https://ai.pydantic.dev/examples/question-graph/#__tabbed_1_2)
```
python-mpydantic_ai_examples.question_graph

```

```
uvrun-mpydantic_ai_examples.question_graph

```

## Example Code
question_graph.py```
from__future__import annotations as _annotations
fromdataclassesimport dataclass, field
frompathlibimport Path
fromtypingimport Annotated
importlogfire
fromdevtoolsimport debug
frompydantic_graphimport BaseNode, Edge, End, Graph, GraphRunContext, HistoryStep
frompydantic_aiimport Agent
frompydantic_ai.format_as_xmlimport format_as_xml
frompydantic_ai.messagesimport ModelMessage
# 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured
logfire.configure(send_to_logfire='if-token-present')
ask_agent = Agent('openai:gpt-4o', result_type=str, instrument=True)

@dataclass
classQuestionState:
  question: str | None = None
  ask_agent_messages: list[ModelMessage] = field(default_factory=list)
  evaluate_agent_messages: list[ModelMessage] = field(default_factory=list)

@dataclass
classAsk(BaseNode[QuestionState]):
  async defrun(self, ctx: GraphRunContext[QuestionState]) -> Answer:
    result = await ask_agent.run(
      'Ask a simple question with a single correct answer.',
      message_history=ctx.state.ask_agent_messages,
    )
    ctx.state.ask_agent_messages += result.all_messages()
    ctx.state.question = result.data
    return Answer()

@dataclass
classAnswer(BaseNode[QuestionState]):
  answer: str | None = None
  async defrun(self, ctx: GraphRunContext[QuestionState]) -> Evaluate:
    assert self.answer is not None
    return Evaluate(self.answer)

@dataclass
classEvaluationResult:
  correct: bool
  comment: str

evaluate_agent = Agent(
  'openai:gpt-4o',
  result_type=EvaluationResult,
  system_prompt='Given a question and answer, evaluate if the answer is correct.',
)

@dataclass
classEvaluate(BaseNode[QuestionState]):
  answer: str
  async defrun(
    self,
    ctx: GraphRunContext[QuestionState],
  ) -> Congratulate | Reprimand:
    assert ctx.state.question is not None
    result = await evaluate_agent.run(
      format_as_xml({'question': ctx.state.question, 'answer': self.answer}),
      message_history=ctx.state.evaluate_agent_messages,
    )
    ctx.state.evaluate_agent_messages += result.all_messages()
    if result.data.correct:
      return Congratulate(result.data.comment)
    else:
      return Reprimand(result.data.comment)

@dataclass
classCongratulate(BaseNode[QuestionState, None, None]):
  comment: str
  async defrun(
    self, ctx: GraphRunContext[QuestionState]
  ) -> Annotated[End, Edge(label='success')]:
    print(f'Correct answer! {self.comment}')
    return End(None)

@dataclass
classReprimand(BaseNode[QuestionState]):
  comment: str
  async defrun(self, ctx: GraphRunContext[QuestionState]) -> Ask:
    print(f'Comment: {self.comment}')
    # > Comment: Vichy is no longer the capital of France.
    ctx.state.question = None
    return Ask()

question_graph = Graph(
  nodes=(Ask, Answer, Evaluate, Congratulate, Reprimand), state_type=QuestionState
)

async defrun_as_continuous():
  state = QuestionState()
  node = Ask()
  history: list[HistoryStep[QuestionState, None]] = []
  with logfire.span('run questions graph'):
    while True:
      node = await question_graph.next(node, history, state=state)
      if isinstance(node, End):
        debug([e.data_snapshot() for e in history])
        break
      elif isinstance(node, Answer):
        assert state.question
        node.answer = input(f'{state.question} ')
      # otherwise just continue

async defrun_as_cli(answer: str | None):
  history_file = Path('question_graph_history.json')
  history = (
    question_graph.load_history(history_file.read_bytes())
    if history_file.exists()
    else []
  )
  if history:
    last = history[-1]
    assert last.kind == 'node', 'expected last step to be a node'
    state = last.state
    assert answer is not None, 'answer is required to continue from history'
    node = Answer(answer)
  else:
    state = QuestionState()
    node = Ask()
  debug(state, node)
  with logfire.span('run questions graph'):
    while True:
      node = await question_graph.next(node, history, state=state)
      if isinstance(node, End):
        debug([e.data_snapshot() for e in history])
        print('Finished!')
        break
      elif isinstance(node, Answer):
        print(state.question)
        break
      # otherwise just continue
  history_file.write_bytes(question_graph.dump_history(history, indent=2))

if __name__ == '__main__':
  importasyncio
  importsys
  try:
    sub_command = sys.argv[1]
    assert sub_command in ('continuous', 'cli', 'mermaid')
  except (IndexError, AssertionError):
    print(
      'Usage:\n'
      ' uv run -m pydantic_ai_examples.question_graph mermaid\n'
      'or:\n'
      ' uv run -m pydantic_ai_examples.question_graph continuous\n'
      'or:\n'
      ' uv run -m pydantic_ai_examples.question_graph cli [answer]',
      file=sys.stderr,
    )
    sys.exit(1)
  if sub_command == 'mermaid':
    print(question_graph.mermaid_code(start_node=Ask))
  elif sub_command == 'continuous':
    asyncio.run(run_as_continuous())
  else:
    a = sys.argv[2] if len(sys.argv) > 2 else None
    asyncio.run(run_as_cli(a))

```

The mermaid diagram generated in this example looks like this:
```
---
title: question_graph
---
stateDiagram-v2
 [*] --> Ask
 Ask --> Answer: ask the question
 Answer --> Evaluate: answer the question
 Evaluate --> Congratulate
 Evaluate --> Castigate
 Congratulate --> [*]: success
 Castigate --> Ask: try again
```

© Pydantic Services Inc. 2024 to present 
