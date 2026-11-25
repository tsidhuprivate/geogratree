from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
TRAITS_CSV = REPO_ROOT / "data" / "PHYLACINE_1.2" / "Data" / "Traits" / "Trait_data.csv"


def load_felidae_traits():
    traits = pd.read_csv(TRAITS_CSV)
    return traits[traits["Family.1.2"] == "Felidae"].reset_index(drop=True)


if __name__ == "__main__":
    felidae = load_felidae_traits()
    print(f"{len(felidae)} Felidae species")
    print(felidae[["Binomial.1.2", "Mass.g", "IUCN.Status.1.2"]].to_string())
