import os
from textnode import TextNode
from leafnode import LeafNode
from parent_node import ParentNode
from textnode import TextType
from markdown_to_html_node import markdown_to_html_node
from pathlib import Path

def main():
    src_dir = "static"
    dst_dir = "public"

    if os.path.exists(dst_dir):
        recursive_delete_files(os.path.abspath(dst_dir))
        print(f"Recursively deleted: {dst_dir}/")

    copy_recursive(src_dir, dst_dir)
    print("Static content copied successfully.")

    # Generate pages recursively from the content directory
    generate_pages_recursive(os.path.abspath("content"), os.path.abspath("template.html"), os.path.abspath("public"))
    

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
        if item.startswith("# "):
            return item[2:].strip()
    raise Exception("No header found")


# should take an abs path
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_content = ""
    template_content = ""

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
        else:
            raise Exception("Not a file! Please input a file's absolute path")
        
    else:
        raise Exception("File path does not exist")
    
    # Conversion
    html_node = markdown_to_html_node(markdown_content)
    html_string_conversion = html_node.to_html()
    title_of_page = extract_title(markdown_content)

    # Replace title and content in the TEMPLATE with the actual content
    replace_template = template_content.replace("{{ Title }}", title_of_page).replace("{{ Content }}", html_string_conversion)

    # Create destination directory if it doesn't exist
    dest_dir = os.path.dirname(dest_path)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(dest_path, "w") as static_site:
        static_site.write(replace_template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:  # Handle subdirectories recursively
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(from_path, template_path, dest_path)


if __name__ == "__main__":
    main()