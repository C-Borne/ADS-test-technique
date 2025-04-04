"""Asynchronous."""

import asyncio
from pathlib import Path

import aiofiles


async def read_file(path: Path) -> str:
    """Read the content of a file."""
    async with aiofiles.open(path) as f:
        content = await f.read()
    print(f"Content of {path} successfully read.")
    return content


async def main():
    """Do stuff."""
    tasks = [
        read_file(Path("resources/file_1")),
        read_file(Path("resources/file_2")),
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    # Explain the code above.
    # Which file will be read first ?
    # What does it depend on ?
    asyncio.run(main())
