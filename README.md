# Prices.tf API


`pricestf_py` is a library to get Team Fortress 2 items' prices from prices.tf API.

Prices can be queried both by items' SKUs or names: to get prices from item names a Steam API key is required.


## Installation

```bash
pip3 install pricestf_py
```

If you are planning to get the items' prices using their names, after installing the package run:

```python
from pricestf_py import TF2Items

TF2Items.save_item_ids(api_key='your-steam-api-key')
```

This method will download the list of item IDs which are necessary to generate the items' SKUs.

Use it also to update the items list (e.g. when new items are added to Team Fortress 2).


## Examples

```python
from pricestf_py import PricesTF

# Get token from prices.tf API
ptf = PricesTF()

# get item prices from its name
response = ptf.price_by_name("Rump-o'-Lantern", "Unique", craftable=False, australium=False, killstreak=0)
print(response)

# get item price from its SKU
r = ptf.price_by_sku(869, 6, craftable=False, australium=False, killstreak=0)
print(response)
```
