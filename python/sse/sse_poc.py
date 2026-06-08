"""
Standard SSE (Server-Sent Events) POC.
Demonstrates industry-standard SSE implementation using FastAPI.
"""

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import asyncio

app = FastAPI()

# Add CORS middleware to allow connections from any origin (including file://)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def token_generator():
    """
    Simulates a stream of incoming data tokens.
    Uses standard SSE format with 'data:' prefix and double newlines.
    """
    for i in range(1, 6):
        await asyncio.sleep(1)  # Simulate processing time
        yield f"data: Token {i} processed successfully\n\n"


@app.get("/stream-events")
async def stream_events():
    """
    SSE endpoint that streams tokens in standard SSE format.
    Media type: text/event-stream (industry standard for SSE)
    """
    return StreamingResponse(
        token_generator(),
        media_type="text/event-stream"
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "sse_poc:app",
        host="0.0.0.0",
        port=8001,
        reload=True,
        log_level="info"
    )
