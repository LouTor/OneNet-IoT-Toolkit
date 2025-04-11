import logging
import requests
from config import Config
from auth import auth_usr


def send_request(row):
    payload = {
        "product_id": str(row['PID']),
        "device_name": str(row['devname'])
    }
    url = f"http://{Config.IP}:{Config.PORT}/common?action=CreateDevice&version=1"
    headers = {"Authorization": auth_usr(row['UID'], row['usr_key'])}

    resp = None
    try:
        resp = requests.post(url, json=payload, headers=headers)
        resp.raise_for_status()
        logging.info(f"成功：设备 {row['devname']}，状态码 {resp.status_code}，响应内容：{resp.text}")  # 新增响应内容记录
        return True
    except requests.exceptions.RequestException as e:
        error_msg = f"失败：设备 {row['devname']}，错误：{str(e)}"
        if hasattr(resp, 'status_code'):
            error_msg += f"，状态码：{resp.status_code}"
        else:
            error_msg += "，状态码：无"
        error_msg += f"，响应内容：{resp.text if resp else '无'}"
        logging.error(error_msg)
        return False
    except Exception as e:
        error_msg = f"失败：设备 {row['devname']}，未知错误：{str(e)}"
        error_msg += f"，响应内容：{resp.text if resp else '无'}"
        logging.error(error_msg)
        return False
