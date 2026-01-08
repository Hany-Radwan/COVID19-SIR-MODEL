import pytest
from sir_model import SIRModel

def test_initialization():
    model = SIRModel(1000, 10, 0, 0.3, 0.1)
    assert model.S == 990
    assert model.I == 10

def test_population_conservation():
    N = 1000
    model = SIRModel(N, 5, 0, 0.5, 0.1)
    model.run_simulation(50)
    final_S = model.S_list[-1]
    final_I = model.I_list[-1]
    final_R = model.R_list[-1]
    # S+I+R must equal N (allowing for tiny math rounding errors)
    assert abs((final_S + final_I + final_R) - N) < 0.0001