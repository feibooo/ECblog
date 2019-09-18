import orm
import asyncio
from model import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='root', db='awesome')
    u = User(name='admin', email='admin@qq.com', passwd='admin', image='about:blank',admin=1)
    await u.save()
    ## 网友指出添加到数据库后需要关闭连接池，否则会报错 RuntimeError: Event loop is closed
    orm.__pool.close()
    await orm.__pool.wait_closed()
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()