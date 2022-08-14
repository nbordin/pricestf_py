import requests

from .tf2_items import TF2Items
from .tf2_item_qualities import TF2_ITEM_QUALITIES


BASE_URL = "https://api2.prices.tf/"
TF2_ITEMS = None


class PricesTF:
    token = None
    verify = True

    def __init__(self, token=None, verify=True):
        self.verify = verify
        if not token:
            self.get_token()

    def _request(self, method, url, params=None, data=None):
        headers = {}
        if self.token:
            headers["Authorization"] = "Bearer " + self.token

        response = requests.request(
            method,
            BASE_URL + url,
            params=params,
            data=data,
            headers=headers,
            verify=self.verify,
        )
        if response.ok:
            return response.json()

    def get_token(self):
        data = self._request("POST", "auth/access")
        self.token = data["accessToken"]

    def prices(self, page=1, limit=100, order="ASC"):
        if order not in ["ASC", "DESC"]:
            raise ValueError("order must be either ASC or DESC.")
        return self._request(
            "GET",
            "prices",
            params={"page": page, "limit": limit, "order": order},
        )

    @staticmethod
    def _compose_sku(item_id, quality, craftable, australium, killstreak):
        sku = str(item_id) + ";" + str(quality)
        if not craftable:
            sku += ";uncraftable"
        if australium:
            sku += ";australium"
        if killstreak > 0 and killstreak <= 3:
            sku += f";kt-{killstreak}"
        return sku

    def price_by_sku(
        self, item_id, quality, craftable=True, australium=False, killstreak=0
    ):
        sku = self._compose_sku(
            item_id, quality, craftable, australium, killstreak
        )
        return self._request("GET", "prices/" + sku)

    def price_by_name(
        self,
        item_name,
        quality_name,
        craftable=True,
        australium=False,
        killstreak=0,
    ):
        global TF2_ITEMS

        if TF2_ITEMS is None:
            TF2_ITEMS = TF2Items.get_tf2_items()

        item_id = TF2_ITEMS.get(item_name)
        if not item_id:
            raise ValueError(f"Invalid item {item_name}")
        quality = TF2_ITEM_QUALITIES.get(quality_name.lower())
        if not quality:
            raise ValueError(f"Invalid quality {quality_name}")

        return self.price_by_sku(
            item_id, quality, craftable, australium, killstreak
        )
