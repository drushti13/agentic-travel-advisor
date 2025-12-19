import json
import hashlib
from pathlib import Path

CACHE_FILE = Path("llm_cache.json")


def _load_cache() -> dict:
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def _save_cache(cache: dict) -> None:
    CACHE_FILE.write_text(
        json.dumps(cache, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def make_key(prompt: str) -> str:
    return hashlib.sha256(prompt.encode("utf-8")).hexdigest()


def get(prompt: str) -> str | None:
    cache = _load_cache()
    key = make_key(prompt)
    return cache.get(key)


def set(prompt: str, response: str) -> None:
    cache = _load_cache()
    key = make_key(prompt)
    cache[key] = response
    _save_cache(cache)
