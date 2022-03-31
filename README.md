# hatsune

初音ミクの色成分を [matplotlib](https://matplotlib.org) で可視化します。

もちろん、初音ミク以外の画像にも使用することが可能です。

[このツイート](https://twitter.com/95d2d3/status/1507072893477277696)と[インターネットお友達](https://twitter.com/2eep2lue/status/1507647686052237313)に[触発](https://twitter.com/2eep2lue/status/1507651659199000576)されました。

<div><video controls src="https://user-images.githubusercontent.com/43885603/160516984-bab60709-2438-4b44-9a4a-0ba614207949.mp4"></video></div>

## Usage

[Pipenv](https://github.com/pypa/pipenv) が必要です。

```sh
pipenv install

pipenv shell

# matplotlib のビューワが起動します。
python ./hatsune.py -i input_image_path

# plot を画像として保存します。
python ./hatsune.py -i input_image_path -o output_image_path
```

入力する画像ファイルはアルファチャンネル付き png が望ましいです。

また、使用されている色が多いと matplotlib のビューワの動作が重くなります。

## Acknowledgment

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">this is so cool! <a href="https://t.co/rXs4qkJK0L">https://t.co/rXs4qkJK0L</a></p>&mdash; Matplotlib (@matplotlib) <a href="https://twitter.com/matplotlib/status/1508140441983762432?ref_src=twsrc%5Etfw">March 27, 2022</a></blockquote>

## LICENSE

ソースコードは `LICENSE` の通り`The MIT License`ですが、初音ミクは ( おそらく ) クリプトン・フューチャー・メディア社が著作権を有しています。
