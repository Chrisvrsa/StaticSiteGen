from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown_block_text):
    valid_headers_list = ["# ", "## ", "### ", "#### ", "##### ", "###### "]
    valid_unordered_list = ["* ", "- ", "+ "]

    for valid_header in valid_headers_list:
        if markdown_block_text.startswith(valid_header):
            return BlockType.HEADING
        
    if markdown_block_text.startswith("```") and markdown_block_text.endswith("```"):
        return BlockType.CODE
    
    elif markdown_block_text.startswith(">"):
        split_sections = markdown_block_text.split("\n")
        split_sections_len = len(split_sections)
        tally = 0

        for section in split_sections:
            if section.startswith(">"):
                tally += 1
        if tally == split_sections_len:
            return BlockType.QUOTE
            
                
    elif markdown_block_text[:2] in valid_unordered_list:
        split_sections = markdown_block_text.split("\n")
        split_sections_len = len(split_sections)
        tally = 0

        for section in split_sections:
            for character in valid_unordered_list:
                if section.lstrip().startswith(character):
                    tally += 1
                    break  # Stop checking after first match

        if tally == split_sections_len:
            return BlockType.UNORDERED_LIST
        
    elif markdown_block_text.startswith("1. "):
        split_sections = markdown_block_text.split("\n")
        tally = 0

        for index, item in enumerate(split_sections):
            count = index + 1
            if item.startswith(f"{count}. "):
                tally += 1
        if len(split_sections) == tally:
            return BlockType.ORDERED_LIST   
    # final case
    else:
        return BlockType.PARAGRAPH

    




