# stac-api-backends

Comparing STAC API backends.

| Feature | pgstac | elasticsearch | stac-geoparquet[^1] |
| -- | -- | -- | -- |
| Used at scale in production | [✅](https://planetarycomputer.microsoft.com/) | [✅](https://element84.com/earth-search/) | ❌ |
| Docker image available 🐳 | [✅](https://github.com/stac-utils/pgstac/pkgs/container/pgstac) | ❌ | ❌ |
| [stac-fastapi](https://github.com/stac-utils/stac-fastapi) (Python) implementation  | [✅](https://github.com/stac-utils/stac-fastapi-pgstac) | [✅](https://github.com/stac-utils/stac-fastapi-elasticsearch-opensearch)[^2] | ❌ |
| [stac-server](https://github.com/stac-utils/stac-server) (Node.js) implementation | ❌ | ✅ | ❌ |
| [Aggregation](https://github.com/stac-api-extensions/aggregation) | [❌](https://github.com/stac-utils/pgstac/issues/257) | ✅  | ❌ |
| Performance | 🤷‍♂️[^3] | 🤷‍♂️ | 🤷‍♂️ |

[^1]: **stac-geoparquet** is untried as a backend for a STAC API, and we include it in this table so we can update as we learn more
[^2]: Includes both elasticsearch and opensearch implementations.
[^3]: **pgstac** performs best when doing an ordered search on an indexed field, such as `datetime`
