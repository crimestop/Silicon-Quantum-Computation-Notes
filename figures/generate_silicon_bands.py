"""Replot NIST JARVIS HSE06 silicon bands and locate six equivalent valleys.

Run with the project's plotting Python: python figures/generate_silicon_bands.py
The saved source data and extraction notes are in data/silicon-bandstructure/.
"""

import itertools
import json
import os
from pathlib import Path
import tempfile

# Keep the font cache in a writable location when running in the editor sandbox.
os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "silicon-mpl-cache"))
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/silicon-bandstructure/silicon_hse06_bands.json"
data = json.loads(DATA.read_text())
meta = data["metadata"]
energies = np.array(data["energies_minus_vbm_eV"])
coords = np.array(data["fractional_reciprocal_coordinates_inferred"])
lattice = np.array(meta["opt_band_direct_primitive_lattice_angstrom"])
reciprocal = 2 * np.pi * np.linalg.inv(lattice).T

# The native HSE file labels Gamma-X and Gamma-L but omits coordinates.
# Coordinates below are inferred from the matching official opt-band KPOINTS;
# all 12 label offsets and all 164 samples match. See the saved provenance.
indices = list(range(93, 71, -1)) + list(range(1, 24))
k = coords[indices] @ reciprocal
distance = np.r_[0, np.cumsum(np.linalg.norm(np.diff(k, axis=0), axis=1))]
gamma_index = 21
assert np.allclose(energies[72, :8], energies[0, :8], atol=1e-4)
assert np.isclose(distance[gamma_index] / (distance[-1] - distance[gamma_index]),
                  np.sqrt(3) / 2, atol=1e-5)

plt.rcParams.update({
    "font.family": "serif", "font.serif": ["STIXGeneral"],
    "mathtext.fontset": "stix", "font.size": 10,
    "axes.labelsize": 10, "xtick.labelsize": 10, "ytick.labelsize": 9,
    "axes.linewidth": .7, "pdf.fonttype": 42, "ps.fonttype": 42,
})
blue, orange, gray = "#345F7E", "#C25A1B", "#9AA3AC"
fig = plt.figure(figsize=(6.15, 3.15))
ax = fig.add_axes([.095, .16, .415, .77])
axk = fig.add_axes([.56, .12, .44, .81])

for band in range(8):
    color = blue if band < 4 else (orange if band == 4 else gray)
    ax.plot(distance, energies[indices, band], color=color,
            lw=1.5 if band == 4 else 1.05, zorder=3 if band == 4 else 2)
ax.axhline(0, color="#BEC6CC", lw=.7, ls=(0, (3, 3)), zorder=0)
ax.axvline(distance[gamma_index], color="#CDD2D7", lw=.7, zorder=0)
ax.set(xlim=(distance[0], distance[-1]), ylim=(-6, 5),
       ylabel=r"$E-E_{\mathrm{VBM}}$ (eV)", xlabel="Crystal wave vector along path")
ax.set_xticks([distance[0], distance[gamma_index], distance[-1]],
              [r"$L$", r"$\Gamma$", r"$X$"])
ax.set_yticks([-6, -4, -2, 0, 2, 4])
ax.tick_params(direction="out", length=3, pad=3)
ax.spines[["top", "right"]].set_visible(False)

cbm_path_index = meta["CBM_native_zero_based_index"] - meta["path_first_native_zero_based_index"]
cbm_local = indices.index(cbm_path_index)
minimum = (distance[cbm_local], energies[cbm_path_index, 4])
ax.scatter(*minimum, s=25, color=orange, edgecolor="white", lw=.6, zorder=5)
ax.annotate("valley minimum", xy=minimum, xycoords="data",
            xytext=(.61, .58), textcoords="axes fraction", ha="center", va="center",
            color=orange, fontsize=9,
            arrowprops={"arrowstyle": "->", "color": orange, "lw": .8,
                        "shrinkB": 5})
ax.text(.02, 1.005, "(a)", transform=ax.transAxes, va="bottom", fontsize=11)

# The fcc Brillouin zone has vertices at permutations of (+/-1, +/-1/2, 0)
# in units 2*pi/a, where a is the conventional cubic lattice constant.
# An orthographic projection displays positions, not equal-energy surfaces.
vertices = np.array(sorted(set(itertools.chain.from_iterable(
    itertools.permutations((s, t * .5, 0))
    for s in (-1, 1) for t in (-1, 1)))))
assert vertices.shape == (24, 3)
projection = np.array([[np.sqrt(3) / 2, -.5], [-np.sqrt(3) / 2, -.5], [0, 1]])
projected = vertices @ projection
edges = [(i, j) for i in range(24) for j in range(i + 1, 24)
         if np.isclose(np.linalg.norm(vertices[i] - vertices[j]), np.sqrt(.5))]
assert len(edges) == 36
for i, j in edges:
    axk.plot(*projected[[i, j]].T, color="#CCD2D7", lw=.6, zorder=0)

directions = np.r_[np.eye(3), -np.eye(3)]
labels = [r"$[100]$", r"$[010]$", r"$[001]$",
          r"$[\bar{1}00]$", r"$[0\bar{1}0]$", r"$[00\bar{1}]$"]
valley_fraction = meta["CBM_gamma_X_fraction_sampled"]
for direction, label in zip(directions, labels):
    point = direction @ projection
    axk.plot([0, point[0]], [0, point[1]], color="#7C8A95", lw=.7,
             ls=(0, (3, 3)), zorder=1)
    axk.scatter(*(valley_fraction * point), s=29, color=orange,
                edgecolor="white", lw=.5, zorder=4)
    xy = 1.42 * point
    axk.text(*xy, label, ha="center", va="center", fontsize=9)

xp = projection[0]
axk.scatter(*xp, s=14, facecolor="white", edgecolor="#536472", lw=.7, zorder=3)
axk.text(xp[0] + .09, xp[1] + .07, r"$X$", fontsize=10, ha="left")
axk.scatter(0, 0, s=12, color="#344550", zorder=4)
axk.text(.08, .06, r"$\Gamma$", fontsize=11)
axk.text(.015, 1.0, "(b)", transform=axk.transAxes, va="top", fontsize=11)
axk.set(xlim=(-1.64, 1.64), ylim=(-1.62, 1.62), aspect="equal")
axk.axis("off")
axk.text(.5, -.015, r"Six valley centers in $\mathbf{k}$ space", transform=axk.transAxes,
         ha="center", va="top", fontsize=10)

output = ROOT / "figures/silicon-band-valleys"
fig.savefig(output.with_suffix(".pdf"), metadata={
    "Title": "Silicon HSE06 bands and six equivalent valley centers",
    "Subject": "NIST JARVIS JVASP-1002; energy zero at VBM; see saved provenance",
    "Creator": "figures/generate_silicon_bands.py",
})
fig.savefig(output.with_suffix(".png"), dpi=220)
plt.close(fig)
print(f"Saved {output}.pdf and .png; sampled indirect gap = {meta['path_indirect_gap_eV']:.4f} eV")
