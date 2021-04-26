#!/usr/bin/env python3
import numpy as np
import open3d as o3d

def pointcloud_to_3d():
    input_path = "./"
    output_path = "./"
    dataname = "NZ19_Wellington_voxel-best_point_6.xyz"
    point_cloud = np.loadtxt(input_path+dataname, skiprows=1)

    # The following command first instantiates the Open3d point cloud object
    # then add points, color and normals to it from the original NumPy array.

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(point_cloud[:, :3])
    #pcd.colors = o3d.utility.Vector3dVector(point_cloud[:, 3:6]/255)
    #pcd.normals = o3d.utility.Vector3dVector(point_cloud[:,6:9])
    o3d.visualization.draw_geometries([pcd])

if __name__ == "__main__":
    pointcloud_to_3d()