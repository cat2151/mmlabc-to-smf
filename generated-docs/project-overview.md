Last updated: 2025-11-03

# Project Overview

## プロジェクト概要
- Music Macro Language (MML) 形式の音楽データをStandard MIDI File (SMF) へ変換するツールです。
- 包括的なデバッグ出力を備えた4パスアーキテクチャを採用し、正確かつ信頼性の高い変換を実現します。
- 音楽制作やデータ変換のワークフローをサポートし、MML利用者の利便性を高めることを目的としています。

## 技術スタック
- フロントエンド: 
- 音楽・オーディオ: 
    - Tone.js: Web Audio APIを抽象化し、ブラウザ上で高度な音声処理を可能にするJavaScriptライブラリです。
    - Web Audio API: ウェブブラウザ上で音声の処理や合成を行うためのAPIで、Tone.js経由で利用されます。
    - MML (Music Macro Language): 音楽をテキスト形式で記述するための記法であり、このプロジェクトの入力データ形式です。
- 開発ツール: 
    - Node.js runtime: JavaScriptコードを実行するためのオープンソースのサーバーサイド実行環境です。
- テスト: 
- ビルドツール: 
- 言語機能: 
- 自動化・CI/CD: 
    - GitHub Actions: コードの変更に基づいてビルド、テスト、デプロイなどのワークフローを自動化するCI/CDサービスです。
        - プロジェクト要約自動生成: プロジェクトの概要情報を自動的に生成します。
        - Issue自動管理: GitHub Issuesの管理を自動化します。
        - README多言語翻訳: READMEファイルを複数の言語に自動翻訳します。
        - i18n automation: 国際化（i18n）関連の自動翻訳ワークフローを指します。
- 開発標準: 
    - EditorConfig: 異なるエディタやIDE間でコードのスタイル（インデント、改行など）を統一するための設定ファイルです。

## ファイル階層ツリー
```
📄 .editorconfig
📄 .gitignore
📁 .vscode/
  📊 settings.json
📄 LICENSE
📖 README.ja.md
📖 README.md
📄 _config.yml
📁 generated-docs/
📁 issue-notes/
  📖 4.md
📄 mml_to_smf.py
📄 pytest.ini
📄 requirements.txt
📄 ruff.toml
📄 setup.py
📁 src/
  📄 __init__.py
  📄 pass1_parser.py
  📄 pass2_ast.py
  📄 pass3_events.py
  📄 pass4_midi.py
📁 tests/
  📄 __init__.py
  📄 test_integration.py
  📄 test_pass1.py
  📄 test_pass2.py
  📄 test_pass3.py
  📄 test_pass4.py
```

## ファイル詳細説明
-   `.editorconfig`: コードエディタ間でインデントスタイルや文字コードなどのコーディングスタイルを統一するための設定ファイルです。
-   `.gitignore`: Gitがバージョン管理の対象としないファイルやディレクトリを指定するファイルです。
-   `.vscode/settings.json`: Visual Studio Codeエディタのプロジェクト固有の設定（ワークスペース設定）を定義するファイルです。
-   `LICENSE`: このプロジェクトのソフトウェアライセンス情報が記載されています。
-   `README.ja.md`: プロジェクトの概要、使い方、特徴などを日本語で説明する主要なドキュメントファイルです。
-   `README.md`: プロジェクトの概要、使い方、特徴などを英語で説明する主要なドキュメントファイルです。
-   `_config.yml`: Jekyllなどの静的サイトジェネレーターで使用される設定ファイルで、サイトのビルドに関するメタデータやオプションを定義します。
-   `generated-docs/`: プロジェクトから自動生成されたドキュメントやレポートを格納するためのディレクトリです。
-   `issue-notes/4.md`: 特定のIssue（GitHub Issue #4 など）に関する詳細なメモや情報が記載されたファイルです。
-   `mml_to_smf.py`: Music Macro Language (MML) から Standard MIDI File (SMF) への変換処理全体を統括するメインスクリプトです。
-   `pytest.ini`: Pythonのテストフレームワーク`pytest`の設定ファイルで、テストの実行方法やオプションを定義します。
-   `requirements.txt`: このPythonプロジェクトが依存する外部ライブラリとそのバージョンを一覧表示するファイルです。
-   `ruff.toml`: Pythonの高速リンターおよびフォーマッターである`ruff`の設定ファイルで、コードの品質チェックや整形ルールを定義します。
-   `setup.py`: Pythonパッケージのセットアップスクリプトで、プロジェクトのインストール、配布、メタデータなどを定義するために使用されます。
-   `src/__init__.py`: `src`ディレクトリをPythonのパッケージとして扱うために必要な初期化ファイルです。
-   `src/pass1_parser.py`: MML文字列を解析し、トークン列に変換する「パス1」の処理を実装しています。
-   `src/pass2_ast.py`: パス1で生成されたトークン列を基に、抽象構文木（AST）を構築する「パス2」の処理を実装しています。
-   `src/pass3_events.py`: パス2で生成されたASTから、MIDIイベント（音符、テンポ変更など）を生成する「パス3」の処理を実装しています。
-   `src/pass4_midi.py`: パス3で生成されたMIDIイベントデータを用いて、最終的なStandard MIDI Fileを生成する「パス4」の処理を実装しています。
-   `tests/__init__.py`: `tests`ディレクトリをPythonのパッケージとして扱うために必要な初期化ファイルです。
-   `tests/test_integration.py`: プロジェクト全体の統合的な動作を検証するためのテストコードを格納しています。
-   `tests/test_pass1.py`: パス1（MMLパーサー）の機能が正しく動作するかを検証する単体テストです。
-   `tests/test_pass2.py`: パス2（AST構築）の機能が正しく動作するかを検証する単体テストです。
-   `tests/test_pass3.py`: パス3（MIDIイベント生成）の機能が正しく動作するかを検証する単体テストです。
-   `tests/test_pass4.py`: パス4（MIDIファイル生成）の機能が正しく動作するかを検証する単体テストです。

## 関数詳細説明
-   `mml_to_smf.py` 内のメイン変換関数 (例: `convert_mml_to_smf`)
    -   役割: MML文字列を受け取り、4つのパスを通してSMFデータを生成し、ファイルとして保存する一連の処理を調整します。
    -   引数: `mml_string` (str, MML形式の文字列), `output_filepath` (str, 出力するSMFファイルのパス)
    -   戻り値: なし (または生成されたSMFデータのバイト列)
    -   機能: パス1からパス4までの各処理を順に呼び出し、MMLからSMFへの変換フロー全体を管理します。

-   `src/pass1_parser.py` 内の解析関数 (例: `parse_mml_to_tokens`)
    -   役割: MML文字列を解析し、構文要素を表すトークンのリストに変換します。
    -   引数: `mml_string` (str, MML形式の文字列)
    -   戻り値: `list` (MMLトークンのリスト)
    -   機能: MMLの各記号やコマンド（例: 'C4', 'L8', '>'' など）を識別し、意味のある単位（トークン）に分解します。

-   `src/pass2_ast.py` 内のAST構築関数 (例: `build_ast_from_tokens`)
    -   役割: トークンのリストから、MMLの構造を表現する抽象構文木（AST）を構築します。
    -   引数: `tokens` (list, パス1で生成されたトークンのリスト)
    -   戻り値: `ASTNode` (MMLの構文ツリーのルートノード)
    -   機能: トークンの順序と関係性に基づいて、階層的なデータ構造を生成し、MMLの論理構造を表現します。

-   `src/pass3_events.py` 内のイベント生成関数 (例: `generate_events_from_ast`)
    -   役割: 抽象構文木（AST）を走査し、タイムライン上に配置されるMIDIイベントのリストを生成します。
    -   引数: `ast_root` (ASTNode, パス2で生成されたASTのルートノード)
    -   戻り値: `list` (MIDIイベントオブジェクトのリスト)
    -   機能: ASTの各ノードをMIDIメッセージ（ノートオン、ノートオフ、テンポチェンジなど）に変換し、正確なタイミングで並べます。

-   `src/pass4_midi.py` 内のMIDIファイル生成関数 (例: `create_smf_from_events`)
    -   役割: MIDIイベントのリストから、Standard MIDI File (SMF) 形式のバイナリデータを生成します。
    -   引数: `midi_events` (list, パス3で生成されたMIDIイベントのリスト)
    -   戻り値: `bytes` (SMF形式のバイナリデータ)
    -   機能: MIDIイベントをSMF仕様に準拠したフォーマットでエンコードし、ヘッダーチャンクやトラックチャンクを含む完全なMIDIファイルデータを構築します。

-   `tests/test_*.py` 内のテスト関数 (例: `test_pass1_basic_mml`)
    -   役割: 各パスまたは機能が期待通りに動作するかを検証します。
    -   引数: なし (通常、テストデータは関数内で用意されるか、テストフィクスチャとして提供されます)
    -   戻り値: なし (テストフレームワークによって結果が報告されます)
    -   機能: 特定の入力に対して出力が正しいか、エラーが適切に処理されるかなどをアサート（検証）します。

## 関数呼び出し階層ツリー
```
関数呼び出し階層を分析できませんでした。

---
Generated at: 2025-11-03 07:04:46 JST
