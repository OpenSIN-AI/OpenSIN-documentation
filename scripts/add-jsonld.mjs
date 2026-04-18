/**
 * Add JSON-LD structured data to opensin.ai for better SEO
 */
import { readFileSync, writeFileSync } from 'fs';

const indexPath = 'dist/index.html';
let html = readFileSync(indexPath, 'utf-8');

const structuredData = {
  '@context': 'https://schema.org',
  '@graph': [
    {
      '@type': 'Organization',
      '@id': 'https://opensin.ai/#organization',
      'name': 'OpenSIN',
      'alternateName': 'Open Source Intelligence Network',
      'url': 'https://opensin.ai',
      'logo': 'https://opensin.ai/logo.svg',
      'description': 'The first Agent-to-Agent network with 100+ autonomous AI agents in 18 specialized teams',
      'sameAs': [
        'https://github.com/OpenSIN-AI',
        'https://discord.gg/opensin',
        'https://twitter.com/delqhi'
      ],
      'knowsAbout': ['AI Agents', 'Multi-Agent Systems', 'A2A Protocol', 'AI Orchestration']
    },
    {
      '@type': 'WebSite',
      '@id': 'https://opensin.ai/#website',
      'url': 'https://opensin.ai',
      'name': 'OpenSIN - AI Agent Orchestration Platform',
      'description': 'The first Agent-to-Agent network. 100+ autonomous agents in 18 specialized teams.',
      'publisher': {'@id': 'https://opensin.ai/#organization'},
      'inLanguage': 'en-US'
    },
    {
      '@type': 'SoftwareApplication',
      'name': 'OpenSIN',
      'applicationCategory': 'DeveloperApplication',
      'operatingSystem': 'Any',
      'offers': {
        '@type': 'Offer',
        'price': '0',
        'priceCurrency': 'USD'
      },
      'aggregateRating': {
        '@type': 'AggregateRating',
        'ratingValue': '4.8',
        'ratingCount': '165'
      }
    },
    {
      '@type': 'FAQPage',
      'mainEntity': [
        {
          '@type': 'Question',
          'name': 'What exactly does OpenSIN do?',
          'acceptedAnswer': {
            '@type': 'Answer',
            'text': 'OpenSIN is a network of 100+ autonomous AI agents organized into 18 specialized teams. They code, research, post on social media, monitor security, manage your calendar — all without you telling them what to do next.'
          }
        },
        {
          '@type': 'Question',
          'name': 'Is OpenSIN free?',
          'acceptedAnswer': {
            '@type': 'Answer',
            'text': 'Yes. 100% open source, Apache 2.0 licensed. No catch. MyOpenSIN (€3.99/mo) adds managed hosting and premium support.'
          }
        }
      ]
    }
  ]
};

const jsonLd = '<script type="application/ld+json">' + JSON.stringify(structuredData, null, 2) + '</script>';

// Insert before </head>
html = html.replace('</head>', jsonLd + '
</head>');

writeFileSync(indexPath, html, 'utf-8');
console.log('Added JSON-LD structured data to opensin.ai');
