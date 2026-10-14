from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET
import json, csv, hashlib, math
base=Path(__file__).resolve().parent
xml=base/'JVASP-1002.xml'
r=ET.parse(xml).getroot()
h=r.find('main_hse06_band/main_hse_bands_info')
def text(key): return h.findtext(key).strip('"')
def rows(key): return [[float(v) for v in row.split(',')] for row in text(key).split(';')]
eup=rows('spin_up_bands_y'); edn=rows('spin_down_bands_y')
labels=text('kp_labels').split(','); ticks=[int(x) for x in text('kp_labels_points').split(',')]
assert len(eup)==32 and len(eup[0])==193 and all(len(x)==193 for x in eup)
spin_difference=max(abs(x-y) for a,b in zip(eup[:8],edn[:8]) for x,y in zip(a[29:],b[29:]))
# The original XML x values are integer sample indices, not Cartesian k distances.
x=rows('spin_up_bands_x'); assert all(row==list(range(193)) for row in x)
start=29
z=ZipFile(base/'opt-band.zip'); kp=z.read('KPOINTS').decode().splitlines()
assert int(kp[1])==164
krows=[line.split() for line in kp[3:]]
coords=[[float(x) for x in row[:3]] for row in krows]
labels_opt=[]; ticks_opt=[]
for i,row in enumerate(krows):
 if len(row)==5 and (not labels_opt or row[4]!=labels_opt[-1]):
  labels_opt.append(row[4]);ticks_opt.append(i)
assert labels_opt==labels[1:] and ticks_opt==[i-start for i in ticks[1:]]
# HSE native coordinates are absent: these coordinates are an explicitly inferred mapping,
# imported from the same material's official optB88-vdW KPOINTS, whose count and all labels match.
for i in range(24):
 for a,b in zip(coords[i],coords[23]): assert abs(a-(i/23)*b)<1e-10
vbm=max(eup[n][k] for n in range(4) for k in range(start,193))
cbm=min((eup[n][k],n,k) for n in range(4,32) for k in range(start,193))
gamma=29; X=52
source_hash=hashlib.sha256(xml.read_bytes()).hexdigest()
path_energies=[[row[k] for row in eup] for k in range(start,193)]
meta={
 'material':'Bulk diamond silicon (Si), space group Fd-3m (227)',
 'database_id':'JVASP-1002', 'calculation':'VASP HSE06 hybrid-functional electronic band structure',
 'energy_unit':'eV', 'native_energy_reference':'E minus Fermi energy (E_F)',
 'native_reference_note':'NIST material page states energies shifted to E_F=0; official jarvis/db/vasp_to_xml.py ebandstruct subtracts vrun.efermi.',
 'native_fermi_absolute_energy_eV':None,
 'raw_xml_sha256':source_hash,
 'raw_xml_url':'https://www.ctcms.nist.gov/~knc6/static/JARVIS-DFT/JVASP-1002.xml',
 'material_page_url':'https://www.ctcms.nist.gov/~knc6/jsmol/JVASP-1002.html',
 'parser_source_url':'https://raw.githubusercontent.com/usnistgov/jarvis/master/jarvis/db/vasp_to_xml.py',
 'kpoints_source_url':'https://ndownloader.figshare.com/files/23713301',
 'kpoints_source_sha256':hashlib.sha256((base/'opt-band.zip').read_bytes()).hexdigest(),
 'kpoints_caveat':'Original HSE XML stores only sample indices and high-symmetry labels. Inferred fractional reciprocal coordinates copied from same material official optB88-vdW band KPOINTS: all 12 label indices and the 164-point length exactly match the HSE path after its first 29 points. HSE original KPOINTS was not supplied by XML download links.',
 'kpoints_coordinate_system':'Fractional coordinates in reciprocal primitive-lattice basis, inferred mapping as above. No actual Cartesian HSE k coordinates claimed.',
 'hse_xml_leading_nonpath_points':29,
 'path_first_native_zero_based_index':29,
 'native_indices':list(range(start,193)),
 'native_shape_bands_by_samples':[32,193],
 'path_shape_samples_by_bands':[164,32],
 'spins':'Spin-up data retained. Lowest eight path bands coincide within numerical precision (see difference); high unoccupied bands show larger convergence differences.',
 'lowest_eight_path_bands_max_spin_difference_eV':spin_difference,
 'n_occupied_bands_per_spin':4,
 'vbm_minus_fermi_eV':vbm,
 'cbm_minus_fermi_eV':cbm[0],
 'path_indirect_gap_eV':cbm[0]-vbm,
 'gamma_direct_gap_eV':eup[4][gamma]-eup[3][gamma],
 'reported_xml_indirect_gap_eV':float(text('band_indir_gap')),
 'reported_xml_direct_gap_eV':float(text('band_dir_gap')),
 'reported_material_page_hse_gap_eV':1.216,
 'gamma_native_zero_based_index':gamma,
 'X_native_zero_based_index':X,
 'CBM_native_zero_based_index':cbm[2],
 'CBM_band_zero_based_index':cbm[1],
 'CBM_gamma_X_fraction_sampled':(cbm[2]-gamma)/(X-gamma),
 'CBM_note':'Sampled minimum, no extremum fitting or band-gap correction applied.',
 'lattice_parameter_conventional_angstrom_reported_page':5.494,
 'opt_band_direct_primitive_lattice_angstrom':[[float(x) for x in row.split()] for row in z.read('POSCAR').decode().splitlines()[2:5]],
 'lattice_parameter_caveat':'Material page describes optB88-vdW relaxed structure; HSE-specific relaxation not independently documented in downloaded XML.',
 'license_url':'https://www.nist.gov/copyrights-disclaimers',
 'license_note':'NIST information is public information and may be distributed/copied unless marked copyrighted; appropriate source credit requested. No separate copyright mark was found on this material record.',
 'retrieved_date':'2026-10-10'
}
data={
 'metadata':meta,
 'path_labels':[{'label':label,'index':idx-start,'native_zero_based_index':idx} for label,idx in zip(labels[1:],ticks[1:])],
 'native_sample_index':list(range(start,193)),
 'fractional_reciprocal_coordinates_inferred':coords,
 'energies_minus_fermi_eV':path_energies,
 'energies_minus_vbm_eV':[[value-vbm for value in row] for row in path_energies]
}
(base/'silicon_hse06_bands.json').write_text(json.dumps(data,indent=2)+'\n')
with (base/'silicon_hse06_bands.csv').open('w',newline='') as f:
 w=csv.writer(f)
 w.writerow(['path_index','native_zero_based_index','k1_inferred','k2_inferred','k3_inferred']+[f'band_{n+1}_minus_VBM_eV' for n in range(32)])
 for j,row in enumerate(data['energies_minus_vbm_eV']): w.writerow([j,j+start,*coords[j],*row])
(base/'silicon_hse06_metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
print('Saved JSON/CSV and metadata.',json.dumps({k:meta[k] for k in ['raw_xml_sha256','path_shape_samples_by_bands','vbm_minus_fermi_eV','path_indirect_gap_eV','gamma_direct_gap_eV','CBM_gamma_X_fraction_sampled']}))
