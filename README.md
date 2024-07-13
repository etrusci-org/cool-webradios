# Cool Webradios

Webradios I like.




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




## Boo

On windows, if this error occurs: `[000001e6ce051950] main libvlc error: stale plugins cache: modified ...`, then open cmd as admin and run:

```sh
"C:\Program Files\VideoLAN\VLC\vlc-cache-gen.exe" "C:\Program Files\VideoLAN\VLC\plugins"
```
