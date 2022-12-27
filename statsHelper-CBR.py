from cbr.plugin.cbrinterface import CBRInterface
from cbr.plugin.info import MessageInfo

METADATA = {
    'id': 'statshelper',
    'version': '0.0.1',
    'name': 'StatsHelper-CBR',
    'description': 'it is a plugin for getting stats from one mc client',
    'author': 'Ricky',
    'link': 'https://github.com/R1ckyH/statsHelper-CBR'
}  # just do it like MCDR


target_client = "survival"


help_msg = '''
##stats <classification> <target> [<-bot>] [<-all>]
add -bot to list bots (dumb filter tho)
add -all to list every player (spam warning)
<classification>: killed, killed_by, dropped, picked_up, used, mined, broken, crafted, custom
the <target> of killed, killed_by are entity type
the <target> of picked_up, used, mined, broken, crafted are block/item id
'''


def on_message(server: CBRInterface, info: MessageInfo):
    if info.content.startswith('##stats'):
        info.cancel_send_message()
        cmd = info.content.replace("##stats rank", "!!stats rank").replace("##stats", "!!stats rank")
        cmd_len = len(cmd.split(' '))
        if cmd_len < 4 or cmd_len > 5:
            server.reply(info, help_msg)
        else:
            result = server.api_query(target_client, 'StatsHelper', 'on_info', [None, None, cmd])
            if result is None:
                server.reply(info, "Cant get any rank")
            else:
                server.reply(info, result)


def on_command(server: CBRInterface, info: MessageInfo):
    on_message(server, info)


def on_load(server: CBRInterface):
    server.register_help_message("##stats", "使用statshelper")

