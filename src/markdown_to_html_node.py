from htmlnode import HTMLNode
from block_type import BlockType
from parent_node import ParentNode
from block_type import block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from text_node_to_html_node import text_node_to_html_node
from text_to_textnodes import text_to_textnodes
from leafnode import LeafNode

def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    html_nodes = []

    for block in markdown_blocks:
        block_type = block_to_block_type(block)

        match block_type:
            case BlockType.HEADING:
                count = 0
                first_elements = block[:6]

                for char in first_elements:
                    if char == "#":
                        count += 1
                if 1 <= count <= 6:
                    cleaned_value = block[count+1:].strip()
                    text_nodes = text_to_textnodes(cleaned_value)
                    html_children = [text_node_to_html_node(node) for node in text_nodes]
                    html_nodes.append(ParentNode(f"h{count}", html_children))
            
            case BlockType.CODE:
                cleaned_code_block = block.replace("```", "")
                new_node = ParentNode("pre", [
                    LeafNode("code", cleaned_code_block)
                ])
                html_nodes.append(new_node)
            
            case BlockType.QUOTE:
                block_split = block.split("\n")
                list_of_cleaned_sections = []

                for section in block_split:
                    if section.startswith("> "):
                        cleaned = section[2:].lstrip()
                    else:
                        cleaned = section.lstrip()
                    list_of_cleaned_sections.append(cleaned)

                joined_quote = "\n".join(list_of_cleaned_sections).strip()
                text_nodes = text_to_textnodes(joined_quote)
                html_children = [text_node_to_html_node(node) for node in text_nodes]
                html_nodes.append(ParentNode("blockquote", html_children))

            case BlockType.UNORDERED_LIST:
                valid_unordered_list = ["* ", "- ", "+ "]
                li_nodes = []

                for section in block.split("\n"):
                    section = section.lstrip()
                    if section != "":
                        for marker in valid_unordered_list:
                            if section.startswith(marker):
                                content = section[len(marker):].lstrip()
                                text_nodes = text_to_textnodes(content)
                                html_children = [text_node_to_html_node(node) for node in text_nodes]
                                li_nodes.append(ParentNode("li", html_children))
                                break
                html_nodes.append(ParentNode("ul", li_nodes))

            case BlockType.ORDERED_LIST:
                li_values = block.split("\n")
                li_nodes = []

                for value in li_values:
                    value = value.lstrip()
                    if value != "":
                        first_space = value.find(' ')
                        if first_space != -1 and value[:first_space].endswith('.'):
                            extract_value = value[first_space+1:]
                        else:
                            extract_value = value

                        text_nodes = text_to_textnodes(extract_value)
                        html_children = [text_node_to_html_node(node) for node in text_nodes]
                        li_nodes.append(ParentNode("li", html_children))

                ol_node = ParentNode("ol", li_nodes)
                html_nodes.append(ol_node)

            case BlockType.PARAGRAPH:
                text_nodes = text_to_textnodes(block)
                html_children = [text_node_to_html_node(node) for node in text_nodes]
                html_nodes.append(ParentNode("p", html_children))

    return ParentNode("div", html_nodes)