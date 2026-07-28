import yaml
import re


INPUT = "flclash-original.yaml"
OUTPUT = "flclash.yaml"


REMOVE_TYPES = [
    "socks5"
]


REMOVE_KEYWORDS = [
    "测试",
    "试用",
    "临时",
    "共享",
    "公益",
    "机场"
]


US_KEYWORDS = [
    "美国",
    "🇺🇸",
    "US",
    "USA",
    "United States"
]


def get_speed(name):

    if not name:
        return 0

    m = re.search(
        r'(\d+\.\d+)MB/s',
        name
    )

    if m:
        return float(m.group(1))

    return 0



with open(INPUT, "r", encoding="utf-8") as f:

    config = yaml.safe_load(f)



proxies = config.get("proxies", [])


result = []

servers = set()



for p in proxies:


    name = p.get("name", "")

    ptype = p.get("type", "")

    server = p.get("server", "")

    port = p.get("port", "")


    # 只保留美国节点

    if not any(
        k.lower() in name.lower()
        for k in US_KEYWORDS
    ):
        continue


    # 删除 socks5

    if ptype in REMOVE_TYPES:
        continue


    # 删除异常关键词

    if any(
        k in name
        for k in REMOVE_KEYWORDS
    ):
        continue


    # 删除不完整节点

    if not server or not port:
        continue


    # 删除重复服务器

    key = f"{server}:{port}"

    if key in servers:
        continue


    servers.add(key)

    result.append(p)



# 按速度排序

result.sort(
    key=lambda x:get_speed(x.get("name")),
    reverse=True
)



config["proxies"] = result



with open(
    OUTPUT,
    "w",
    encoding="utf-8"
) as f:

    yaml.dump(
        config,
        f,
        allow_unicode=True,
        sort_keys=False
    )


print(
    f"美国节点过滤完成：{len(proxies)} → {len(result)}"
)
