from pathlib import Path

import pandas as pd

TRAITS_CSV = Path(__file__).resolve().parents[2] / "data" / "PHYLACINE_1.2" / "Data" / "Traits" / "Trait_data.csv"
EXTINCT_STATUSES = ["EP", "EX", "EW"]

traits = pd.read_csv(TRAITS_CSV)
felidae = traits[(traits["Family.1.2"] == "Felidae") & ~traits["IUCN.Status.1.2"].isin(EXTINCT_STATUSES)].reset_index(drop=True)

print(f"{len(felidae)} Felidae species")
print(felidae[["Binomial.1.2", "Mass.g", "IUCN.Status.1.2"]].to_string())
