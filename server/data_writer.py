from datetime import datetime, timedelta
from pathlib import Path
import atexit

_files = {}

@atexit.register
def _cleanup():
    for key in _files.keys():
        for file in _files[key].values():
            file.close()

def write(uid: str, data: str) -> None:
    now = datetime.now()
    date = now.strftime('%Y-%m-%d')
    time = now.strftime('%H:%M:%S')
    if _files.get(date) is None:
        Path(f'data/{date}').mkdir(parents=True, exist_ok=True)
        _files[date] = {}
        yesterday = (now - timedelta(days=1)).strftime('%Y-%m-%d')
        if _files.get(yesterday) is not None:
            for file in _files[yesterday].values():
                file.close()
            del _files[yesterday]
    if _files[date].get(uid) is None:
        _files[date][uid] = open(f'data/{date}/{uid}.csv', 'a', buffering=1)
    _files[date][uid].write(f'{time},{data}\n')
