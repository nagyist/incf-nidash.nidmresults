# Example: reading a NIDM pack available on NeuroVault
import os
import json
import shutil
import tempfile
import nidmresults as nidm
import urllib.request

# Download the NIDM pack locally
nidm_url = 'https://neurovault.org/collections/2210/fsl_default_130.nidm.zip'
nidmpack = "2210_fsl_default_130.nidm.zip"

if not os.path.isfile(nidmpack):
    print('Downloading ' + nidmpack)
    urllib.request.urlretrieve(nidm_url, nidmpack)
 
# Known issues with NIDM packs in collection 2210
to_replace = {
    ' \\ntask': '\\\\n task',
    ';\n    nidm_coordinateVectorInVoxels: "null"^^xsd:string .':
    '.'}

# Read the NIDM pack
nres = nidm.load(nidmpack, to_replace=to_replace)

print(json.dumps(nres.get_info(), indent=4))
