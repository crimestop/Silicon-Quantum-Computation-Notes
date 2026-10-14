# Silicon Quantum Dot Quantum Computing

[Read the compiled PDF](output/pdf/main.pdf) · [LaTeX entry file](main.tex)

English research notes for readers who know quantum mechanics but do not
assume a background in semiconductor devices or measurement circuits.

The notes use the standard LaTeX `article` class, with an unnumbered
Preface, eight main sections, and 25 appendices arranged by their role in
the main text. The main text
develops the central question: how
confined electrons in silicon can store, manipulate, and reveal quantum
information. It gives the results, physical interpretation, and conditions
needed to follow that explanation. Detailed derivations, specialized
calculations, measurement protocols, and supplementary topics are kept in
the appendices for consultation as needed. The main text is organized by
its physical argument; an appendix topic does not automatically require a
corresponding formula or tutorial in the main text.

## Preface

The Preface appears after the title and before the table of contents.
It states the question addressed by the notes and defines the shared
conventions: spin quantum numbers, physical and logical Pauli operators,
basis order, logical rotations, time evolution, and
phases. It also collects the general Pauli, Hadamard, SWAP, square-root
SWAP, CZ, and CNOT forms and their rotation or gate identities. Its
formulas use Pref.1–Pref.9 to distinguish them from Appendix P. The physical encodings are defined in section 3;
their Hamiltonians and pulse implementations are developed in sections 4
and 6.

## Main text

1. What is a quantum dot?
2. Controlling the electron number.
3. Qubit architectures and encodings.
4. Engineering spin control and exchange interactions.
5. Initialization and spin readout.
6. Quantum gates.
7. Coherence and loss of quantum information.
8. Selecting and connecting qubits in an array.

The opening first explains a quantum dot as confined electrons in a
localized potential well, then selects a gate-controlled silicon
implementation. Device potentials lead to orbitals, valley states, and
fixed-electron-number energies. A fourth subsection uses a local basis to
divide a coupled-dot system at fixed total electron number into charge
subspaces. Each subspace has its own ground and excited states; transfer
terms mix different subspaces. A one-electron double dot shows why weak
mixing requires a small transfer matrix element relative to the connected
level spacing: near degeneracy can produce strong mixing even when the
tunnel coupling is small.
Section 2 first explains how energy exchange with a reservoir and gate
voltages select electron number. Section 2.1 chooses one electron for the
single-spin qubit used later, then uses a one-dimensional charge map to
show emptying, loading, and retention. Section 2.2 chooses the (1,1)
configuration for the later two-dot spin model, then uses the honeycomb
diagram to distinguish reservoir exchange from interdot transfer and
select voltages that prepare one electron per dot. Section 3 defines the single-spin logical basis and
the two-spin and three-spin encodings. The four spin states of a two-dot
(1,1) charge configuration show why charge preparation alone does not
select a spin state.

Section 4 starts with static Zeeman splitting and the conditions for
retaining a two-level spin space, then introduces transverse driving and
exchange. This puts the Hamiltonians after the computational spaces on
which they act. The voltage response needed to select electron number is
introduced in section 2. Compensation of two-dot level shifts appears in
section 4.3, where changing a tunnel barrier is used to control exchange;
its array extension is discussed in section 8. Rotating-frame and
spin–orbit algebra, fermionic sign calculations, and the detailed
elimination of charge amplitudes are developed in the appendices.

Section 5 explains how to prepare the encoded spin states and read them
out. Its opening states the spin-to-charge conversion and points to
Appendix G.2 for the separate sensor; the detailed detector response is
kept there, including position sensitivity and time-resolved charge records.
With these input states and measured outcomes established, section 6
uses the control Hamiltonians to construct rotations and entangling gates.
Its opening uses the evolution operator defined in the Preface and states
the conditions for returning to the computational space. The three
encoding-specific subsections give the Hamiltonians, resulting evolution,
and calibrated pulse conditions that realize the common gate definitions.
Section 6.1 retains the exchange pulse areas for SWAP and square-root SWAP
and the exchange construction of CZ. Sections 6.2 and 6.3 give the encoded
realizations or, for the six-spin CNOT, the target and sequence requirements.
Generic matrices and gate identities are collected in the Preface.

Where a model parameter or pulse condition determines an operation, the
main text identifies the quantity to measure and the voltage, frequency,
phase, or duration chosen from it. Measurements use the relevant operating
settings and complete pulse waveforms, including finite edges where they
affect the rotation angle. The cited appendices contain the signals, scans,
and parameter-extraction procedures. Appendix N.1.2 includes the calibration
of a fixed edge area and its contribution to the required hold time.

## Appendices

Each appendix is a section, numbered A--Y. Its boundary follows the
specific result or question it expands in the main text. Calculations that
serve different purposes are separated even when they use the same model;
material serving one control or readout problem is collected together.
The order below follows those uses: Appendix G explains how electron-number
changes produce electrical signals, then Appendix H uses those signals to
map double-dot charge stability. Appendix G also supports the readout
signal in section 5. Appendix L derives the rotating-frame dynamics and
rotating-wave approximation for the generic transverse coupling used in
section 4.2. Appendix M relates that coupling to direct magnetic driving,
electric motion in a magnetic-field gradient, and spin–orbit response.
Its effective gate-dependent Zeeman model also incorporates orbital and
valley contributions without counting the same response twice. The final
subsection connects electric-motion mechanisms to voltage amplitude and
phase programming. Section 4.2 cites Appendix M when the oscillating
transverse coupling is introduced and Appendix L when changing to the
rotating frame. Appendix N develops calibration and implementation of
single-qubit and two-qubit gates for single-spin qubits. Model
inference and calibration feedback remain supplementary methods at the end. There are no additional group headings
in the PDF.

| Appendix | Topic | Role in the main text | Source suffix in `sections/appendix-*.tex` |
|---|---|---|---|
| A | Calculating the confining potential | §1: obtain the potential from geometry, materials, and voltages | `device-confinement` |
| B | Orbital states in the effective-mass approximation | §1: derive the orbital equation and calculate bound states | `effective-mass` |
| C | Valley states and interface coupling | §1: obtain coupled orbital–valley states and the valley gap | `valley-states` |
| D | Screening of the Electron--Electron Interaction | §1.3: explain the screened interaction used in the many-electron Hamiltonian | `screened-interaction` |
| E | Calculating many-electron energies | §§1–2: fixed-charge energies, charge-subspace blocks, and coupled-dot matrix elements; E.2 gives the general orbital-basis representation and exact charge-projector decomposition | `interacting-models` |
| F | How voltages set and preserve model parameters | §2: threshold response; §4: compensation while tuning exchange; §8: include affected neighbours | `voltage-response` |
| G | Electrical detection of charge | §2: support the brief statement that electron-number changes are electrically detectable; §5: calculate the electrical signal after spin-to-charge conversion; G.2 includes spatial sensitivity to charge rearrangement and time-resolved detection | `charge-detection` |
| H | Double-dot charge stability diagrams | §2.2: derive the boundaries shown in the main-text honeycomb diagram and explain measurement details; §3.1: distinguish charge labels from spin states | `charge-stability` |
| I | Spectroscopy of dot excitations | §4.1: check excitation gaps and spin–valley mixing | `dot-spectroscopy` |
| J | From Orbital Hamiltonians to Spin Exchange | §4.3: justify the one-spatial-state and density-interaction approximations, then eliminate high-energy charge states to obtain exchange and virtual-charge weight | `exchange-reduction` |
| K | Measuring interdot tunneling | §4.3: determine the coherent tunneling parameter used in the exchange model | `tunnel-coupling` |
| L | Rotating Frame | §§4.2 and 6: derive the generic transverse-drive rotating-wave approximation and control axes | `spin-driving` |
| M | Physical Origins of Transverse Spin Driving | §§4.2 and 6: explain physical sources of the effective transverse coupling and the required reductions; §8: supply the local electric-drive response | `transverse-drive-origins` |
| N | Single-Spin Control and Exchange Gates | §6: calibrate and implement single-qubit and two-qubit gates for single-spin qubits, including systematic pulse corrections | `single-spin-control` |
| O | Singlet–triplet qubit control | §6: logical rotations, capacitive entanglement, and residual coupling | `st-control` |
| P | Exchange-only qubit control | §6: projected axes, waveform conditions, and six-spin gate checks | `exchange-only-control` |
| Q | From tunneling amplitudes to rate equations | §5: justify the reservoir rates and waiting-time laws | `open-system-dynamics` |
| R | Preparing spin-qubit states | §5: work out loading and separation conditions for each encoding | `state-preparation` |
| S | Converting spin states into readout probabilities | §5: conversion, classification, and probabilities; §8: joint readout | `spin-readout` |
| T | Gate verification and fidelity | §5: expand state and gate reconstruction beyond one output population | `gate-verification` |
| U | Coherence, relaxation, and pulse errors | §7: distinguish waiting-time measurements, angle noise, and leakage | `noise-leakage` |
| V | Connectivity, parallel gates and spectator response | §8: check target selection, spectator effects, and parallel scheduling | `array-parallel-control` |
| W | Communication between qubits | §8: expand SWAP routing, shuttling, and mode-mediated coupling | `qubit-communication` |
| X | Inferring and testing an effective model | Supplement to §§2 and 4: infer parameters from several measurements and test an independent prediction | `model-inference` |
| Y | Calibration feedback | Supplement to §§2 and 6: convert measured errors into control updates | `calibration-feedback` |

The 25 appendix entry files are listed above. Appendix F also loads
`sections/appendix-virtual-gates.tex` as a component, not an additional
appendix. Array voltage compensation is part of F; joint readout is part
of S. The former combined array-calibration/readout file is archived.

## Build

Use a LaTeX distribution containing pdfLaTeX, BibTeX, latexmk, the standard
`article` class, and the packages used in `preamble.tex`, including
`fancyhdr` and `titlesec`. From the project directory, run:

```sh
make
```

The PDF is written to `output/pdf/main.pdf`. Compilation requires neither
shell escape nor network access.

## Reproducing the silicon band and valley figure

The band panel uses the actual HSE06 eigenvalues for silicon from NIST
JARVIS entry JVASP-1002, plotted along L–Γ–X with the valence-band maximum
set to zero energy. The companion panel is a schematic of the six valley
positions in crystal momentum space; it is not an additional band curve.

The input is saved locally at
`data/silicon-bandstructure/silicon_hse06_bands.json`, so regenerating the
figure requires no network access. With Python, NumPy, and Matplotlib
installed, run from the project directory:

```sh
python figures/generate_silicon_bands.py
```

The script writes `figures/silicon-band-valleys.pdf` for the LaTeX document
and `figures/silicon-band-valleys.png` for inspection. Run `make` afterwards
to include the regenerated PDF in the notes.

## Repository contents

- `main.tex`: article layout, document order, title, contents, and bibliography.
- `preamble.tex`: typography, packages, and notation.
- `sections/preface.tex`: introduction, notation, and general gate definitions.
- `sections/01-quantum-dots.tex`: section 1, quantum dots and confined electron states.
- `sections/02-electron-number.tex`: section 2, electron-number control and loading.
- `sections/03-qubit-encodings.tex`: section 3, single-spin, singlet–triplet, and exchange-only encodings.
- `sections/04-spin-control-exchange.tex`: section 4, Zeeman splitting, transverse driving, and exchange.
- `sections/05-initialization-readout.tex`: section 5, state preparation and spin readout.
- `sections/06-quantum-gates.tex`: section 6, physical implementations of quantum gates.
- `sections/07-coherence.tex`: section 7, dephasing, relaxation, and leakage.
- `sections/08-qubit-arrays.tex`: section 8, addressing, parallel operations, and communication.
- `sections/appendix-*.tex`: the 25 appendix entry files and the virtual-gates component.
- `figures/`: native LaTeX diagrams, generated plots, and their plotting scripts.
- `data/silicon-bandstructure/`: saved NIST JARVIS silicon band data used by the figure script.
- `references.bib`: bibliography.
- `output/pdf/main.pdf`: compiled notes.
