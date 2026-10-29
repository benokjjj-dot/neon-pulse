#!/usr/bin/env python3
"""Neon Pulse — монитор публичных API."""

import json
import time
import urllib.request

ENDPOINTS = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/users/1",
]


def check(endpoint):
    start = time.time()
    try:
        with urllib.request.urlopen(endpoint, timeout=10) as r:
            code = r.status
        return {"endpoint": endpoint, "status": code, "ms": round((time.time() - start) * 1000, 2)}
    except Exception as e:
        return {"endpoint": endpoint, "status": str(e), "ms": round((time.time() - start) * 1000, 2)}


def main():
    report = [check(e) for e in ENDPOINTS]
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
