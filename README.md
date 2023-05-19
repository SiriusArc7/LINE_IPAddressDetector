IPアドレスの変更を検知したらLINE Notify APIを使ってお知らせするだけ

変わりなければ何もしない

cronで数分~数時間おきに実行する運用を想定


This script just sends notification via LINE Notify API when an IP address of the computer/raspi/machine has changed.

It will remain silent if there is no change. Suitable for running every couple minutes to hours for monitoring.


事前にやっておくこと:

Requirements:
```
pip install python-decouple
```