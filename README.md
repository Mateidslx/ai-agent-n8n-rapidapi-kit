# AI Agent & n8n Utility Kit (RAG, Web-to-Markdown, B2B Lead Enrichment & Audits)

Ready-to-import **n8n workflows**, **Python clients**, and **LLM function-calling tool schemas** powered by fast, zero-setup REST APIs on RapidAPI (with free tiers to start testing immediately).

---

## Included APIs (All Live with Free Tiers)

| API | Best For | Endpoints | Free Tier | Link |
| :--- | :--- | :---: | :---: | :--- |
| **AI Web Scraper & Markdown RAG** | Converting web pages, RSS feeds & sitemaps into clean LLM-ready Markdown, JSON-LD & RAG chunks | 5 | 100 req/mo | [Open on RapidAPI](https://rapidapi.com/MateiDeSaintLeger/api/ai-web-scraper-markdown-rag) |
| **B2B Domain & Lead Enrichment Engine** | Validating work emails (MX, disposable, B2B), extracting company contacts/tech stack, DNS/SPF/DMARC/SSL & SEO audits | 4 | 50 req/mo | [Open on RapidAPI](https://rapidapi.com/MateiDeSaintLeger/api/b2b-domain-lead-enrichment-engine) |
| **Kai Developer Utility Suite** | All-in-one WCAG accessibility audit, HTTP security headers, secret leak scanner, SEO, video metadata & transcript cleanser | 10 | 100 req/mo | [Open on RapidAPI](https://rapidapi.com/MateiDeSaintLeger/api/kai-developer-utility-suite1) |

---

## Quick Start in n8n (2 Minutes)

1. Subscribe to the free **BASIC** tier on the API(s) you want above and copy your `X-RapidAPI-Key`.
2. Download one of the ready-to-use workflows from [`n8n/`](./n8n):
   - [`n8n/ai-rag-web-research-workflow.json`](./n8n/ai-rag-web-research-workflow.json) — Scrape any webpage to clean Markdown and chunk it for vector databases (Pinecone / Qdrant / Supabase).
   - [`n8n/b2b-lead-enrichment-audit-workflow.json`](./n8n/b2b-lead-enrichment-audit-workflow.json) — Validate a B2B email (MX + disposable check), enrich the company domain (emails, socials, tech stack), and audit DNS/SPF/DMARC + SSL.
3. In **n8n**, click **Import from File** (or paste the JSON).
4. Replace `YOUR_RAPIDAPI_KEY` in the HTTP Request node headers with your key and click **Test Workflow**.

---

## Quick Start in Python

```bash
export RAPIDAPI_KEY="your_rapidapi_key_here"
python examples/python_quickstart.py
```

Or copy a single call directly:

```python
import os, requests

RAPIDAPI_KEY = os.environ["RAPIDAPI_KEY"]

# 1. Turn any webpage into clean LLM-ready Markdown
resp = requests.post(
    "https://ai-web-scraper-markdown-rag.p.rapidapi.com/v1/web/extract-markdown",
    headers={
        "Content-Type": "application/json",
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "ai-web-scraper-markdown-rag.p.rapidapi.com",
    },
    json={"url": "https://example.com", "include_links": True},
    timeout=15,
)
print(resp.json()["markdown"])
```

---

## Quick Start with cURL

### 1. Web to LLM Markdown (`AI Web Scraper & Markdown RAG`)
```bash
curl -X POST "https://ai-web-scraper-markdown-rag.p.rapidapi.com/v1/web/extract-markdown" \
  -H "Content-Type: application/json" \
  -H "x-rapidapi-key: YOUR_RAPIDAPI_KEY" \
  -H "x-rapidapi-host: ai-web-scraper-markdown-rag.p.rapidapi.com" \
  -d '{"url": "https://example.com", "include_links": true}'
```

### 2. Validate Work Email & MX Check (`B2B Domain & Lead Enrichment Engine`)
```bash
curl -X POST "https://b2b-domain-lead-enrichment-engine.p.rapidapi.com/v2/b2b/validate-email" \
  -H "Content-Type: application/json" \
  -H "x-rapidapi-key: YOUR_RAPIDAPI_KEY" \
  -H "x-rapidapi-host: b2b-domain-lead-enrichment-engine.p.rapidapi.com" \
  -d '{"email": "contact@stripe.com"}'
```

### 3. Scan Code/Logs for Leaked Secrets (`Kai Developer Utility Suite`)
```bash
curl -X POST "https://kai-developer-utility-suite1.p.rapidapi.com/v1/security/secret-scan" \
  -H "Content-Type: application/json" \
  -H "x-rapidapi-key: YOUR_RAPIDAPI_KEY" \
  -H "x-rapidapi-host: kai-developer-utility-suite1.p.rapidapi.com" \
  -d '{"content": "AWS_KEY=AKIAIOSFODNN7EXAMPLE"}'
```

---

## LLM Function-Calling / AI Agent Tools

See [`examples/openai_tools_schema.json`](./examples/openai_tools_schema.json) for drop-in JSON tool definitions compatible with OpenAI, Anthropic, LangChain, CrewAI, and n8n AI Agent nodes.

## License

MIT — free to use in commercial and personal automations.
