from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tests import AmazonBot

app = FastAPI(title="Amazon Bot API")


class LoginRequest(BaseModel):
    email: str
    password: str
    mode: str = "headless"  # "headless" o "headed"


@app.post("/run-bot")
async def run_bot(request: LoginRequest):
    if request.mode not in ["headless", "headed"]:
        raise HTTPException(status_code=400, detail="Mode must be 'headless' or 'headed'")

    headless = request.mode == "headless"
    bot = AmazonBot(email=request.email, password=request.password, headless=headless)

    try:
        await bot.run_test()
        return {"status": "success", "message": "Bot finished execution"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
