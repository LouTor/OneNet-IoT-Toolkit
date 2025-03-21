# 测试用例
from utils.file_utils import load_json
from services.conversion_service import ConversionService

def test_v3_conversion():
    input_data = load_json("../json_tms/v3.0.json")
    output = ConversionService.convert(input_data, "2.x")
    assert 'stTmId' in output['profile']

test_v3_conversion()
