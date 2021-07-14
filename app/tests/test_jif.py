import contextvars
from pprint import pprint

from fastapi.testclient import TestClient

from app import main

VERSION = "v1"

client = TestClient(main.app)


def test_part_list():

    response = client.get(f"/api/{VERSION}/parts")

    pprint(response.json())

    assert response.status_code == 200

    assert response.json() == ["ad9680", "adrv9009", "ad9081_rx", "ad9144"]


def test_hmc7044_solve():
    response = client.post(
        f"/api/{VERSION}/clock/solve/",
        json={
            "part": "hmc7044",
            "vcxo": 125000000,
            "output_clocks": [1e9, 500e6, 7.8125e6],
            "custom_props": {"r2": 1},
        },
    )
    pprint(response.json())

    assert response.status_code == 200
    ref = {
        "config": {
            "n2": 12,
            "out_dividers": [3, 6, 384],
            "output_clocks": {
                "clock_0": {"divider": 3, "rate": 1000000000.0},
                "clock_1": {"divider": 6, "rate": 500000000.0},
                "clock_2": {"divider": 384, "rate": 7812500.0},
            },
            "r2": 1,
        },
        "part": "hmc7044",
    }

    assert response.json() == ref
