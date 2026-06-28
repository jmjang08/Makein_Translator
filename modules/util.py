import os


def load_glossary(file_path: str) -> dict:
    """용어집 로드"""
    # CSV 읽기
    glossary = {}
    if not os.path.exists(file_path):
        return glossary
    
    with open(file_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i == 0:
                continue  # 헤더 제외
            parts = line.strip().split(",")
            if len(parts) != 2:
                continue  # 잘못된 줄 제외
            src_term, tgt_term = parts
            glossary[src_term.strip()] = tgt_term.strip()
    
    return glossary
