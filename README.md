# SDF-gen
## Installation
Compile sdf generator
```shell
cd SDF-gen
mkdir build && cd build && cmake ..
make
```
## Usage
You need to specify the object 3D .obj file path (/path/to/object_obj_file), the dimension (dim, an integer) and the padding (pad, an integer). The generated sdf file and the given obj file are in the same directory and have the same name. The shape of the sdf data is dim\*dim\*dim. 
```shell
cd build/bin/
sdf_gen /path/to/object_obj_file dim pad
```
You can also generate sdf files in batch by running the python scripts. It will generate SDF files for all objects on the objects_name list. The object model library should be organized as follows:
* object_dir
  * object_name1
    * textured.obj
    * textured.mtl
    * ...
  * object_name2
  * ...
```shell
cd scripts
python gen_sdf.py --sdfgen_path /path/to/SDF-gen/build/bin/sdf_gen --objects_path /path/to/object_dir --objects_name_path /path/to/objects_name_list
```