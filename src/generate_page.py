

from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    """
    Extracts the first heading from the markdown content to use as the page title.
    
    Args:
        markdown (str): The markdown content.
    
    Returns:
        str: The title extracted from the first heading.
    """
    lines = markdown.split("\n")
    heading = ""
    ret_lines = []
    for line in lines:
        if line.startswith("# "):
            heading = "<h1>" + line[2:].strip() + "</h1>" # Return the text after the first '# '
        else:
            ret_lines.append(line)
    if heading:
        return heading, "\n".join(ret_lines)
    raise ValueError("No heading found in markdown content")

def generate_page(from_path, template_path, dest_path, basepath):
    """
    Generates a page by reading content from a markdown file, processing it,
    and writing the output to a specified destination path using a template.
    
    Args:
        from_path (str): Path to the markdown file to read.
        template_path (str): Path to the template file to use.
        dest_path (str): Path where the generated HTML file will be saved.
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as f:
        content = f.read()

    with open(template_path, 'r') as f:
        template = f.read()

    try:
        #title, content = extract_title(content)
        title, content2 = extract_title(content)
    except ValueError as e:
        raise ValueError(f"Error extracting title from {from_path}: {e}")
    html_node = markdown_to_html_node(content)
    html_content = html_node.to_html()
    template = template.replace("{{ Title }}", title)
    #print(title)
    template = template.replace("{{ Content }}", html_content).replace('href=\"', f'href="{basepath}').replace('src=\"', f'src="{basepath}')

    with open(dest_path, 'w') as f:
        f.write(template)
    