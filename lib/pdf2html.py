import os
import subprocess

def pdf_to_html(pdf_path, output_dir='output',pdf2htmlEX=""):
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    basename = os.path.basename(pdf_path)
    html_output = os.path.join(output_dir, basename+'.html')
    subprocess.run([pdf2htmlEX, pdf_path, html_output])
     
    return html_output
