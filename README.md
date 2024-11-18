# Crypto News Tweet Generator Bot

An automated system that generates witty pro-crypto tweets based on news articles (via CoinTelegraph), 
market activity (via GeckoTerminal), and crypto Twitter discussions. 
Uses Claude for news summarization and contextual tweet generation.

An automated system that generates witty pro-crypto tweets based on news articles (via CoinTelegraph), 
market activity (via GeckoTerminal), and crypto Twitter discussions.
Uses Claude for news summarization and contextual tweet generation. 
Now supports **posting on Twitter and Farcaster**. 
Includes a dedicated branch for Farcaster-only posting.


NOTE: Please remember to delete `article_summaries.json` and `generated_tweets.json` files each time you do a fresh run.

## Prerequisites

- Python 3.10+
- Anthropic API key
- Twitter API with Read & Write enabled for OAuth 1.0a / 2.0

## Installation


#### **For Twitter Integration**
```env
BEARER_TOKEN=your_twitter_bearer_token
API_KEY=your_twitter_api_key
API_KEY_SECRET=your_twitter_api_secret
ACCESS_TOKEN=your_twitter_access_token
ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
```

#### **For Farcaster Integration**
- You must use an **Ethereum wallet private key** for an account that already exists on Farcaster.
- Add the private key in the `.env` file as `EVM_SEED_PHRASE` (mnemonic seed phrase or private key).

```env
EVM_SEED_PHRASE=your_ethereum_wallet_mnemonic_or_private_key
```

## **Branches**
The project now has two main branches:

1. **`master`**: Posts on both Twitter and Farcaster.
2. **`farcaster-post-integration`**: Dedicated branch for Farcaster-only posting. Removes Twitter-specific dependencies.

---

## **New Farcaster-Specific Features**

### Farcaster Integration
The bot uses the **Warpcast SDK** for Farcaster integration. It requires:

- An Ethereum wallet private key for an account registered on Farcaster.
- Posts are created using the Warpcast `post_cast` method.

### Key Updates

#### **Environment Variable**:
- Add the `EVM_SEED_PHRASE` in your `.env` file for wallet authentication.
```env
EVM_SEED_PHRASE=your_ethereum_wallet_mnemonic_or_private_key

## System Flow

The system automatically:
1. Fetches and summarizes crypto news articles every 12 hours
2. Updates tweet cache from monitored accounts every hour
3. Fetches trending pools data from GeckoTerminal
4. Generates and posts a witty pro-crypto tweet when you hit `POST http://localhost:8000/trigger-tweet`

Each tweet is generated considering:
- Latest crypto news summaries
- Recent tweets from influential crypto accounts
- Current market activity and trends
- Historical example tweets

## Configuration

Create `tweets_config.json` with example tweets:
```json
{
  "pro_crypto": [
    "Example tweet showing optimistic crypto perspective",
    "Example tweet highlighting innovation in the space",
    "Example tweet about market dynamics"
  ]
}
```

## Data Sources

- **News**: CoinTelegraph RSS feed
- **Market Data**: GeckoTerminal API (trending pools, volume, transactions)
- **Social Context**: Monitored crypto Twitter accounts
- **Example Style**: Curated pro-crypto tweets from `tweets_config.json`

## Monitoring

Access system status via HTTP endpoints:
- Health check: `http://localhost:8000/health`
- Statistics: `http://localhost:8000/stats`
- Manual article fetch: `POST http://localhost:8000/fetch-articles`
- Manual tweet generation: `POST http://localhost:8000/trigger-tweet`

The stats endpoint provides:
- Total articles processed
- Total tweets generated
- Next scheduled tweet time
- System status

## Project Structure

The project consists of several key components:
- `main.py`: FastAPI app, scheduling, and endpoints
- `agent.py`: Article processing and tweet generation
- `config.py`: System configuration and prompts
- `twitter_helpers.py`: Twitter API integration
- `tweets_cache.py`: Tweet caching system
- `gecko_terminal.py`: Market data integration

## Logs

The system maintains detailed logs of:
- Article fetching and summarization
- Tweet generation and posting
- Market data updates
- Cache management
- System status and errors

Logs use standard Python logging with timestamps and levels for easy monitoring.
