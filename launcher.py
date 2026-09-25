import marshal
import sys
import zlib
from pathlib import Path

def resource_path(name: str) -> Path:
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    return base / name

payload = resource_path("app_payload.bin").read_bytes()
code = marshal.loads(zlib.decompress(payload))
namespace = {
    "__name__": "__main__",
    "__file__": str(Path(sys.executable).resolve().parent / "christmas_player_1000.py"),
    "__package__": None,
}
exec(code, namespace, namespace)
