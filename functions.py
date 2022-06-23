import json

from loggers import file_logger


def get_json(fname='posts.json'):
    try:
        with open(fname, encoding='utf-8') as fin:
            posts = json.load(fin)
    except FileNotFoundError:
        print('Posts file not found!')
        file_logger.error('JSON file not found')
        posts = []
    except json.JSONDecodeError:
        print('Json recoding error')
        file_logger.error('JSON decoding error')
        posts = []
    return posts


def write_json(posts, fname='posts.json'):
    try:
        with open(fname, 'w', encoding='utf-8') as fout:
            json.dump(posts, fout, indent=1, ensure_ascii=False)
    except IOError:
        print('IO error')


def find_posts(posts: list, s: str) -> list:
    filtered = []
    for post in posts:
        if s in post["content"]: filtered.append(post)
    return filtered


def add_post(pic: str, post: str):
    posts = get_json()
    posts.append({'pic': pic, 'content': post})
    write_json(posts)


