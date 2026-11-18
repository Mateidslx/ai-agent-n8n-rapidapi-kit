#!/usr/bin/env python3
"""Quickstart client for the AI RAG, B2B Lead Enrichment, and Dev Utility RapidAPIs."""

import json
import os
import sys
import urllib.request

RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY", "").strip()
if not RAPIDAPI_KEY:
    print("Set RAPIDAPI_KEY environment variable first:")
    print("  export RAPIDAPI_KEY='your_rapidapi_key'")
    sys.exit(1)


def call_rapidapi(host: str, path: str, payload: dict) -> dict:
    url = f"https://{host}{path}"
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Content-Type": "application/json",
            "x-rapidapi-key": RAPIDAPI_KEY,
            "x-rapidapi-host": host,
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


if __name__ == "__main__":
    print("=== 1. AI Web Scraper & Markdown RAG ===")
    md = call_rapidapi(
        "ai-web-scraper-markdown-rag.p.rapidapi.com",
        "/v1/web/extract-markdown",
        {"url": "https://example.com", "include_links": True},
    )
    print(f"Title: {md.get('title')} | Words: {md.get('word_count')}")

    print("\n=== 2. B2B Domain & Lead Enrichment Engine ===")
    email_res = call_rapidapi(
        "b2b-domain-lead-enrichment-engine.p.rapidapi.com",
        "/v2/b2b/validate-email",
        {"email": "contact@stripe.com"},
    )
    print(
        f"Email: {email_res.get('email')} | MX: {email_res.get('has_mx_records')} | "
        f"Corporate B2B: {email_res.get('is_corporate_b2b')} | Score: {email_res.get('deliverability_score')}"
    )

    print("\n=== 3. Kai Developer Utility Suite ===")
    sec = call_rapidapi(
        "kai-developer-utility-suite1.p.rapidapi.com",
        "/v1/security/headers-audit",
        {"url": "https://example.com"},
    )
    print(f"Security Score: {sec.get('score_out_of_100')}/100 (Grade {sec.get('grade')})")
