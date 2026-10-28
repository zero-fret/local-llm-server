from llama_cpp.server.app import create_app
import os

os.environ["MODEL"] = str(__file__).replace("server.py", "Qwen3.5-4B.Q4_K_M.gguf")
os.environ["N_GPU_LAYERS"] = "-1"
os.environ["N_CTX"] = "65536"
os.environ["LOGITS_ALL"] = "False"
os.environ["N_MAX_TOKENS"] = "65536"
app = create_app()

print("URLs:")
for route in app.routes:
    print(f"  {route.methods} {route.path}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

    