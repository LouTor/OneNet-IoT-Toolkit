from ....src.tm_converter.core.converters.adapters import *
from ....src.tm_converter.utils.file_utils import load_json
import json


src_data = load_json("tm-converter/tests/json_tms/v1.2.json")
intermediate = FuseAdapter.to_intermediate(src_data)
# print(f"{intermediate.model_dump()}\n")
dst_data = FuseAdapter.from_intermediate(intermediate)
print(f"{json.dumps(dst_data, ensure_ascii=False, indent=2)}\n{type(dst_data)}")
