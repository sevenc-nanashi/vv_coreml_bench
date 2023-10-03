# vv_coreml_bench

Voicevox CoreのモデルはCoreML+Conv2dで速くなるのかを調べるためのリポジトリ。

## 環境構築
```bash
# Python周り
python -m pip install --upgrade pip
pip install -r requirements.txt

# OpenJTalkの辞書
curl "https://jaist.dl.sourceforge.net/project/open-jtalk/Dictionary/open_jtalk_dic-1.11/open_jtalk_dic_utf_8-1.11.tar.gz" -o open_jtalk_dic_utf_8-1.11.tar.gz
tar zxvf open_jtalk_dic_utf_8-1.11.tar.gz

# vvmダウンロード
curl https://github.com/VOICEVOX/voicevox_core/raw/main/model/sample.vvm -Lo conv1d.vvm
curl https://cdn.discordapp.com/attachments/847301818571816960/1152729793381552209/xaa -Lo /tmp/xaa
curl https://cdn.discordapp.com/attachments/847301818571816960/1152729793733865562/xab -Lo /tmp/xab
cat /tmp/xaa /tmp/xab > conv2d.vvm

# onnxruntimeダウンロード
curl https://github.com/microsoft/onnxruntime/releases/download/v1.14.0/onnxruntime-osx-x86_64-1.14.0.tgz -Lo onnxruntime-osx-x86_64-1.14.0.tgz
tar zxvf onnxruntime-osx-x86_64-1.14.0.tgz
cp onnxruntime-osx-x86_64-1.14.0/lib/libonnxruntime.1.14.0.dylib .
```
