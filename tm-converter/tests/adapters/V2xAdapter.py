from ...src.tm_converter.adapters import V2xAdapter
from ...src.tm_converter.utils.file_utils import load_json

src_data = load_json("tm-converter/tests/json_tms/v3.0.json")
intermediate = V2xAdapter.to_intermediate(src_data)
# print(intermediate)

dst_data = V2xAdapter.from_intermediate(intermediate)
print(f"{dst_data}\n{type(dst_data)}")
