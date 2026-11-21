# AI Agent & n8n Utility Kit (RAG, Web-to-Markdown, B2B Lead Enrichment & Audits)

Ready-to-import **n8n workflows**, **Python clients**, and **LLM function-calling tool schemas** powered by fast, zero-setup REST APIs on RapidAPI (with free tiers to start testing immediately).

---

## Included APIs (All 11 Live with Free Tiers & Pay-Per-Use)

| API | Best For | Endpoints | Free Tier | Link |
| :--- | :--- | :---: | :---: | :--- |
| **AI Web Scraper & Markdown RAG** | Converting web pages, RSS feeds & sitemaps into clean LLM-ready Markdown, JSON-LD & RAG chunks | 5 | 100 req/mo | [Open on RapidAPI](https://rapidapi.com/MateiDeSaintLeger/api/ai-web-scraper-markdown-rag) |
| **B2B Domain & Lead Enrichment Engine** | Validating work emails (MX, disposable, B2B), extracting company contacts/tech stack, DNS/SPF/DMARC/SSL & SEO audits | 4 | 50 req/mo | [Open on RapidAPI](https://rapidapi.com/MateiDeSaintLeger/api/b2b-domain-lead-enrichment-engine) |
| **Custom QR Code Generator & Barcode Studio** | Generating custom-styled QR codes (PNG, SVG, WiFi login, vCard) with custom colors & sizing | 3 | 100 req/mo | [Open on RapidAPI](https://rapidapi.com/MateiDeSaintLeger/api/custom-qr-code-generator-barcode-studio) |
| **LLM JSON Repair Schema & Patch Studio** | Repairing broken LLM JSON (markdown fences, trailing commas, single quotes), JSON Schema validation, RFC 6902 diff/patch & CSV flattening | 3 | 100 req/mo | [Open on RapidAPI](https://rapidapi.com/MateiDeSaintLeger/api/llm-json-repair-schema-patch-studio) |
| **AI Prompt PII Redaction & GDPR Sanitizer** | Reversible PII redaction before LLM calls (`<EMAIL_1>`, `<IBAN_1>`), response rehydration & IBAN/Luhn/SIREN/SIRET/NIR validation | 3 | 100 req/mo | [Open on RapidAPI](https://rapidapi.com/MateiDeSaintLeger/api/ai-prompt-pii-redaction-gdpr-sanitizer) |
| **Deterministic PDF Table & CSV Extractor** | Zero-token-waste extraction from messy CSVs (auto-delimiter/BOM), HTML tables (`colspan`-aware) & Base64 PDFs | 3 | 100 req/mo | [Open on RapidAPI](https://rapidapi.com/MateiDeSaintLeger/api/deterministic-pdf-table-csv-extractor) |
| **Deterministic Invoice Math Cron & SLA Verifier** | Zero-hallucination `Decimal` invoice/VAT/discount math, holiday-aware business-day SLA deadlines, timezone Cron & unit conversions | 4 | 100 req/mo | [Open on RapidAPI](https://rapidapi.com/MateiDeSaintLeger/api/deterministic-invoice-math-cron-sla-verifier) |
| **SQL Security Guard & Dialect Transpiler** | Read-only SQL safety & injection auditing for Text-to-SQL AI agents, dialect transpilation (Postgres/MySQL/SQLite/BigQuery) & metadata extraction | 3 | 100 req/mo | [Open on RapidAPI](https://rapidapi.com/MateiDeSaintLeger/api/sql-security-guard-dialect-transpiler) |
| **LLM Prompt Injection Firewall & Token Cost Optimizer** | Detecting & stripping prompt injection/jailbreak attacks, multi-model token/USD cost estimation & RAG context compression | 3 | 100 req/mo | [Open on RapidAPI](https://rapidapi.com/MateiDeSaintLeger/api/llm-prompt-injection-firewall-token-cost-optimizer) |
| **Pure SVG Telemetry Charts Sparklines & Status Badges** | Generating zero-JS SVG status badges, area trend sparklines & telemetry bar charts for READMEs, emails & dashboards | 3 | 100 req/mo | [Open on RapidAPI](https://rapidapi.com/MateiDeSaintLeger/api/pure-svg-telemetry-charts-sparklines-status-badges) |
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
