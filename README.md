# Cool Webradios

Webradios I like.


To listen, open **[cool-webradios.m3u](./cool-webradios.m3u)** in a media player.
To get an overview, open **[cool-webradios.html](./cool-webradios.html)** in a web browser.




## Dependencies

To listen to the webradios:
- Media player with webradio support, e.g. [Foobar2000](https://www.foobar2000.org), [VLC](https://videolan.org), etc.

To run **bin/chk.py**:

- [Python](https://python.org) `>= 3.11.2`
- [VLC](https://videolan.org) `>= 3.0.21`
- [Python bindings for libvlc](https://github.com/oaubert/python-vlc)

```sh
sudo apt install python3
sudo apt install vlc
sudo apt install python3-vlc
```




## Build

```sh
# check station channels for availability
# result will be written to log/chk.log
bin/chk.py

# bake m3u and html file with data from src/webradios.json
bin/bake.py
```

You can adjust the defaults in the `if __name__ == '__main__':` part of **bin/chk.py** and **bin/bake.py**.




## Boo

On windows, if a `[000001e6ce051950] main libvlc error: stale plugins cache: modified ...`, error occurrs, open cmd as admin and run...

```sh
"C:\Program Files\VideoLAN\VLC\vlc-cache-gen.exe" "C:\Program Files\VideoLAN\VLC\plugins"
```




## License

[The Unlicense](./LICENSE.md)
