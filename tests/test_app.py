import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))

from app.app import index

def test_index():
    assert index() == "Hello world!"
