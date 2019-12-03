
from make_file import FilePath
import urllib.request


def data_list():
    """ jsonのDATAの中のlistを全て取得
    """
    js = []
    with FilePath() as f:
        js = [x for x in f.read_json()]
    return js


def add_data(name, file_path, words):
    result = None
    try:
        with FilePath(name=name, path=file_path, words=words) as fp:
            result = fp.add_json()
            return result
    except Exception as e:
        return result


def download_pict(url, file_name):
    """リクエスト使ってファイルの取得
    """
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
    }

    req = urllib.request.Request(url, headers=header)
    with urllib.request.urlopen(req) as wf:
        data = wf.read()
        with open(f"./pict/{file_name}", "wb") as lf:
            lf.write(data)

    return f"./pict/{file_name}"


if __name__ == "__main__":
    # add_data("test", "path", ["t"])
    # download_pict("url", "test")

    # dat = call_list()
    # print(dat)

    # for x in [x for x in call_list()]:
    #     if "a" in x["words"][:]:
    #         print(x)

    pass