# -*- coding: UTF-8 -*-
import nonebot
import plugins.twitter.notification.tweetUtils as utils
from plugins.management.management import valid_group



@nonebot.on_command('loadtwitterlist', aliases = ('加载','推特列表'),only_to_me=False, privileged=True)
async def getOld(session: nonebot.CommandSession):
    oldTwitter = utils.get_old_twitter()
    length = len(oldTwitter.tList)
    await session.send("列表共找到{0}条推特".format(length))
    for t in oldTwitter.tList:
        await session.send(str(t))

@nonebot.on_command('update', aliases=("刷新","refresh",),only_to_me=False,privileged=True)
async def getUpdate(session: nonebot.CommandSession):
    updateTwitter = utils.get_update_twitter()
    length = len(updateTwitter.tList)
    await session.send("共找到{0}条新推特".format(length))
    for t in updateTwitter.tList:
        await session.send(str(t))
    pass
