# -*- coding:utf-8 -*-

import requests
import json
import os
try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO

ata_url = "https://ata.360.cn/api/v1/task/submit"
token = "1c2VyX2lkIjo4MCwidXNlcm5hbWUiOiJBVEFcdTZjOTlcdTdiYjFcdTRlOTEiLCJleHAiOjIzODI2NjI3NDAsImVtYWlsIjoiYXRhLXBheUAzNjAuY24ifQ.9857AdeUEUNS4q8fC2dlVPdrE59kSaaxKOZ5Qhtirg8"


def submit_file(file_path, token=None, host=None, machine="windows7_sp1_x86_cn_cloud_f21i9j7o10r9", file_type=None, decrypt_https=True, is_public=False, timeout=120, priority=150):
    if not host:
        host = ata_url
    headers = {"Authorization": "JWT {0}".format(token)}
    file_name = os.path.basename(file_path)
    file_payload = {
        "category": "file",
        "priority": priority,
        "config_map": json.dumps({
            file_name: {
                "is_public": is_public,
                "active_reboot": True,
                "env_var": [],
                "timeout": timeout,
                "internet": True,
                "human": False,
                "machine": machine,
                "file_type": file_type,
                "decrypt_https": decrypt_https
            }
        })
    }
    files = [("sample", open(file_path, "rb"))]
    response = requests.post(host, headers=headers, data=file_payload, files=files)

    if response.status_code == 200:
        return "success", response.text.encode("utf8"), file_name
    else:
        return "failed", response.text.encode("utf8"), file_name


def submit_url(url_name, token=None, host=None, machine="windows7_sp1_x86_cn_cloud_f21i9j7o10r9", decrypt_https=True, is_public=False, timeout=120, priority=150):
    if not host:
        host = ata_url
    headers = {"Authorization": "JWT {0}".format(token)}
    url_payload = {
        "category": "url",
        "config_map": json.dumps({
            url_name: {
                "is_public": is_public,
                "env_var": [],
                "timeout": timeout,
                "internet": True,
                "human": False,
                "decrypt_https": decrypt_https,
                "machine": machine
            }
        }),
        "url": [url_name],
        "priority": priority
    }

    response = requests.post(host, headers=headers, data=url_payload)
    if response.status_code == 200:
        return "success", response.text.encode("utf8"), url_name
    else:
        return "failed", response.text.encode("utf8"), url_name


def submit_md5(md5_name, token=None, host=None, machine="windows7_sp1_x86_cn_cloud_f21i9j7o10r9", decrypt_https=True, is_public=False, timeout=120, priority=150):
    if not host:
        host = ata_url
    headers = {"Authorization": "JWT {0}".format(token)}
    md5_payload = {
        "category": "md5",
        "priority": priority,
        "config_map": json.dumps({
            md5_name: {
                "is_public": is_public,
                "env_var": [],
                "timeout": timeout,
                "internet": True,
                "human": False,
                "machine": machine,
                "decrypt_https": decrypt_https
            }
        }),
        "md5": [md5_name]
    }
    response = requests.post(host, headers=headers, data=md5_payload)
    if response.status_code == 200:
        return "success", response.text.encode("utf8"), md5_name
    else:
        return "failed", response.text.encode("utf8"), md5_name


def submit_stream(file_path, content, token=None, host=None, machine="windows7_sp1_x86_cn_cloud_f21i9j7o10r9", file_type=None, decrypt_https=True, is_public=False, timeout=120, priority=150):
    if not host:
        host = ata_url
    filename = os.path.basename(file_path)
    f = StringIO(content)
    headers = {"Authorization": "JWT {0}".format(token)}
    payload = {
        'category': 'file',
        'config_map': json.dumps({
            filename: {
                "is_public": is_public,
                "active_reboot": True,
                "machine": machine,
                "env_var": [],
                "timeout": timeout,
                "internet": True,
                "human": False,
                "decrypt_https": decrypt_https,
                "file_type": file_type
            }
        })
    }
    files = [("sample", (filename, f.read()))]
    response = requests.post(host, headers=headers, data=payload, files=files)
    if response.status_code == 200:
        return "success", response.text.encode("utf8"), filename
    else:
        return "failed", response.text.encode("utf8"), filename


if __name__ == "__main__":
    content = u'qqqqqqqqqqqq'
    result, text, name = submit_stream('E:\\6c27a66fc08deef807cd7c27650bf88f', content, token)
    print(result, text, name)
