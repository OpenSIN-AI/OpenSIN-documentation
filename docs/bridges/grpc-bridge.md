# gRPC Bridge

> **Status:** ✅ Active | **Type:** RPC Communication

## Overview

gRPC bridge enables high-performance RPC communication between OpenSIN services.

## Protocol Buffers

```protobuf
service AgentService {
  rpc ExecuteTask (TaskRequest) returns (TaskResponse);
  rpc StreamLogs (LogRequest) returns (stream LogEntry);
}
```

## Usage

Used for internal service-to-service communication with low latency.

---

*Last updated: 2026-04-04 by SIN-Zeus*
