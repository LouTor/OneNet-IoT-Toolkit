from tm_converter.src.tm_converter.utils.file_utils import load_json
from tm_converter.src.tm_converter.services.conversion_service import ConversionService


# 测试接口
def test_v3_conversion():
    input_data = load_json("tm-converter/tests/json_tms/1.2.json")
    output = ConversionService.convert(input_data, "1.2", "3.x")
    print(output)


test_v3_conversion()
