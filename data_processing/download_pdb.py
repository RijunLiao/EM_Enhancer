import os
def download_cif(download_dir,pdb_id):
    root_dir=os.getcwd()
    os.chdir(download_dir)
    # if not os.path.exists(download_dir, pdb_id+".cif"):
    os.system("wget https://files.rcsb.org/download/%s.cif"%(pdb_id))
    os.chdir(root_dir)
def download_pdb(download_dir,pdb_id):
    root_dir=os.getcwd()
    os.chdir(download_dir)
    # if not os.path.exists(download_dir, pdb_id+".cif"):
    os.system("wget https://files.rcsb.org/download/%s.pdb"%(pdb_id))
    os.chdir(root_dir)

