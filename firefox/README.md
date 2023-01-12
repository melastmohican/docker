

``` bash
docker build -t firefox .

```

``` bash
docker run -ti --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix firefox
```