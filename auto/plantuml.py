import os
import re
import hashlib
import requests
import markdown
import urllib.parse
import zlib
import base64
import shutil

def extract_plantuml_code_blocks(markdown_text):
    pattern = r'```plantuml\n(.*?)\n```'
    code_blocks = re.findall(pattern, markdown_text, re.DOTALL)
    return code_blocks

def generate_md5_hash(text):
    md5_hash = hashlib.md5()
    md5_hash.update(text.encode('utf-8'))
    return md5_hash.hexdigest()

def generate_svg_from_plantuml(code_block, server_url):
    # 将文本以UTF-8编码
    encoded_text = code_block.encode('utf-8')
    # 使用Deflate算法进行压缩
    compressed_text = zlib.compress(encoded_text)
    # 将压缩后的文本重新编码为ASCII，并使用类似Base64的字符映射
    encoded_ascii = base64.b64encode(compressed_text).decode('ascii')
    # 由于字符映射的顺序不同，需要进行字符替换
    encoded_plantuml = encoded_ascii.translate(str.maketrans(
        'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/',
        '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
    ))
    plantuml_url = f'{server_url}/svg/{encoded_plantuml}'
    response = requests.get(plantuml_url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def encode_plantuml(data):
    encoding_table = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"
    encoded_data = ""
    for b in data:
        encoded_data += encoding_table[(b >> 4) & 0x0F]
        encoded_data += encoding_table[b & 0x0F]
    return encoded_data

def insert_svg_into_markdown(svg, code_block, markdown_text, asset_filename):
    img_tag = f'![plantuml](./plantuml/{asset_filename}.svg)'
    updated_text = markdown_text.replace(f'```plantuml\n{code_block}\n```', img_tag)
    return updated_text

def generate_svg_images_from_markdown(src_file_path, new_file_path, server_url):
    with open(src_file_path, 'r') as file:
        markdown_text = file.read()
    assets_directory = f'{os.path.dirname(src_file_path)}/plantuml'
    if os.path.exists(assets_directory):
        shutil.rmtree(assets_directory)

    code_blocks = extract_plantuml_code_blocks(markdown_text)
    for code_block in code_blocks:
        md5_hash = generate_md5_hash(code_block)
        asset_filename = f'{md5_hash}'
        svg = generate_svg_from_plantuml(code_block, server_url)
        if svg is not None:
            if not os.path.exists(assets_directory):
                os.makedirs(assets_directory)
            asset_path = f'{assets_directory}/{asset_filename}.svg'
            if os.path.exists(asset_path):
                os.remove(asset_path)
            with open(asset_path, 'w') as svg_file:
                svg_file.write(svg)
            markdown_text = insert_svg_into_markdown(svg, code_block, markdown_text, asset_filename)

    with open(new_file_path, 'w') as file:
        file.write(markdown_text)

def process_raw_files(directory, server_url):
    # 遍历目录下的所有文件和文件夹
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.raw.md'):
                # 构造文件的完整路径
                src_file_path = os.path.join(root, file)
                # 获取移除.raw字样后的新路径
                # 获取文件名和目录
                directory, filename = os.path.split(src_file_path)
                # 构造新的路径
                new_file_path = os.path.join(directory, filename.replace('.raw', ''))
                generate_svg_images_from_markdown(src_file_path, new_file_path, server_url)

def check_service_readiness(server_url):
    response = requests.get(server_url)
    if response.status_code >= 200 and response.status_code < 400:
        pass
    else:
        raise Exception("The PlantUML server is not ready")

if __name__ == '__main__':
    import sys
    server_url = 'http://127.0.0.1:30057'
    directory = sys.argv[1]
    try:
        check_service_readiness(server_url)
        process_raw_files(directory, server_url)
    except Exception as e:
        print(str(e))
