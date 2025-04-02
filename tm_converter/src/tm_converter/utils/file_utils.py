import json
from pathlib import Path
from typing import Any


def load_json(file_path: str) -> Any:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise ValueError(f"文件不存在：{file_path}")
    except json.JSONDecodeError:
        raise ValueError("JSON文件格式错误")


def save_json(data: Any, file_path: str, indent: int = 2) -> None:
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)


def gain_path(path) -> str:
    """
    :param path:
    :return:
    file_name = os.path.splitext(os.path.basename(path))[0]  # 获取完整文件名元组的元素[0] 不含拓展名的文件名
    tm_converted_path = os.path.join(os.path.dirname(path), f"{self.ver}-{file_name}.json")
    """
    pass
