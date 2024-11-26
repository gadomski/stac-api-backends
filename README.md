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

## What does it mean to be "at scale"?

Most of the large commercial STAC APIs ([Microsoft's Planetary Computer](https://planetarycomputer.microsoft.com/), [AWS's Earth Search](https://element84.com/earth-search/)) don't publish user numbers, so it's hard to know how these backends hold up in terms of simultaneous users.
In terms of data size, the last [comprehensive crawl](https://developers.planet.com/blog/2022/Aug/31/state-of-stac/) was done in 2022 by Tim Schaub at Planet.
In that report, he found that the largest APIs had over 100M [items](https://github.com/radiantearth/stac-spec/blob/master/item-spec/item-spec.md).
A quick check on 2024-11-26 of AWS Earth Search shows 104M items, though some of those may be duplicates due to ongoing [Sentinel 2 reprocessing efforts](https://us13.campaign-archive.com/?u=a7a7fcb1ce46c4d001fc76289&id=c5e6cf4785).

[^1]: **stac-geoparquet** is untried as a backend for a STAC API, and we include it in this table so we can update as we learn more
[^2]: Includes both elasticsearch and opensearch implementations.
[^3]: **pgstac** performs best when doing an ordered search on an indexed field, such as `datetime`
