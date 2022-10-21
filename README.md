Simple wrapper for [pytrends](https://github.com/GeneralMills/pytrends) package. This allows quick and easy scraping of Google Trends data from Apify. It allows for scraping of interest over time, interest by region, related topic and related queries. All configurable (less data you need, the faster response are) and output in JSON/XML formats.

---

## Get started

### Running locally

```
python3 -m venv .venv
source .venv/bin/activate
```

### Deploying to Apify

```
apify login
apify push
```

### Inputs

See `INPUT_SCHEMA.json` for available settings.

## Disclaimer

Please note that 429 are thrown by Google Trends when the limit is reached. This is not an error in the code, but a limitation of Google Trends. I'm actively working on a workaround to limit the number of times this is thrown (one of the options being utilization of Apify proxy).

## Notes

Use `apify vis` to validate input schema.
