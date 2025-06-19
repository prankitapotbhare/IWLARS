# Noise filtering logic (placeholder) 

import open3d as o3d

def remove_noise(pcd, nb_neighbors=20, std_ratio=2.0):
    """
    Removes noise from a point cloud using statistical outlier removal.
    Returns the filtered point cloud.
    """
    cl, ind = pcd.remove_statistical_outlier(nb_neighbors=nb_neighbors, std_ratio=std_ratio)
    filtered_pcd = pcd.select_by_index(ind)
    return filtered_pcd 