import asyncio

async def download_chunk(fileSize, chunkSize):

    byteDownloaded = 0

    while byteDownloaded < fileSize :
        await asyncio.sleep(0.5)

        byteDownloaded = byteDownloaded + chunkSize

        yield f"Byte Downloaded {byteDownloaded}"


async def main():
    print("starting download")

    async for chunk in download_chunk(5000,500):
        print(chunk)
    
    print("download complete")

asyncio.run(main())

