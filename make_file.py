
import json
from pathlib import Path


class FilePath:
    def __init__(self, name=None, path=None, words=[]):
        self.name = name
        self.path = str(path)
        self.words = words
        self.json_path = Path("./filepath.json")
        if type(words) is not list:
            raise Exception("not list")

    def add_json(self):
        if not self.name and not self.path and not self.words:
            """未入力項目があったら追記はしない
            """
            return False
        if "TBD":
            # 重複項目は入力しない条件を作る
            pass
        with open(self.json_path, "r") as json_file:
            jf = json.load(json_file)
            jf["data"].append({"name": self.name,
                               "file_path": self.path,
                               "words": self.words
                               })
        with open(self.json_path, "w") as f:
            json.dump(jf, f, indent=4)

        return True

    def read_json(self):
        """ jsonの中身を返却
        """
        with open(self.json_path, "r") as jf:
            result = json.load(jf)
        return result["data"]

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_value, trace):
        """エラー出したくない"""
        return True
