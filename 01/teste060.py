import pandas as pd


dados = {
    "carros": [
        {"nome": "gol", "preco": 23000, "ano": 2015, "seguro": True},
        {"nome": "celta", "preco": 18000, "ano": 2010, "seguro": False},
        {"nome": "corolla", "preco": 64000, "ano": 2018, "seguro": False},
        {"nome": "kombi", "preco": 30000, "ano": 2009, "seguro": False},
        {"nome": "montana", "preco": 37600, "ano": 2019, "seguro": True}
        
    ],
    "lugares": [
        "curitiba", "recife", "canoas", "bicas", "bonito"
    ]
}

df = pd.DataFrame(dados)
df

print('---------------------')