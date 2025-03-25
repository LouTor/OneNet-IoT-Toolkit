from ...src.tm_converter.adapters import *
from ...src.tm_converter.utils.file_utils import load_json
import json

src_data = load_json("tm-converter/tests/json_tms/v1.2.json")
dst_data = V30Adapter.from_intermediate(V12Adapter.to_intermediate(src_data))
print(f"{json.dumps(dst_data, ensure_ascii=False, indent=2)}\n{type(dst_data)}")
