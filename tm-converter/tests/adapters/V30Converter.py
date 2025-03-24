from ...src.tm_converter.adapters import V30Converter
from ...src.tm_converter.utils.file_utils import load_json

src_data = load_json("tm-converter/tests/json_tms/v3.0.json")
intermediate = V30Converter.to_intermediate(src_data)
