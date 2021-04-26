#!/usr/bin/env python3
import numpy as np
import laspy as lp

input_path = "./"
output_path = "./"

def pc_lidar():
  dataname = "NZ19_Wellington"
  point_cloud = lp.file.File(input_path+dataname+".las", mode="r")

  points = np.vstack((point_cloud.x, point_cloud.y, point_cloud.z)).transpose()
  colors = np.vstack((point_cloud.red, point_cloud.green,
                    point_cloud.blue)).transpose()

  voxel_size=6
  nb_vox=np.ceil((np.max(points, axis=0) - np.min(points, axis=0))/voxel_size)

  non_empty_voxel_keys, inverse, nb_pts_per_voxel= np.unique(((points - np.min(points, axis=0)) // voxel_size).astype(int), axis=0, return_inverse=True, return_counts=True)
  idx_pts_vox_sorted=np.argsort(inverse)
  voxel_grid={}
  grid_barycenter,grid_candidate_center=[],[]
  last_seen=0

  for idx,vox in enumerate(non_empty_voxel_keys):
    voxel_grid[tuple(vox)]=points[idx_pts_vox_sorted[last_seen:last_seen+nb_pts_per_voxel[idx]]]
    grid_barycenter.append(np.mean(voxel_grid[tuple(vox)],axis=0))
    grid_candidate_center.append(voxel_grid[tuple(vox)][np.linalg.norm(voxel_grid[tuple(vox)]-np.mean(voxel_grid[tuple(vox)],axis=0),axis=1).argmin()])
    last_seen+=nb_pts_per_voxel[idx]
    
  np.savetxt(output_path+dataname+"_voxel-best_point_%s.xyz" % (voxel_size), grid_candidate_center, delimiter=" ", fmt="%1.15f")

if __name__ == "__main__":
  pc_lidar()