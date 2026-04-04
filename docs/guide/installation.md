# Installation

## Prerequisites

- **Node.js** 18 or higher
- **npm** 9 or higher (or yarn/pnpm)
- **Docker** (optional, for containerized deployment)
- **Git** 2.30 or higher

## Install from Source

```bash
# Clone the repository
git clone https://github.com/OpenSIN-AI/OpenSIN.git
cd OpenSIN

# Install dependencies
npm install

# Build the project
npm run build

# Run tests
npm test
```

## Install via npm

```bash
npm install @opensin/core
```

## Docker Deployment

```bash
# Using Docker Compose
docker-compose up -d

# Using Docker
docker build -t opensin .
docker run -p 3000:3000 opensin
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `NODE_ENV` | Environment (development/production) | No |
| `PORT` | Server port (default: 3000) | No |
| `OPENAI_API_KEY` | OpenAI API key | Yes |
| `ANTHROPIC_API_KEY` | Anthropic API key | No |
| `GOOGLE_API_KEY` | Google API key | No |
| `TELEGRAM_BOT_TOKEN` | Telegram bot token | No |
| `DISCORD_BOT_TOKEN` | Discord bot token | No |

## Verify Installation

```bash
# Run the hello world example
npm run example:hello-world

# Run benchmarks
npm run benchmarks
```

## Next Steps

- [Quick Start](/guide/quick-start) — Get started in 5 minutes
- [Core Concepts](/guide/core-concepts) — Learn the fundamentals
