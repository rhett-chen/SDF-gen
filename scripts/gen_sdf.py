import os
import argparse


def generate_sdf(sdfgen_path, obj_path, dim=100, padding=5):
    """
    Args:
        sdfgen_path: [str], sdfgen executable file path. refer to README.md
        obj_path: str, .obj mesh file path
        dim: int, 3D grid shape, dim*dim*dim, for GraspNet1-billion dataset, default is 100
        padding: int, for GraspNet1-billion dataset, default is 5
    Returns:
    """
    sdfgen_cmd = "{} {} {} {}".format(sdfgen_path, obj_path, dim, padding)
    os.system(sdfgen_cmd)


def batch_generate_sdf(sdfgen_path, objects_path, objects_name_list):
    """
    Args:
        sdfgen_path: str, /path/to/sdfgen_executable_file.
        objects_path: str, /path/to/object/models.
        objects_name_list: str, object name list .txt file path, each row in .txt file is a object name.

    """
    with open(objects_name_list, 'r') as t:
        objects = t.readlines()
        objects = [obj.strip() for obj in objects]

    for obj in objects:
        generate_sdf(
            sdfgen_path=sdfgen_path,
            obj_path='{}/{}/textured.obj'.format(objects_path, obj),
        )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate sdf base on .obj mesh file")
    parser.add_argument('--sdfgen_path', type=str, help="/path/to/SDF-gen/build/bin/sdf_gen")
    parser.add_argument('--objects_path', type=str, help="/path/to/objects_directory")
    parser.add_argument('--objects_name_path', type=str, help="/path/to/objects_name_list, a txt file")
    args = parser.parse_args()

    print("!!! We assume that the names of all .obj files are 'textured' !!!")
    batch_generate_sdf(args.sdfgen_path, args.objects_path, args.objects_name_path)
