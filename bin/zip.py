from zipfile import ZipFile


async def zipped(file):
    zipObject = ZipFile(file)
