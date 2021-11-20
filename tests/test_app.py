import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))

from app.app import index, print_ip

def test_index():
    assert index() == "Hello, world!"


def test_print_ip():
    assert print_ip() == "172.17.0.2" or "10.1.0.10"