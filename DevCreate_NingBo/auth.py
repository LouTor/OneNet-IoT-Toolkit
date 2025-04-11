import hashlib
import hmac
import urllib.parse
import base64
import time

def assemble_token(version, resource_name, expiration_time, signature_method, access_key):
    res = urllib.parse.quote(resource_name, safe='')
    sig = urllib.parse.quote(generator_signature(version, resource_name, expiration_time, access_key, signature_method), safe='')
    return f"version={version}&res={res}&et={expiration_time}&method={signature_method}&sign={sig}"

def generator_signature(version, resource_name, expiration_time, access_key, signature_method):
    message = f"{expiration_time}\n{signature_method}\n{resource_name}\n{version}"
    encrypted = hmac_encrypt(message, access_key, signature_method)
    return base64.b64encode(encrypted).decode()

def hmac_encrypt(message, key, algorithm):
    signing_key = base64.b64decode(key)
    algo = hashlib.sha1 if algorithm == 'sha1' else hashlib.md5
    hmac_object = hmac.new(signing_key, message.encode(), algo)
    return hmac_object.digest()

class SignatureMethod:
    SHA1 = 'sha1'
    MD5 = 'md5'
    SHA256 = 'sha256'


# 用户级(API)鉴权调用
def auth_usr(UID, usr_key):
    res = f'userid/{UID}'
    et = int(time.time()) + 30 * 24 * 3600  # 鉴权有效期时间戳
    version = '2020-05-29'  # 城市平台:2020-05-29 融合平台:2022-05-01
    method = SignatureMethod.SHA1
    token = assemble_token(version, res, et, method, usr_key)
    # print(f"Authorization: {token}")  # Debug
    return token


if __name__ == "__main__":
    UID = '37990'  # 右上角用户信息获取用户ID与key
    usr_key = '0113deac55c94b108e67af9cf266c6a1'
    print(auth_usr(UID, usr_key))
