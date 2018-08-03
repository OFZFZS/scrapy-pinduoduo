==========================

# **scrapy-pinduoduo**(拼多多爬虫)

基于scrapy的拼多多的爬虫

- 默认抓取拼多多的热门栏目所有商品
- 默认每个商品只获取二十条评论
- 爬取到的数据存储到MongoDB数据库

经过测试,拼多多客户端的数据和它手机版http://yangkeduo.com/的数据是一模一样的,因此这里爬取的数据都出自这个站点.


主要接口
=============

- 热销商品列表: http://apiv3.yangkeduo.com/v5/goods?page=页码&size=条数
  - page:默认从第一页开始
  - size:默认是20条,最多可以设置400条
- 用户评论: http://apiv3.yangkeduo.com/reviews/商品ID/list?&size=条数
  - 商品ID:从热销商品列表页面获取
  - size:默认是10条,最多可以设置20条




截图展示
=======

![数据展示](https://github.com/OFZFZS/scrapy-pinduoduo/blob/master/scpture.jpg?raw=true)



联系作者
-------

欢迎给我发送邮件s:

    admin@sanhe66.com
