import os
from textnode import TextNode
from leafnode import LeafNode
from parent_node import ParentNode
from textnode import TextType


def main():
    src_dir = "static"
    dst_dir = "public"

    if os.path.exists(dst_dir):
        recursive_delete_files(os.path.abspath(dst_dir))
        print(f"Recursively deleted: {dst_dir}/")

    copy_recursive(src_dir, dst_dir)
    print("Static content copied successfully.")


def recursive_delete_files(path):
    if not os.path.exists(path):
        return

    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        if os.path.isdir(item_path):
            recursive_delete_files(item_path)
        else:
            os.remove(item_path)

    os.rmdir(path)


def copy_recursive(src, dst):
    if os.path.isdir(src):
        if not os.path.exists(dst):
            os.mkdir(dst)
            print(f"Created directory: {dst}")

        for item in os.listdir(src):
            src_path = os.path.join(src, item)
            dst_path = os.path.join(dst, item)
            copy_recursive(src_path, dst_path)
    else:
        with open(src, 'rb') as f_src:
            with open(dst, 'wb') as f_dst:
                f_dst.write(f_src.read())
            print(f"Copied file: {src} -> {dst}")


if __name__ == "__main__":
    main()