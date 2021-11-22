import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))

from app.app import index, print_ip

def test_index():
    assert index() == "Hello world!"
