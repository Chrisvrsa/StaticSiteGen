from htmlnode import HTMLNode
from block_type import BlockType
from parent_node import ParentNode
from block_type import block_to_block_type
from markdown_to_blocks import markdown_to_blocks

def markdown_to_html_node(markdown):
    # returns a list of markdown blocks
    markdown_blocks = markdown_to_blocks(markdown)
    html_nodes = []

    for block in markdown_blocks:
        # returns an enum type
        block_type = block_to_block_type(block)

        match block_type:
            case BlockType.HEADING:
                # Keep count of each # in the header
                # valid_headers_list = ["# ", "## ", "### ", "#### ", "##### ", "###### "]
                count = 0
                first_elements = block[:6]

                for char in first_elements:
                    if char == "#":
                        count += 1
                if count == 1:
                    cleaned_value = block.replace("#", "").strip()
                    html_nodes.append(HTMLNode("h1", cleaned_value))
                elif count == 2:
                    # perhaps redundant. But what if they have a # as a value string? not to signify the header
                    cleaned_value = block.replace("##", "").strip()
                    html_nodes.append(HTMLNode("h2", cleaned_value))
                elif count == 3:
                    cleaned_value = block.replace("###", "").strip()
                    html_nodes.append(HTMLNode("h3", cleaned_value))
                elif count == 4:
                    cleaned_value = block.replace("####", "").strip()
                    html_nodes.append(HTMLNode("h4", cleaned_value))
                elif count == 5:
                    cleaned_value = block.replace("#####", "").strip()
                    html_nodes.append(HTMLNode("h5", cleaned_value))
                elif count == 6:
                    cleaned_value = block.replace("######", "").strip()
                    html_nodes.append(HTMLNode("h6", cleaned_value))
            
            case BlockType.CODE:
                # remove backticks from markdown, and pass it in as a value to the child html node.
                cleaned_code_block = block.replace("```", "")
                new_node = ParentNode("pre", [
                    HTMLNode("code", cleaned_code_block)
                    
                ])
                html_nodes.append(new_node)
            
            case BlockType.QUOTE:
                cleaned_code_quote = block.replace("> ", "").lstrip()
                html_nodes.append(HTMLNode("blockquote", cleaned_code_quote))

            case BlockType.UNORDERED_LIST:
                valid_unordered_list = ["* ", "- ", "+ "]
                li_nodes = []

                for section in block.split("\n"):
                    section = section.lstrip()
                    for marker in valid_unordered_list:
                        if section.startswith(marker):
                            content = section[len(marker):].lstrip()
                            li_nodes.append(HTMLNode("li", content))
                            break # only match the first matched marker     
                ul_node = ParentNode("ul", li_nodes)
                html_nodes.append(ul_node)      

            
                



                

