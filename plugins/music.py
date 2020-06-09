from nonebot import on_command, CommandSession,permission as perm
import asyncio
import traceback
from helper import getlogger,msgSendToBot,CQsessionToStr,check_path
from module.roll import match_roll
import config
from os import path
logger = getlogger(__name__)
__plugin_name__ = '音乐'
__plugin_usage__ = r"""
音乐！！！！！
"""
check_path('music')
music_path = path.join(config.music_path,'music','')
#1376882360 希望之花 163
#预处理
def headdeal(session: CommandSession):
    if session.event['message_type'] == "group" and session.event.sub_type != 'normal':
        return False
    return True
@on_command('希望之花',permission=perm.SUPERUSER | perm.PRIVATE_FRIEND | perm.GROUP_ADMIN | perm.GROUP_OWNER,only_to_me = False)
async def xwzh(session: CommandSession):
    if not headdeal(session):
        return
    await session.send("[CQ:music,type=163,id=1376882360]")

def deal_filename(stripped_arg):
    if path.exists(path.join('cache','music',stripped_arg)):
        return stripped_arg
    if path.exists(path.join('cache','music',stripped_arg + ".mp3")):
        return stripped_arg + ".mp3"
    return ''
@on_command('语音',aliases=['rec','REC'],permission=perm.SUPERUSER | perm.PRIVATE_FRIEND | perm.GROUP_ADMIN | perm.GROUP_OWNER,only_to_me = False)
async def recode(session: CommandSession):
    if not headdeal(session):
        return
    stripped_arg = session.current_arg_text.strip()
    stripped_arg = deal_filename(stripped_arg)
    if stripped_arg == '':
        await session.send("文件不存在")
        return
    if path.exists(path.join('cache','music',stripped_arg)+".mp3"):
        stripped_arg = stripped_arg + ".mp3"
    logger.info(CQsessionToStr(session))
    await session.send("[CQ:record,file={file}]".format(file = music_path + stripped_arg))