import os
from textnode import TextNode
from leafnode import LeafNode
from parent_node import ParentNode
from textnode import TextType
from markdown_to_html_node import markdown_to_html_node

"""markdown_to_html_node(markdown) is a function that:

Takes a markdown string as input
Parses the markdown and converts it into an HTML node structure
Returns an HTML node object (not a string yet)"""


""".to_html() is a method that:

Is called on an HTML node object
Converts the HTML node structure into an actual HTML string
Returns the final HTML string that can be written to a file"""

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
            


# Extracts the header from the raw markdown
def extract_title(markdown):
    items = markdown.split("\n")
    for item in items:
        item = item.lstrip()
        if item[0:2].startswith("# "):
            item = item[2:].strip()
            return item
    raise Exception("No header found")


# should take an abs path
def generate_page(from_path, template_path, dest_path):

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown_content = ""
    template_content = ""

    # Should end with .md to convert
    if not from_path.rstrip().endswith(".md"):
        raise Exception("Markdown content must end with '.md'.")
    
    # Get markdown
    if os.path.exists(from_path):
        if os.path.isfile(from_path):
            with open(from_path) as md_file:
                markdown_content = md_file.read()
        else:
            raise Exception("Not a file! Please input a file's absolute path")
    else:
        raise Exception("File path does not exist")
    
    # Get template
    if os.path.exists(template_path):
        if os.path.isfile(template_path):
            with open(template_path) as temp_file:
                template_content = temp_file.read()

    # Conversion
    nodes = markdown_to_html_node(markdown_content)
    html_conversion = nodes.tohtml()
    return html_conversion






if __name__ == "__main__":
    main()