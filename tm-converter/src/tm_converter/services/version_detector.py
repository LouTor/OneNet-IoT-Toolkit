# 自动版本检测
class VersionDetector:
    @staticmethod
    def detect(data: dict) -> str:
        # 根据特征检测版本
        if 'combs' in data:
            return "fuse"
        if 'stTmId' in data.get('profile', {}):
            return "2.x"
        if any(prop.get('functionType') == 'st' for prop in data.get('properties', [])):
            return "3.0"
        if any(service.get('callType') == 's' for service in data.get('services', [])):
            return "1.2"
        return "unknown"
