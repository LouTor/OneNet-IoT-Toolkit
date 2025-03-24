# 测试用例

from ..src.tm_converter.utils.file_utils import load_json
from ..src.tm_converter.services.conversion_service import ConversionService


# 测试接口
def test_v3_conversion():
    input_data = load_json("../json_tms/v3.0.json")
    output = ConversionService.convert(input_data, "2.x")
    assert 'stTmId' in output['profile']


test_v3_conversion()
