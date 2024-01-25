import os
import re
import requests
import sys
import markdown

def extract_plantuml_code_blocks(markdown_text):
    pattern = r'```plantuml\n(.*?)\n```'
    code_blocks = re.findall(pattern, markdown_text, re.DOTALL)
    return code_blocks

def generate_svg_from_plantuml(code, server_url):
    payload = {'text': code}
    response = requests.post(server_url, data=payload)
    if response.status_code == 200:
        return response.text
    else:
        return None

def insert_svg_into_markdown(svg, code_block, markdown_text):
    img_tag = f'\n\n![PlantUML generated image](assets/{code_block}.svg)\n\n'
    updated_text = markdown_text.replace(f'```plantuml\n{code_block}\n```', img_tag)
    return updated_text

def generate_svg_images_from_markdown(md_file, server_url):
    with open(md_file, 'r') as file:
        markdown_text = file.read()

    code_blocks = extract_plantuml_code_blocks(markdown_text)
    for code_block in code_blocks:
        svg = generate_svg_from_plantuml(code_block, server_url)
        if svg is not None:
            with open(f'assets/{code_block}.svg', 'w') as svg_file:
                svg_file.write(svg)
            markdown_text = insert_svg_into_markdown(svg, code_block, markdown_text)

    with open(md_file, 'w') as file:
        file.write(markdown_text)

if __name__ == '__main__':
    markdown_file_path = sys.argv[1]
    server_url = 'http://localhost:30057/svg/'
    generate_svg_images_from_markdown(markdown_file_path, server_url)
