from pathlib import Path

import pandas as pd

TRAITS_CSV = Path(__file__).resolve().parents[2] / "data" / "PHYLACINE_1.2" / "Data" / "Traits" / "Trait_data.csv"
EXTINCT_STATUSES = ["EP", "EX", "EW"]

traits = pd.read_csv(TRAITS_CSV)
felidae = traits[traits["Family.1.2"] == "Felidae"]
felidae = felidae[~felidae["IUCN.Status.1.2"].isin(EXTINCT_STATUSES)]
