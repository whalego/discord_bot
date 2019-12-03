
import discord
import modules
from pathlib import Path
token = "TOKEN"
client = discord.Client()

@client.event
async def on_ready():
    print("wakeup bot")

@client.event
async def on_message(msg):
    if msg.author.bot:
        return

    if str(msg.author.id) == "自分のID" and "ボット消すなにか" in msg.content:
        import os
        os.sys.exit(0)

    if msg.content == "/help list":
        words_list = [x for x in modules.data_list()][:]
        await msg.channel.send(f"{words_list}")

    if msg.content:
        try:
            for x in [x for x in modules.data_list()]:
                for y in x["words"]:
                    if y in msg.content:
                        fp = Path(x["file_path"])
                        file_img = discord.File(fp)
                        await msg.channel.send(file=file_img)
                        break

        except Exception as e:
            print(e)

    if "/help_add_command" == msg.content:
        await msg.channel.send("/add_command img_name=test.jpg words=words1,words2 img_url=http://url\nファイルパス反応しない")
        return

    if "/add_command" in msg.content:
        """
        /add_command img_name=test.jpg words=test,tttt img_url=httpURL
        TODO: メッセージの頭がだったらの記述増やす
        """
        cmd_list = msg.content.split(" ")
        if len(cmd_list) == 4:
            if cmd_list[1].replace("img_name=", "") in [x["name"] for x in modules.data_list()]:
                await msg.channel.send(f"すでに同じ名前のコマンドが登録されています。")
                return

            if not cmd_list[1].replace("img_name=", "").split(".")[-1] in ["jpg", "gif", "jpeg", "bmp"]:
                await msg.channel.send(f"jpg, gif, jpeg, bmp only")
                return
            "nameで重複チェックを行う"
            img_path = modules.download_pict(url=cmd_list[-1].replace("img_url=", ""),
                                             file_name=cmd_list[1].replace("img_name=", ""))
            result = modules.add_data(name=cmd_list[1],
                                      file_path=img_path,
                                      words=[x for x in cmd_list[2].split("=")[1].split(",")]
                                      )
            if result:
                await msg.channel.send(f"登録成功\n{cmd_list[2].split('=')[1].split(',')}")
            else:
                await msg.channel.send(f"登録失敗")
        else:
            await msg.channel.send(f"コマンドの入力方法間違えてる\nplease type this command `/help_add_command`")
        return 
        

client.run(token)

