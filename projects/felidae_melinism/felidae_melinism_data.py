from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
TRAITS_CSV = REPO_ROOT / "data" / "PHYLACINE_1.2" / "Data" / "Traits" / "Trait_data.csv"
EXTINCT_STATUSES = ["EP", "EX", "EW"]


def load_felidae_traits(include_extinct=False):
    traits = pd.read_csv(TRAITS_CSV)
    felidae = traits[traits["Family.1.2"] == "Felidae"]
    if not include_extinct:
        felidae = felidae[~felidae["IUCN.Status.1.2"].isin(EXTINCT_STATUSES)]
    return felidae.reset_index(drop=True)


if __name__ == "__main__":
    felidae = load_felidae_traits()
    print(f"{len(felidae)} Felidae species")
    print(felidae[["Binomial.1.2", "Mass.g", "IUCN.Status.1.2"]].to_string())
