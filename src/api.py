from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from .tests import AmazonBot

app = FastAPI(title="Amazon Bot API", version="0.1.0")

class RunBotRequest(BaseModel):
    email: str
    password: str
    mode: str = "headless"  # "headless" o "headed"

async def run_bot_script(email: str, password: str, mode: str):
    headless = True if mode.lower() == "headless" else False
    bot = AmazonBot(email=email, password=password, headless=headless)
    await bot.run_test()

@app.post("/run-bot")
async def run_bot(request: RunBotRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(run_bot_script, request.email, request.password, request.mode)
    return {"status": "success", "message": "Bot started in background."}
