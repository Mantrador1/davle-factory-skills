# WEB RESEARCH - Internet Research & Data Gathering

## Purpose
Enable web research via APIs and scraping. No external dependencies.

## Quick Commands

### DuckDuckGo Search (Free, No API Key)
```bash
ddg_search() {
  curl -s "https://api.duckduckgo.com/?q=$1&format=json" | jq -r '.AbstractText'
}
```

### Web Page Scraping
```bash
scrape_page() {
  curl -s "$1" | sed 's/<[^>]*>//g' | grep -v '^[[:space:]]*$' | head -100
}
```

### GitHub Search
```bash
github_search() {
  curl -s "https://api.github.com/search/repositories?q=$1&sort=stars&per_page=5" | \
    jq -r '.items[] | "\(.name) - \(.html_url)"'
}
```

## Usage Examples
```bash
# Competitor research
ddg_search "MD307 watch face reviews"

# Tech docs
scrape_page "https://developer.android.com/training/wearables"

# Find libraries
github_search "wear os complications"
```

## TL;DR
Basic web research without external dependencies. 🔍
