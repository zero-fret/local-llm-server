# Local LLM Server

A lightweight OpenAI-compatible local LLM server built on [llama.cpp](https://github.com/ggml-org/llama.cpp) with a simple streaming CLI client.

## Features

- OpenAI-compatible `/v1/chat/completions` endpoint
- Streaming responses
- GPU acceleration (offloads all layers to GPU)
- 64K context window
- Zero config — just drop your `.gguf` model next to `server.py`

## Quick Start

### 1. Install dependencies

```bash
pip install llama-cpp-python[server] openai uvicorn
```

### 2. Download a model

Place a GGUF model file next to `server.py`. By default it expects:

```
Qwen3.5-4B.Q4_K_M.gguf
```

You can also edit the `MODEL` path in `server.py` to point to any local `.gguf` file.

### 3. Start the server

```bash
python server.py
```

The server listens on `http://0.0.0.0:8000`. Available routes are printed on startup.

### 4. Chat from the client

```bash
python client.py
```

Type your message and press Enter. The response streams token by token. Type `exit` or `quit` to leave.

## Configuration

Edit `server.py` to tweak:

| Env var | Default | Description |
|---|---|---|
| `MODEL` | `Qwen3.5-4B.Q4_K_M.gguf` | Path to GGUF model |
| `N_GPU_LAYERS` | `-1` | Layers to offload to GPU (`-1` = all) |
| `N_CTX` | `65536` | Context window size |
| `N_MAX_TOKENS` | `65536` | Max output tokens |
| `LOGITS_ALL` | `False` | Return logits for every token |

## API Usage

Because the server is OpenAI-compatible, you can use any OpenAI SDK:

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="1337")

resp = client.chat.completions.create(
    model="any",
    messages=[{"role": "user", "content": "Hello!"}],
    stream=True,
)
for chunk in resp:
    print(chunk.choices[0].delta.content or "", end="")
```

## Files

- `server.py` — starts the llama.cpp OpenAI-compatible server
- `client.py` — interactive streaming chat client
- `randomstring.py` — utility to generate a random API key
