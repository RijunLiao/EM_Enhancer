import os
import shutil
def download_map(emd_id,save_path):
    current_map_path = os.path.join(save_path, emd_id+ ".mrc")
    file_url = "ftp://ftp.ebi.ac.uk/pub/databases/emdb/structures/EMD-" + str(
                            emd_id) + "/map/emd_" + str(emd_id) + ".map.gz"
    root_path = os.getcwd()
    os.chdir(save_path)
    os.system("wget " + str(file_url))
    os.system("gzip -d emd_" + str(emd_id) + ".map.gz")
    os.chdir(root_path)
    # f_dst = os.path.join(save_path, str(key) + ".map")
    f_src = os.path.join(save_path, "emd_" + str(emd_id) + ".map")
    if os.path.exists(f_src):
        shutil.move(f_src, current_map_path)

