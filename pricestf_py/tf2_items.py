import os
import json

import requests


class TF2Items:
    @staticmethod
    def item_ids_path():
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "item_ids.json"
        )

    @classmethod
    def has_item_ids(cls):
        return os.path.exists(cls.item_ids_path())

    @classmethod
    def get_tf2_items(cls):
        if not cls.has_item_ids():
            raise ValueError(
                "Item ids file not present. "
                + "Download it calling\n"
                + "from pricestf_py import TF2Items\n"
                + "TF2Items.save_item_ids(api_key='my-steam-api-key')"
            )

        with open(cls.item_ids_path()) as json_file:
            item_ids = json.load(json_file)
        return item_ids

    @classmethod
    def save_item_ids(cls, api_key):
        data = []
        start = 0
        while True:
            response = requests.get(
                "https://api.steampowered.com/IEconItems_440/GetSchemaItems/v1/",
                params={"key": api_key, "start": start, "language": "en",},
            )
            result = response.json()["result"]
            data.extend(result["items"])
            start = result.get("next")
            if not start:
                break

        item_ids = {}
        for v in data:
            item_ids[v["item_name"]] = v["defindex"]

        with open(cls.item_ids_path(), "w") as fp:
            json.dump(item_ids, fp, indent=4)
