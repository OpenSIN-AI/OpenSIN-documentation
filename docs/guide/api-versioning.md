# API Versioning & Migration Guide

Manage API versions and migrate between them safely.

## Versioning Strategy

OpenSIN uses URL-based versioning:

```
https://api.opensin.ai/v1/agents
https://api.opensin.ai/v2/agents
```

## Current Versions

| Version | Status | End of Life |
|---------|--------|-------------|
| v1 | ✅ Stable | 2027-04-04 |
| v2 | 🔄 Beta | - |

## Migration Guide: v1 → v2

### Breaking Changes

| Change | v1 | v2 | Migration |
|--------|----|----|-----------|
| Agent creation | `POST /agents` | `POST /v2/agents` | Update URL |
| Response format | `{agent: {...}}` | `{data: {...}, meta: {...}}` | Update parsing |
| Error format | `{error: "message"}` | `{error: {code, message, details}}` | Update error handling |
| Pagination | `?page=1&limit=20` | `?cursor=abc&limit=20` | Use cursor-based pagination |

### Non-Breaking Changes

- New fields added to responses
- New optional parameters
- New endpoints

### Migration Steps

1. **Update base URL**
   ```python
   # Old
   client = Client(base_url="https://api.opensin.ai/v1")
   
   # New
   client = Client(base_url="https://api.opensin.ai/v2")
   ```

2. **Update response parsing**
   ```python
   # Old
   agent = response.json()["agent"]
   
   # New
   agent = response.json()["data"]
   meta = response.json()["meta"]
   ```

3. **Update error handling**
   ```python
   # Old
   if response.status_code != 200:
       print(response.json()["error"])
   
   # New
   if response.status_code != 200:
       error = response.json()["error"]
       print(f"{error['code']}: {error['message']}")
   ```

4. **Update pagination**
   ```python
   # Old
   agents = []
   page = 1
   while True:
       response = client.get(f"/agents?page={page}&limit=20")
       agents.extend(response.json()["agents"])
       if len(response.json()["agents"]) < 20:
           break
       page += 1
   
   # New
   agents = []
   cursor = None
   while True:
       params = {"limit": 20}
       if cursor:
           params["cursor"] = cursor
       response = client.get("/agents", params=params)
       data = response.json()
       agents.extend(data["data"])
       cursor = data["meta"].get("next_cursor")
       if not cursor:
           break
   ```

## Deprecation Policy

1. **6 months notice** before end of life
2. **Warning headers** in API responses
3. **Migration guide** provided
4. **Support** during transition period

### Deprecation Headers

```
Deprecation: true
Sunset: Sat, 04 Apr 2027 00:00:00 GMT
Link: <https://docs.opensin.ai/guide/api-versioning>; rel="deprecation"
```

## Best Practices

1. **Always specify version** in API calls
2. **Monitor deprecation headers**
3. **Test against new versions** before they become stable
4. **Subscribe to changelog** for breaking changes
5. **Use SDK** — SDKs handle version compatibility

## Next Steps

- [API Reference](/api/overview)
- [SDK Overview](/api/sdk-overview)
- [Changelog](/guide/changelog)
