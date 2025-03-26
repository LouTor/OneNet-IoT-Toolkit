from .base_converter import BaseConverter


class V30Adapter(BaseConverter):
    @classmethod
    def from_intermediate(cls, intermediate):
        output = intermediate.model_dump()
        cls.func_type(output, "st")
        cls.desc(output, "ept")
        cls.call_type(output, "full")
        return output


class V2xAdapter(BaseConverter):
    @classmethod
    def from_intermediate(cls, intermediate):
        output = intermediate.model_dump()
        cls.func_type(output, "u")
        cls.desc(output, "ept")
        cls.call_type(output, "full")
        return output


class V12Adapter(BaseConverter):
    @classmethod
    def from_intermediate(cls, intermediate):
        output = intermediate.model_dump()
        cls.func_type(output, "u")
        cls.desc(output, "null")
        cls.step(output, "null")
        cls.call_type(output, "simp")
        cls.func_mode(output)
        cls.length_str(output)
        return output


class FuseAdapter(BaseConverter):
    @classmethod
    def from_intermediate(cls, intermediate):
        output = intermediate.model_dump()
        cls.func_type(output, "u")
        cls.call_type(output, "full")
        return output
