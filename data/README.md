# data/

Put data downloaded from external sources here. Everything in this folder is ignored by git except this README and the submodules listed below, so large or third-party files stay out of the repository.

## PHYLACINE 1.2 (git submodule)

[PHYLACINE 1.2](https://github.com/MegaPast2Future/PHYLACINE_1.2) (Faurby et al. 2018, mammal phylogeny, ranges and traits) is included as a git submodule at `data/PHYLACINE_1.2`, pinned to the `v1.2.1` release. The same release is also archived on Zenodo.

Contents: `Data/Ranges` (about 11,700 GeoTIFF range maps, current and present-natural), `Data/Phylogenies` (two NEXUS files of about 96 MB and 132 MB, stored with Git LFS), `Data/Taxonomy`, `Data/Traits/Trait_data.csv`, and the metadata PDF.

Get it with:

```sh
git clone --recurse-submodules https://github.com/tsidhuprivate/geogratree.git
# or, in an existing clone:
git submodule update --init data/PHYLACINE_1.2
```

The phylogeny `.nex` files are Git LFS objects, so install [Git LFS](https://git-lfs.com) (`git lfs install`) before cloning, otherwise you get small pointer files instead. To skip them, set `GIT_LFS_SKIP_SMUDGE=1` when running the commands above.
