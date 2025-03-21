# 数据校验器
class SchemaValidator:
    @staticmethod
    def validate_intermediate(model: IntermediateModel):
        # 校验中间模型
        for prop in model.properties:
            if prop.dataType.type == 'struct':
                if not isinstance(prop.dataType.specs, list):
                    raise ValueError("Struct specs must be array")
            elif prop.dataType.type == 'array':
                if 'specs' in prop.dataType.specs:
                    raise ValueError("Array specs should not have nested specs")

class VersionCompatibility:
    @staticmethod
    def check_compatibility(source_ver, target_ver):
        # 检查版本兼容性逻辑
        incompatible_pairs = [('1.0', '3.0'), ('3.0', '1.2')]
        if (source_ver, target_ver) in incompatible_pairs:
            raise ValueError(f"Direct conversion from {source_ver} to {target_ver} not supported")