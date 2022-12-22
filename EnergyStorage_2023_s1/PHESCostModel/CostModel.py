# Author: Jingran
# The cost model of PHES module based on
# https://docs.google.com/spreadsheets/d/11bFXnNKr1owT3xGqLR3pNUcy8UGSeM15/edit#gid=1789734258

import copy

from DefualtParameters import *


def parameters_initial(**kwargs):
    dic = copy.deepcopy(INPUT_DEFAULT_VALUE)

    dic["head"] = kwargs["head"]
    dic["separation"] = kwargs["separation"]
    keys = dic.keys()
    for key in kwargs.keys():
        if key not in ("head", "separation"):
            if key in keys:
                dic[key] = kwargs[key]
    return dic


class CostModel():

    def __init__(self, **kargs):
        self.potential_energy = POTENTIAL_ENERGY
        self.pumping_efficiency = PUMPING_EFFICIENCY
        self.generation_efficiency = GENERATION_EFFICIENCY
        self.usable_fraction_water_volume = USABLE_FRACTION_WATER_VOLUME
        self.dam_cost = DAM_COST
        self.power_benchmark_cost = POWER_BENCHMARK_COST
        self.energy_benchmark_cost = ENERGY_BENCHMARK_COST

        self.exchange_rate_to_USD = kargs["exchange_rate_to_USD"]
        self.head = kargs["head"]
        self.separation = kargs["separation"]
        self.power_rating = kargs["power_rating"]
        self.stored_energy = kargs["stored_energy"]
        self.equity_fraction = kargs["equity_fraction"]
        self.equity_rate_of_return = kargs["equity_rate_of_return"]
        self.bank_interest_rate = kargs["bank_interest_rate"]
        self.inflation_rate = kargs["inflation_rate"]
        self.energy_purchase_price = kargs["energy_purchase_price"]
        self.system_life = kargs["system_life"]
        self.pumping_generating_cycles_annually = kargs["pumping_generating_cycles_annually"]
        self.water_to_rock = kargs["water_to_rock"]


if __name__ == '__main__':
    pass
