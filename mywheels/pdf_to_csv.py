import os
import pandas as pd
import pdfplumber as pdf


def read_files(path: str, lists=[]) -> list:
    file_list = os.listdir(path)
    for f in [os.path.join(path, f) for f in file_list]:
        if os.path.isfile(f):
            lists.append(f)
        elif os.path.isdir(f):
            read_files(f, lists)
        else:
            pass
    return lists


def read_pdf(pdf_path: str) -> list:
    pdf_data = pdf.open(pdf_path)
    return pdf_data.pages


def extract_table(page) -> pd.DataFrame:
    table = page.extract_table()
    df_data = pd.DataFrame(table)
    return df_data


def extract_text(page) -> str:
    """从pdf中提取 document"""
    text = page.extract_text()
    return text


def save_csv(data: pd.DataFrame, path: str) -> None:
    data.to_csv(
        path, mode='a', index=False, encoding='sig-utf8',
        header=not os.path.exists(path)
        )
    return None


def main(path: str, save_name: str):
    save_path = os.path.join(path, save_name)
    file_list = read_files(path)
    print(f'总共 {len(file_list)} 个文件')

    for i, file in enumerate(file_list):
        page_list = read_pdf(file_list[0])
        print(f"{file} 共 {len(page_list)} 页")

        for page in page_list:
            data = extract_table(page)
            save_csv(data, save_path)
        print(f'完成第 {i+1} 个文件')


if __name__ == '__main__':
    """
    说明：从pdf中提取表格，并保存到scv中
    path: 存放pdf 文件的文件目录 
    save_name: csv文件名，存放位置与pdf位置相同
    """
    path = r'others\pdf_to_csv\科技型中小企业名单'
    save_name = 'all_company.csv'
    main(path, save_name)
