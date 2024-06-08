import h5py

# Path to your DREAM.3D file
file_path = 'path/to/your/file.dream3d'

# Open the file
with h5py.File(file_path, 'r') as file:
    # List all groups
    print("Keys: %s" % file.keys())
    # Assuming you know the path to the dataset you need
    data_path = 'DataContainer/SomeGroup/SomeDataset'
    if data_path in file:
        data = file[data_path][()]
        print(data)
    else:
        print("Dataset not found in the file.")
