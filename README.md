# discord_bot
##コマンド一覧
* /help list  
Jsonに書いたdata内のlistを全部表示させる。  
いつか中身をきれいに整形させる・・・
* /help_add_command  
コマンド追加するコマンドを表示させるよう。
* /add_command  
  * /add_command img_name=test.jpg words=test,tttt img_url=httpURL  
    * img_name = コマンドの名前を入れる(保存するファイル名にもなる)
    * words = ここに入れた文字に反応するようになる。
      * 何個でも追加できる。追加する場合は`,`で区切る。途中にスペース入れると壊れる。
      * 追加出来るファイル拡張子はjpg, gif, jpeg, bmpのみ。
        * PNG忘れてたけど。いつか追加する
        * URLのファイルがGIFだろうがBMPだろうが、img_nameのところで指定したファイルで保存される。
    * img_url = HTTPのURLをそのまま張る。
      * ローカルのファイルパスじゃないので注意
  * 同じimg_nameは登録できない
