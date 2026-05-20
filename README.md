# IP Query Service

轻量级 IP 查询服务，返回当前服务器的公网 IP 地址。

## 原理

1. 向 `http://checkip.amazonaws.com` 发起请求，获取服务器的公网 IP
2. 结果缓存 5 分钟，避免频繁请求外部接口
3. 收到 HTTP GET 请求后，以纯文本形式返回 IP 地址

## 快速开始

### 使用 Docker

```bash
docker build -t ip-server .
docker run -d -p 5056:5056 --name ip-server ip-server
```

### 直接运行

```bash
pip install -r /dev/null  # 纯标准库，无需额外依赖
python app.py
```

## 访问

```bash
curl http://localhost:5056
# 返回：x.x.x.x
```

## 配置

| 参数 | 说明 | 默认值 |
|------|------|--------|
| 端口 | HTTP 监听端口 | 5056 |
| 缓存 TTL | IP 缓存时间 | 300 秒（5 分钟） |

如需修改端口，编辑 `app.py` 中的 `port` 变量。
