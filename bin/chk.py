#!/usr/bin/env python3

import datetime
import json
import pathlib
import time

import vlc # python3-vlc




def check_webradios(src_file: pathlib.Path, log_file: pathlib.Path, playtime: int) -> None:
    if not src_file.is_file():
        print(f'SRC_FILE not found: {SRC_FILE}')
        exit(1)

    source: list[dict[str, dict[str, str] | list[dict[str, str]]]] = json.loads(src_file.read_bytes())

    instance: vlc.Instance = vlc.Instance()
    player: vlc.MediaPlayer = instance.media_player_new()
    player.audio_set_mute(True) # does not always work
    player.audio_set_volume(0) # does not always work

    errors: int = 0
    log: list[str] = []

    print('checking station channels ...')

    try:
        for station in source:
            for channel in station['channel']:
                print(f"{station['name']} - {channel['name']}")
                media: vlc.Media = instance.media_new(channel['url'])
                player.set_media(media)
                player.play()
                time.sleep(playtime)
                state: str = str(player.get_state())
                player.stop()
                if state.lower() != 'state.playing':
                    log.append(f"{datetime.datetime.now()} BOO: {station['name']} - {channel['name']} - {channel['url']}")
                    errors += 1
                else:
                    log.append(f"{datetime.datetime.now()} OK: {station['name']} - {channel['name']} - {channel['url']}")
                time.sleep(2)

    except KeyboardInterrupt:
        pass
    finally:
        player.stop()
        log_file.write_text('\n'.join(log))

    if errors == 0:
        print('everything seems ok')
    else:
        print(f'errors occurred, see {log_file}')




if __name__ == '__main__':
    SRC_FILE: pathlib.Path = (pathlib.Path(__file__).parents[1] / 'src' / 'webradios.json').resolve()
    LOG_FILE: pathlib.Path = (pathlib.Path(__file__).parents[1] / 'log' / 'chk.log').resolve()
    PLAYTIME: int = 10

    check_webradios(src_file=SRC_FILE, log_file=LOG_FILE, playtime=PLAYTIME)
