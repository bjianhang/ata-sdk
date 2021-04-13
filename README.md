# 简介
依托360核心安全15年攻防实践与安全大数据积累，360沙箱云具备领先的漏洞检测技术和深入全面的样本行为分析能力，构筑漏洞攻防知识与高级威胁检测能力的闭环，让威胁无所遁行。


## 提交文件：submit_file

```
    参数说明：
        file_path       文件绝对路径，必填
        token           用户JWT token，必填
        host            提交接口，默认为沙箱云线上环境，选填
        machine         检测镜像，默认为windows7_sp1_x64_cn_cloud_f21i9j7o10r9，选填
        file_type       指定文件类型，选填
        decrypt_https   是否开启https解密 ，选填
        is_public       是否公开，选填
        timeout         超时设置，选填
        priority        优先级，默认150，最大256，选填
 ```
        
## 提交url：submit_url

```
    参数说明：
        url_name        url路径，必填
        token           用户JWT token，必填
        host            提交接口，默认为沙箱云线上环境，选填
        machine         检测镜像，默认为windows7_sp1_x64_cn_cloud_f21i9j7o10r9，选填
        decrypt_https   是否开启https解密 ，选填
        is_public       是否公开，选填
        timeout         超时设置，选填
        priority        优先级，默认150，最大256，选填
```

## 提交MD5:submit_md5

```
    参数说明：
        md5             md5，必填
        token           用户JWT token，必填
        host            提交接口，默认为沙箱云线上环境，选填
        machine         检测镜像，默认为windows7_sp1_x64_cn_cloud_f21i9j7o10r9，选填
        file_type       指定文件类型，选填
        decrypt_https   是否开启https解密 ，选填
        is_public       是否公开，选填
        timeout         超时设置，选填
        priority        优先级，默认150，最大256，选填
```
        
## 提交文件流：submit_stream
        file_path       文件绝对路径，必填
        content         文件内容，unicoude格式，必填
        token           用户JWT token，必填
        host            提交接口，默认为沙箱云线上环境，选填
        machine         检测镜像，默认为windows7_sp1_x64_cn_cloud_f21i9j7o10r9，选填
        file_type       指定文件类型，选填
        decrypt_https   是否开启https解密 ，选填
        is_public       是否公开，选填
        timeout         超时设置，选填
        priority        优先级，默认150，最大256，选填
