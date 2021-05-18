# Shodan Search

Shodan与谷歌、百度等搜索引擎爬取网页信息不同，它爬取的是互联网上所有设备的 IP 地址及其端口号。

打开 `shodan.io` 搜索设备 Hikvision-Webs 可以看到到这个品牌的摄像头设备遍及全球的IP及其暴露的端口号

Shodan 官方提供了 Python SDK 包来帮助 python 开发者

#### 安装
```
pip install shodan
```

#### 注册获取API Key
1. 登陆 https://account.shodan.io/register
2. 输入完相关信息，点击 CREATE 会跳转到个人账户页
3. 此时 API Key 会显示你的API秘钥，请记录这个秘钥，后续会使用到这个秘钥去请求接口。

#### 使用 python 调用
Shodan 本质上就是一个搜索引擎，只需要输入搜索的关键词
```
from shodan import Shodan

api = Shodan('你的API KEY')

def search_shodan(keyword):
    # 调用搜索接口
    result = api.search(keyword)

    # 显示所有IP
    for service in result['matches']:
            print(service['ip_str'])

search_shodan("Hikvision-Webs")
```
> 如果你想要使用过滤条件，Shodan 需要你升级API权限
> 价格为 49$ 不过是一次性支付终身可以使用


#### 进阶
Shodan 的用处当然不仅仅是在黑客攻防中，它还能用于统计。
如果你想要了解哪些国家的使用这款摄像头的数量最多，可以使用 Facets 特性。
```
from shodan import Shodan

api = Shodan('你的API KEY')
def try_facets(query):
    FACETS = [
        'org',
        'domain',
        'port',
        'asn',
        ('country', 3),
    ]

    FACET_TITLES = {
        'org': 'Top 5 Organizations',
        'domain': 'Top 5 Domains',
        'port': 'Top 5 Ports',
        'asn': 'Top 5 Autonomous Systems',
        'country': 'Top 3 Countries',
    }

    try:
        # 使用 count() 方法可以不需要升级API，且比 search 方法更快。
        result = api.count(query, facets=FACETS)

        print('Shodan Summary Information')
        print('Query: %s' % query)
        print('Total Results: %s\n' % result['total'])

        # 显示每个要素的摘要
        for facet in result['facets']:
            print(FACET_TITLES[facet])

            for term in result['facets'][facet]:
                print('%s: %s' % (term['value'], term['count']))

    except Exception as e:
        print('Error: %s' % e)

try_facets("Hikvision-Webs")
```
从 Top 3 Countries 中可以看到，这款摄像头使用数量排名前三的国家分别是：美国、日本和德国。

Shodan 用于产品分析也挺不错。

同样地原理，如果你把关键词改为 apache ，你可以知道目前哪些国家使用apache服务器数量最多，最普遍被使用的版本号是什么。