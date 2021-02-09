import requests
import os


def downloader(url, file, attempt=1):
    """Wrap for multiple attempts"""

    while attempt:
        if resume_download(url, file):
            return True
        attempt -= 1
    return False


def resume_download(url, file):
    """ Use for downloading large files or with a bad connection.
    URL: some url
    FILE: file save path
    """

    resume_header = None
    size_offline = 0

    if os.path.exists(file):
        size_offline = os.path.getsize(file)
        resume_header = {'Range': f'bytes={size_offline}-'}

    r = requests.head(url)
    size_online = int(r.headers.get('content-length', 0))

    if size_offline < size_online:
        r = requests.get(url, stream=True, headers=resume_header)
        mode = 'ab' if size_offline else 'wb'
        with open(file, mode) as f:
            for chunk in r.iter_content(1024 * 32):
                f.write(chunk)

    if os.path.getsize(file) == size_online:
        return True

    return False
