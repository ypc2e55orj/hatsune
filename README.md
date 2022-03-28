# hatsune

初音ミクの色成分をmatplotlibで可視化します。

[このツイート](https://twitter.com/95d2d3/status/1507072893477277696) とインターネットお友達に触発されました。

## Usage
[Pipenv](https://github.com/pypa/pipenv) が必要です。

```sh
pipenv install

# matplotlibのビューワが起動します。
python ./hatsune.py -i input_image_path -s

# 画像として保存します。
python ./hatsune.py -i input_image_path -o output_image_path
```

## Acknowledgments

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">this is so cool! <a href="https://t.co/rXs4qkJK0L">https://t.co/rXs4qkJK0L</a></p>&mdash; Matplotlib (@matplotlib) <a href="https://twitter.com/matplotlib/status/1508140441983762432?ref_src=twsrc%5Etfw">March 27, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## LICENSE

ソースコードは `LICENSE` の通り`The MIT License`ですが、初音ミクは ( おそらく ) クリプトン・フューチャー・メディア社が著作権を有しています。
