# mmlabc-to-smf

Music Macro Language (MML) から Standard MIDI File (SMF) への変換ツール

<p align="left">
  <a href="README.ja.md"><img src="https://img.shields.io/badge/🇯🇵-Japanese-red.svg" alt="Japanese"></a>
  <a href="README.md"><img src="https://img.shields.io/badge/🇺🇸-English-blue.svg" alt="English"></a>
</p>

## 概要

このプロジェクトは、Music Macro Language形式の文字列を、包括的なデバッグ出力を備えた4パスアーキテクチャを使用してStandard MIDI Fileに変換します。

## 特徴

- **4パスアーキテクチャ**: 
  - パス1: MML文字列をトークンに解析（`pass1_tokens.json`を出力）
  - パス2: トークンを抽象構文木（AST）に変換（`pass2_ast.json`を出力）
  - パス3: ASTからMIDIイベントを生成（`pass3_events.json`を出力）
  - パス4: Standard MIDI Fileを作成（`.mid`ファイルを出力）
- **デバッグJSON出力**: 各パスは、デバッグ用に中間結果をJSONとして保存します
- **テスト駆動開発**: ユニットテストと統合テストを含む包括的なテストスイート
- **モジュール設計**: 各パスはファイルごとに約100行以下で実装されています

## 必要要件

- Python 3.8以上
- mido（PythonのMIDIライブラリ）

## インストール

```bash
pip install -r requirements.txt
```

## 使い方

### 基本的な使い方

```bash
python mml_to_smf.py "cde"
```

これにより、MML文字列"cde"（音符C、D、E）が以下のように変換されます：
- MIDIノート 60、62、64（ミドルC、D、E）
- 出力ファイル: `output.mid`
- デバッグファイル: `pass1_tokens.json`、`pass2_ast.json`、`pass3_events.json`

### カスタム出力ファイル

```bash
python mml_to_smf.py "cde" -o my_song.mid
```

### サポートされる音符

現在、基本的な音符名をサポートしています：`c`、`d`、`e`、`f`、`g`、`a`、`b`

## 実行例

```bash
$ python mml_to_smf.py "cde"
Converting MML: cde
Pass 1: Parsing MML...
  Generated 3 tokens → pass1_tokens.json
Pass 2: Creating AST...
  Generated AST with 3 notes → pass2_ast.json
Pass 3: Creating MIDI events...
  Generated 6 events → pass3_events.json
Pass 4: Creating MIDI file...
  Generated MIDI file → output.mid

Conversion complete!
Output files:
  - pass1_tokens.json (debug)
  - pass2_ast.json (debug)
  - pass3_events.json (debug)
  - output.mid (final output)
```

## プロジェクト構成

```
mmlabc-to-smf/
├── src/
│   ├── pass1_parser.py    # パス1: MML解析
│   ├── pass2_ast.py        # パス2: AST作成
│   ├── pass3_events.py     # パス3: イベント生成
│   └── pass4_midi.py       # パス4: MIDIファイル作成
├── tests/
│   ├── test_pass1.py       # パス1のユニットテスト
│   ├── test_pass2.py       # パス2のユニットテスト
│   ├── test_pass3.py       # パス3のユニットテスト
│   ├── test_pass4.py       # パス4のユニットテスト
│   └── test_integration.py # 統合テスト
├── mml_to_smf.py          # メインCLIスクリプト
├── requirements.txt        # Python依存関係
└── README.md              # このファイル
```

## テスト

すべてのテストを実行：

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

特定のテストファイルを実行：

```bash
python -m unittest tests.test_integration
```

## 開発

このプロジェクトはテスト駆動開発（TDD）の原則に従っています：

1. 各モジュールは約100行以下に抑えられています
2. 各パスには対応するユニットテストがあります
3. 統合テストは完全なパイプラインを検証します
4. トラブルシューティングのために各段階でデバッグJSON出力があります

## ライセンス

詳細はLICENSEファイルを参照してください。

※英語版README.mdは、README.ja.mdを元にAI翻訳により生成する予定です
