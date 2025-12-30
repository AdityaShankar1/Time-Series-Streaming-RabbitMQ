import pandas as pd

def test_energy_balance():
    df = pd.DataFrame({
        'Consumption': [100, 200],
        'Production': [150, 150]
    })
    df['Balance'] = df['Production'] - df['Consumption']
    assert df['Balance'].tolist() == [50, -50]

def test_energy_mix():
    df = pd.DataFrame({
        'Production': [100, 200],
        'Nuclear': [20, 40],
        'Wind': [30, 60]
    })
    mix = df[['Nuclear','Wind']].mean() / df['Production'].mean() * 100
    assert round(mix['Nuclear'], 1) == 20.0
    assert round(mix['Wind'], 1) == 30.0
