from tm_converter.src.tm_converter.services.version_detector import VersionDetector
from tm_converter.src.tm_converter.utils.file_utils import load_json

# 根据文件检测输入版本
input_data = load_json("../json_tms/fuse.json")
src_version = VersionDetector.detect(input_data)
print(src_version)

# 直接输入版本
src_version = VersionDetector.select("3.0")
print(src_version)