from urllib.request import urlopen


def words_per_line(flo):
    return [len(line.split()) for line in flo.readlines()]


with open("write_to_file.txt", mode='rt', encoding='utf-8') as real_file:
    wpl = words_per_line(real_file)
    print(wpl)
    print(type(real_file))  # _io.TextIOWrapper

with urlopen("http://sixty-north.com/c/t.txt") as web_file:
    wpl = words_per_line(web_file)
    print(wpl)
    print(type(web_file))  # http.client.HTTPResponse
