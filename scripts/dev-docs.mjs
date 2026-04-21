#!/usr/bin/env bun
import { createServer } from 'vitepress';

const server = await createServer('docs');
await server.listen();
server.printUrls();
