# 基础镜像（Windows GUI需特殊处理）
FROM python:3.10-slim

# 复制代码
COPY iot-converter/ /app/iot-converter
COPY shared-libs/ /app/shared-libs

# 安装依赖
RUN pip install --no-cache-dir -r /app/iot-converter/requirements.txt

# 解决Linux GUI问题（可选）
ENV DISPLAY=:0

# 入口命令
CMD ["python", "-m", "iot_converter.main"]