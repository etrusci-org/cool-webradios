#!/usr/bin/env python3

import json
import pathlib




def bake_dist(src_file: pathlib.Path, dist_dir: pathlib.Path) -> None:
    source: list[dict[str, dict[str, str] | list[dict[str, str]]]] = json.loads(src_file.read_bytes())
    html_tpl_file: pathlib.Path = (pathlib.Path(src_file.parent) / 'html.tpl').resolve()
    m3u_file: pathlib.Path = (pathlib.Path(dist_dir) / 'cool-webradios.m3u').resolve()
    html_file: pathlib.Path = (pathlib.Path(dist_dir) / 'cool-webradios.html').resolve()

    print('baking distributable ...')

    m3u_data: list[str] = [
        '#EXTM3U',
    ]

    html_tpl: str = html_tpl_file.read_text()
    html_data: list[str] = []

    for webradio in source:
        for channel in webradio['channel']:
            m3u_data.append(f"#EXTINF:0,{webradio['name']} : {channel['name']}\n{channel['url']}")
            html_data.append(f"<li>[<a href=\"{webradio['url']}\" target=\"_blank\">www</a>] [<a href=\"{channel['url']}\" target=\"_blank\">&gt;&gt;&gt;</a>] <strong>{webradio['name']}</strong> : {channel['name']}</li>")

    print(m3u_file)
    m3u_file.write_text('\n'.join(m3u_data))

    print(html_file)
    html_file.write_text(html_tpl.replace('{list}', ''.join(html_data)))




if __name__ == '__main__':
    SRC_FILE: pathlib.Path = (pathlib.Path(__file__).parents[1] / 'src' / 'webradios.json').resolve()
    DIST_DIR: pathlib.Path = (pathlib.Path(__file__).parents[1]).resolve()

    bake_dist(src_file=SRC_FILE, dist_dir=DIST_DIR)
