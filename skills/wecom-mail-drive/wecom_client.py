#!/usr/bin/env python3
"""企业微信微盘客户端"""

import os
import json
import time
import base64
import urllib.request
import urllib.error
from typing import Optional, Dict, Any, List

class WeComWeDrive:
    """企业微信微盘API客户端"""

    def __init__(self, corp_id: str = None, secret: str = None):
        self.corp_id = corp_id or os.environ.get("WECOM_CORP_ID", "ww4d3e18a99c2d9b61")
        self.secret = secret or os.environ.get("WECOM_WEDRIVE_SECRET") or os.environ.get("WECOM_CORP_SECRET")
        self.base_url = "https://qyapi.weixin.qq.com/cgi-bin"
        self._token_cache = {"token": None, "expires": 0}

    def get_access_token(self) -> str:
        """获取access_token"""
        if self._token_cache["token"] and time.time() < self._token_cache["expires"]:
            return self._token_cache["token"]

        url = f"{self.base_url}/gettoken?corpid={self.corp_id}&corpsecret={self.secret}"
        data = self._request_get(url)

        if data.get("errcode", 0) == 0:
            self._token_cache["token"] = data["access_token"]
            self._token_cache["expires"] = time.time() + data.get("expires_in", 7200) - 300
            return self._token_cache["token"]

        raise Exception(f"获取token失败: {data}")

    def _request_get(self, url: str) -> Dict:
        """GET请求"""
        with urllib.request.urlopen(url) as resp:
            return json.loads(resp.read().decode())

    def _request_post(self, url: str, data: Dict) -> Dict:
        """POST请求"""
        req = urllib.request.Request(
            url,
            data=json.dumps(data).encode(),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())

    def get_space_list(self, userid: str = None) -> Dict:
        """获取空间列表

        Args:
            userid: 用户ID，不填则获取应用可见范围内所有空间
        """
        token = self.get_access_token()
        url = f"{self.base_url}/wedrive/space_list?access_token={token}"
        data = {}
        if userid:
            data["userid"] = userid
        return self._request_post(url, data)

    def get_space_info(self, spaceid: str) -> Dict:
        """获取空间信息

        Args:
            spaceid: 空间ID
        """
        token = self.get_access_token()
        url = f"{self.base_url}/wedrive/space_info?access_token={token}"
        return self._request_post(url, {"spaceid": spaceid})

    def list_files(self, spaceid: str, fatherid: str = None,
                   start: int = 0, limit: int = 100, sort_type: int = 1) -> Dict:
        """获取文件列表

        Args:
            spaceid: 空间ID
            fatherid: 父文件夹ID，空为根目录
            start: 起始位置
            limit: 返回数量限制
            sort_type: 排序方式 1-名称升序 2-名称降序 3-大小升序 4-大小降序 5-修改时间升序 6-修改时间降序
        """
        token = self.get_access_token()
        url = f"{self.base_url}/wedrive/file_list?access_token={token}"
        data = {
            "spaceid": spaceid,
            "start": start,
            "limit": limit,
            "sort_type": sort_type
        }
        if fatherid:
            data["fatherid"] = fatherid
        return self._request_post(url, data)

    def upload_file(self, spaceid: str, fatherid: str, file_path: str,
                    file_name: str = None) -> Dict:
        """上传文件

        Args:
            spaceid: 空间ID
            fatherid: 父文件夹ID
            file_path: 本地文件路径
            file_name: 上传后的文件名，默认使用原文件名
        """
        token = self.get_access_token()
        url = f"{self.base_url}/wedrive/file_upload?access_token={token}"

        if not file_name:
            file_name = os.path.basename(file_path)

        with open(file_path, "rb") as f:
            content = base64.b64encode(f.read()).decode()

        data = {
            "spaceid": spaceid,
            "fatherid": fatherid,
            "file_name": file_name,
            "file_base64_content": content
        }
        return self._request_post(url, data)

    def download_file(self, fileid: str = None, selected_ticket: str = None) -> Dict:
        """获取文件下载链接

        Args:
            fileid: 文件ID
            selected_ticket: JS-SDK选择文件返回的ticket

        Returns:
            包含download_url和cookie_name/cookie_value的字典
        """
        token = self.get_access_token()
        url = f"{self.base_url}/wedrive/file_download?access_token={token}"

        data = {}
        if fileid:
            data["fileid"] = fileid
        elif selected_ticket:
            data["selected_ticket"] = selected_ticket
        else:
            raise ValueError("必须提供fileid或selected_ticket")

        return self._request_post(url, data)

    def download_file_to_local(self, fileid: str, save_path: str) -> str:
        """下载文件到本地

        Args:
            fileid: 文件ID
            save_path: 保存路径

        Returns:
            保存的文件路径
        """
        result = self.download_file(fileid=fileid)

        if result.get("errcode", 0) != 0:
            raise Exception(f"获取下载链接失败: {result}")

        download_url = result.get("download_url")
        cookie_name = result.get("cookie_name")
        cookie_value = result.get("cookie_value")

        req = urllib.request.Request(download_url)
        if cookie_name and cookie_value:
            req.add_header("Cookie", f"{cookie_name}={cookie_value}")

        with urllib.request.urlopen(req) as resp:
            with open(save_path, "wb") as f:
                f.write(resp.read())

        return save_path

    def create_folder(self, spaceid: str, fatherid: str, folder_name: str) -> Dict:
        """创建文件夹

        Args:
            spaceid: 空间ID
            fatherid: 父文件夹ID
            folder_name: 文件夹名称
        """
        token = self.get_access_token()
        url = f"{self.base_url}/wedrive/file_create?access_token={token}"
        data = {
            "spaceid": spaceid,
            "fatherid": fatherid,
            "file_type": 1,  # 1=文件夹
            "file_name": folder_name
        }
        return self._request_post(url, data)

    def delete_file(self, fileid: List[str]) -> Dict:
        """删除文件/文件夹

        Args:
            fileid: 文件ID列表
        """
        token = self.get_access_token()
        url = f"{self.base_url}/wedrive/file_delete?access_token={token}"
        return self._request_post(url, {"fileid": fileid})

    def rename_file(self, fileid: str, new_name: str) -> Dict:
        """重命名文件/文件夹

        Args:
            fileid: 文件ID
            new_name: 新名称
        """
        token = self.get_access_token()
        url = f"{self.base_url}/wedrive/file_rename?access_token={token}"
        return self._request_post(url, {"fileid": fileid, "new_name": new_name})

    def move_file(self, fileid: List[str], fatherid: str) -> Dict:
        """移动文件/文件夹

        Args:
            fileid: 文件ID列表
            fatherid: 目标文件夹ID
        """
        token = self.get_access_token()
        url = f"{self.base_url}/wedrive/file_move?access_token={token}"
        return self._request_post(url, {"fileid": fileid, "fatherid": fatherid})

    def get_file_info(self, fileid: str) -> Dict:
        """获取文件信息

        Args:
            fileid: 文件ID
        """
        token = self.get_access_token()
        url = f"{self.base_url}/wedrive/file_info?access_token={token}"
        return self._request_post(url, {"fileid": fileid})


# 命令行工具
if __name__ == "__main__":
    import sys

    client = WeComWeDrive()

    if len(sys.argv) < 2:
        print("用法:")
        print("  python wecom_client.py spaces              # 获取空间列表")
        print("  python wecom_client.py list <spaceid>      # 获取文件列表")
        print("  python wecom_client.py upload <spaceid> <fatherid> <filepath>  # 上传文件")
        print("  python wecom_client.py download <fileid> <savepath>  # 下载文件")
        sys.exit(1)

    cmd = sys.argv[1]

    try:
        if cmd == "spaces":
            result = client.get_space_list()
            print(json.dumps(result, ensure_ascii=False, indent=2))

        elif cmd == "list" and len(sys.argv) >= 3:
            spaceid = sys.argv[2]
            fatherid = sys.argv[3] if len(sys.argv) > 3 else None
            result = client.list_files(spaceid, fatherid)
            print(json.dumps(result, ensure_ascii=False, indent=2))

        elif cmd == "upload" and len(sys.argv) >= 5:
            spaceid = sys.argv[2]
            fatherid = sys.argv[3]
            filepath = sys.argv[4]
            result = client.upload_file(spaceid, fatherid, filepath)
            print(json.dumps(result, ensure_ascii=False, indent=2))

        elif cmd == "download" and len(sys.argv) >= 4:
            fileid = sys.argv[2]
            savepath = sys.argv[3]
            result = client.download_file_to_local(fileid, savepath)
            print(f"文件已保存到: {result}")

        else:
            print(f"未知命令: {cmd}")
            sys.exit(1)

    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)
