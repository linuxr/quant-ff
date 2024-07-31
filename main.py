# -*- coding=utf-8 -*-

import fire
from factors import get_factor


def sample():
    factor = get_factor("adosc")
    print(factor.name)
    print(factor.get_parameters())

    factor.set_parameters([[1, 2], [3, 4]])
    print(factor.get_parameters())


if __name__ == "__main__":
    fire.Fire(
        {
            "sample": sample,
        }
    )
