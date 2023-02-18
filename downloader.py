"""
A rudimentary URL downloader (like wget or curl) to demonstrate Rich progress bars.
"""

import os.path
import sys
from concurrent.futures import ThreadPoolExecutor
import signal
from functools import partial
from threading import Event
from typing import Iterable
from urllib.request import urlopen
import requests

from rich.progress import (
    BarColumn,
    DownloadColumn,
    Progress,
    TaskID,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
)

progress = Progress(
    TextColumn("[bold blue]{task.fields[filename]}", justify="right"),
    BarColumn(bar_width=None),
    "[progress.percentage]{task.percentage:>3.1f}%",
    "•",
    DownloadColumn(),
    "•",
    TransferSpeedColumn(),
    "•",
    TimeRemainingColumn(),
)


done_event = Event()


def handle_sigint(signum, frame):
    done_event.set()


signal.signal(signal.SIGINT, handle_sigint)


def copy_url(task_id: TaskID, url: str, path: str) -> None:
    """Copy data from a url to a local file."""
    # response = urlopen(url)
    response=requests.get(url,stream=True)
    # This will break if the response doesn't contain content length
    progress.update(task_id, total=int(response.headers["Content-length"]))
    with open(path, "wb") as dest_file:
        progress.start_task(task_id)
        for data in response.iter_content(chunk_size = 1024):
            dest_file.write(data)
            progress.update(task_id, advance=len(data))
            if done_event.is_set():
                return



def download(urls: Iterable[str]):
    """Download multiple files to the given directory."""

    with progress:
        with ThreadPoolExecutor(max_workers=4) as pool:
            for i in range(0,len(urls),2):
                url=urls[i]
                if url=='':
                    print("无法下载:"+urls[i+1])
                    continue
                if 'http' in url:
                    filename = urls[i+1]
                    dest_path = filename
                    task_id = progress.add_task("download", filename=filename, start=False)
                    pool.submit(copy_url, task_id, url, dest_path)

# download(['http://music.163.com/song/media/outer/url?id=1971659843.mp3','2.mp3'])
# if __name__ == "__main__":
#     # Try with https://releases.ubuntu.com/20.04/ubuntu-20.04.3-desktop-amd64.iso
#     if sys.argv[1:]:
#         download(sys.argv[1:], "")
#     else:

#         print("Usage:\n\tpython downloader.py URL1 URL2 URL3 (etc)")
