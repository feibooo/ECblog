import logging
logging.basicConfig(level=logging.INFO)
import asyncio
from aiohttp import web

#make respone
async def index(request):
    return web.Response(body='<h1>Awesome Website</h1>'.encode(),content_type='text/html')

def init():
    app=web.Application()
    app.router.add_get('/',index)
    web.run_app(app,host='127.0.0.1',port=9000)

if __name__ == '__main__':
    init()