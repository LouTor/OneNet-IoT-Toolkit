from ...src.tm_converter.services.version_detector import VersionDetector
from ...src.tm_converter.utils.file_utils import load_json

input_data = load_json("tm-converter/tests/json_tms/fuse.json")

src_version = VersionDetector.detect(input_data)
print(src_version)
