import asyncio
from browser_use_sdk import AsyncBrowserUse
from pydantic import BaseModel

class Post(BaseModel):
    title: str
    url: str
    points: int

class PostList(BaseModel):
    items: list[Post]

async def main():
    client = AsyncBrowserUse()
    result = await client.run(
        "Get the top 3 posts from Hacker News",
        output_schema=PostList,
    )
    for post in result.output.items:
        print(f"{post.title} ({post.points} pts)")

asyncio.run(main())
