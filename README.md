# コロッケゲームランド

コロッケが主役のミニゲーム集です。スマホでもパソコンでもあそべます。

▶ https://korokke-games.github.io/

## 更新のしかた

ゲームの元ファイルは Claude のプロジェクトで作っています。`python3 tools/sync.py .` で最新のゲームをこのリポジトリにコピーし（Artifact 用のHTMLを完全なページに包みます）、新しいゲームはトップページ `index.html` にカードを追加して `main` に push すると公開されます。
