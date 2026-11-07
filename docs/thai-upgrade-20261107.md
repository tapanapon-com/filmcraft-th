# Filmcraft Thai upgrade 7 November 2026

Upstream release: https://github.com/storytold/filmcraft/releases/tag/v0.18.0

Thai distribution being prepared: 0.18.0-th.1. Based on the complete upstream release tag, preserving its engine and format crate versions. Existing Thai translations remain, with new source strings translated. Current Thai catalog: 3,786 entries.

Catalog validation passed. Native build, platform packaging and integration checks are in progress. This record does not claim that installers have been released or that all upstream functionality has been tested. Previous 0.17.1 validation reports remain historical.

Mac builds are ad-hoc signed and are not Apple-notarized. Windows builds are unsigned. Build one job at a time.

The merge is checkpointed on the upgrade branch for full external CI before publication. Local catalog and Python syntax checks passed; formatting passed. A checkpoint commit does not mean the default branch or installers have been published. Full workspace checks use one GitHub runner to avoid local system-disk/swap pressure observed while compiling the sibling VectorCraft workspace.
