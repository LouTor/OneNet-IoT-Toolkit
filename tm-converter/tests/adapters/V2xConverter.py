from ...src.tm_converter.adapters import V21Adapter
from ...src.tm_converter.utils.file_utils import load_json

src_data = load_json("tm-converter/tests/json_tms/v3.0.json")
intermediate = V30Converter.to_intermediate(src_data)
# print(intermediate)

dst_data = V30Converter.from_intermediate(intermediate)
print(f"{dst_data}\n{type(dst_data)}")
