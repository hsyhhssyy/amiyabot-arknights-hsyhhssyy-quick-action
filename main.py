import os
import importlib
import inspect

from amiyabot.util import temp_sys_path
from core import log, Message, Chain, LazyLoadPluginInstance

curr_dir = os.path.dirname(__file__)

class QuickActionPluginInstance(LazyLoadPluginInstance):
    def install(self):
        pass
    def load(self):
        log.info('lazy detect other plugins')

bot = QuickActionPluginInstance(
    name='快速响应模式',
    version='1.2',
    plugin_id='amiyabot-arknights-hsyhhssyy-quick-action',
    plugin_type='',
    description='让兔兔可以一次执行多个任务',
    document=f'{curr_dir}/README.md'
)

def import_plugin_lib(module_name):

    plugin_dir = f'{curr_dir}/../'
    if os.path.exists(plugin_dir):
        folders = os.listdir(plugin_dir)

        for dir_name in folders:
            dir_path =  f'{curr_dir}/../{dir_name}'
            #log.info(f'dir_path:{dir_path} | basename:{os.path.basename(dir_path)} | abspath:{os.path.abspath(dir_path)} | dirname:{os.path.dirname(os.path.abspath(dir_path))}')

            if os.path.isdir(dir_path):
                if os.path.basename(dir_path).startswith(module_name):
                    with temp_sys_path(os.path.dirname(os.path.abspath(dir_path))):
                        module = importlib.import_module(os.path.basename(dir_path))
                    return module
    return None

@bot.on_message(keywords=['一键三连'],level=10)
async def _(data: Message):

    log.info('一键三连')

    #查询是否加载了签到插件，也就是plugins目录下有没有amiyabot-user-x文件夹

    user_module = import_plugin_lib(f'amiyabot-user')

    if user_module:
        #只有没有签过到才会触发一键三连
        reply = await user_module.main.user_info(data)
        await data.send(reply.text(user_module.main.sign_in(data, 1)['text']))
    else:
        log.info(f'未启用兔兔交互模块')

    #查询是否加载了抽卡插件，也就是plugins目录下有没有amiyabot-arknights-gacha

    gacha_module = import_plugin_lib(f'amiyabot-arknights-gacha')

    if gacha_module:
        gc = gacha_module.gachaBuilder.GachaBuilder(data)
        await data.send(gc.detailed_mode(10, 10, 0, ten_times=True))
    else:
        log.info(f'未启用寻访模拟模块')

    #查询是否加载了选老婆插件，也就是plugins目录下有没有amiyabot-arknights-hsyhhssyy-wifu

    wifu_module = import_plugin_lib('amiyabot-arknights-hsyhhssyy-wifu')

    if wifu_module:
        wifu =await wifu_module.main.wifu_action(data)
        await data.send(wifu)
    else:
        log.info(f'未启用选干员模块')