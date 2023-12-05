# blender_decimate_modifier
Decimate modifier script that decimates models in a directory and overwrites them after decimating to the given ratio.

# Steps to decimate models

**Note**: Currently tested only on **.dae** models and using **Collapse** decimation type on **bpy 3.6**

1. Install python >= 3.10
2. Create a virtual environment (required only if you have multiple python version)
    > python3.10 -m venv blender_ws
3. Source the venv
    > cd blender_ws
    > source ./bin/activate
4. Create directories scripts, wheels and download [bpy 3.6](https://pypi.org/project/bpy/3.6.0/#files) and place it in the wheels directory
    > mkdir wheels
5. Then install the wheel in venv
    > cd wheels

    > pip install wheels/bpy-3.6.0-cp310-cp310-manylinux_2_28_x86_64.whl

Once you've completed the installation, place the decimate modifier script in the scripts directory.

**Change the below mentioned variables according to your needs**

`decimate_ratio`, `min_number_of_faces`, `path_to_model_directory` 

**decimate_ratio** - The ratio in which the model must be decimated.

**min_number_of_faces** - The minimum number of faces a model should have if it's to be decimated (just to preserve the model's shape)

**path_to_model_directory** - The path to the directory containing the .dae models.
1. The scripts will search for all the .dae files in the given directory
2. ### Caution: The script overwrites on the same path after decimating the model so if you need your original models make sure you have a copy of it.

# Running the script

1. Once above steps are completed go the the scripts directory and execute the following command.

    > blender -b -P decimate_models.py

Once completed your models should be decimated and placed in the same location.


# Support

1. Please open an issue if found any.








