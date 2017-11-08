# Import PCL module
import pcl

# Load Point Cloud file
cloud = pcl.load_XYZRGB('tabletop.pcd')

# Create a VoxelGrid filter object for our input point cloud
vox = cloud.make_voxel_grid_filter()

# Voxel Grid filter
# Note: this (1) is a poor choice of leaf size   
# Experiment and find the appropriate size!
LEAF_SIZE = 0.01   

# Set the voxel (or leaf) size  
vox.set_leaf_size(LEAF_SIZE, LEAF_SIZE, LEAF_SIZE)

# Extract inliers
# RANSAC plane segmentation
cloud_filtered = vox.filter()
filename = 'voxel_downsampled.pcd'

# Save pcd for table
# pcl.save(cloud, filename)
pcl.save(cloud_filtered, filename)

# PassThrough filter
# Create a PassThrough filter object.
passthrough = cloud_filtered.make_passthrough_filter()

# Assign axis and range to the passthrough filter object.
filter_axis = 'z'
passthrough.set_filter_field_name(filter_axis)
axis_min = 0.6
axis_max = 1.1
passthrough.set_filter_limits(axis_min, axis_max)

# Extract outliers
# Finally use the filter function to obtain the resultant point cloud. 
cloud_filtered = passthrough.filter()
filename = 'pass_through_filtered.pcd'

# Save pcd for tabletop objects
pcl.save(cloud_filtered, filename)
