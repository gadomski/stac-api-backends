from httpx import Client

APIS = {
    "aws-earth-search": {
        "url": "https://earth-search.aws.element84.com/v1",
        "collections": [
            "sentinel-2-l2a",
            "sentinel-2-c1-l2a",
            "cop-dem-glo-30",
            "cop-dem-glo-90",
            "landsat-c2-l2",
            "sentinel-2-l1c",
            "sentinel-1-grd",
        ],
    },
    "microsoft-pc": {
        "url": "https://planetarycomputer.microsoft.com/api/stac/v1",
        "collections": ["sentinel-2-l2a"],
    },
}


def main():
    client = Client()
    for key, config in APIS.items():
        count = 0
        for collection in config["collections"]:
            response = client.get(
                f"{config['url']}/search", params=[("collections", collection)]
            )
            response.raise_for_status()
            data = response.json()
            if "context" in data:
                count += data["context"]["matched"]
                print(key, collection, data["context"]["matched"])
        print(key, count)


if __name__ == "__main__":
    main()
