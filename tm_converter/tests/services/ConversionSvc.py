from tm_converter.src.tm_converter.utils.file_utils import load_json
from tm_converter.src.tm_converter.services.conversion_service import ConversionService

input_data = load_json("tm-converter/tests/json_tms/1.2.json")
output = ConversionService.convert(input_data, "1.2", "3.x")
print(output)
