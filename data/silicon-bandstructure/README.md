# Bulk silicon band data

The figure in §1.2 uses **calculated HSE06 bands for bulk diamond silicon**,
NIST JARVIS-DFT record JVASP-1002. It is not an experimental band measurement.

- Material record: https://www.ctcms.nist.gov/~knc6/jsmol/JVASP-1002.html
- Raw XML: https://www.ctcms.nist.gov/~knc6/static/JARVIS-DFT/JVASP-1002.xml
- Same-material optB88-vdW band input/output archive: https://ndownloader.figshare.com/files/23713301
- NIST reuse statement: https://www.nist.gov/copyrights-disclaimers
- Retrieved: 2026-10-10. Original checksums are in `silicon_hse06_metadata.json`.

`extract_hse.py` extracts the HSE06 block from the saved XML, discards the
first 29 non-path samples, and writes JSON/CSV. The retained path has 164
points and 32 bands. The figure displays the lowest eight spin-up bands;
these agree with the spin-down bands within 0.0001 eV. Energies are shifted
from the source's Fermi reference to the valence-band maximum. No gap
correction, fitting, or smoothing is applied: straight lines join samples.
The sampled indirect gap is 1.2157 eV. The minimum along Gamma-X is at
19/23 of that segment; it is not artificially moved to the usual approximate
bulk-silicon value of 0.85.

## Wave-vector coordinates

The HSE XML supplies sample indices and high-symmetry labels, but no k
coordinates. The official opt-band KPOINTS contains 164 points and matches
**all 12 high-symmetry node offsets** after removal of the HSE file's first
29 points. Its reciprocal coordinates are therefore used as an explicitly
inferred mapping. This provenance is recorded in the JSON field name
`fractional_reciprocal_coordinates_inferred` and in the metadata. The
opt-band POSCAR supplies a reciprocal metric. Only node labels are shown
on the figure's horizontal axis; no HSE lattice constant is asserted.

The plotted L-Gamma-X path concatenates path indices 93 down to 72 and
1 through 23. The two Gamma samples agree. Cubic symmetry allows X to be
represented along [100]. Panel (b) is a geometric diagram of six equivalent
valley centers inside the first fcc Brillouin zone, not an energy surface.
Its radial fraction uses the sampled minimum above, and its crystal axes
need not align with the device axes used in the note.

## Reproduce

From the project root, using the Python environment with NumPy and Matplotlib:

```sh
python data/silicon-bandstructure/extract_hse.py
python figures/generate_silicon_bands.py
```

The extraction script uses only the Python standard library. Both commands
use saved local files and require no network access. `silicon_hse06_bands.json`
is the figure's input; the CSV and separate metadata are also retained for
inspection. Source credit is given in the figure caption and bibliography.
