# Project Name

> テンプレートからリポジトリを作成したら、このファイルをプロジェクト向けに更新してください。

このプロジェクトの目的と対象ユーザーを簡潔に記載します。

[English](README.md)

## 必要環境

必要なランタイム、ツールチェーン、外部サービスを記載します。

## セットアップ

```sh
# このプロジェクトの標準セットアップコマンドを記載します。
```

## 開発

開発・テスト・Lint・Format・Type check・Build の標準コマンドを記載します。`AGENTS.md` と内容を一致させてください。

## ドキュメント

詳細なプロジェクト文書は [`docs/`](docs/) 以下に配置します。

## コントリビューション

[CONTRIBUTING.md](CONTRIBUTING.md) を参照してください。

## ライセンス

MIT License。[LICENSE](LICENSE) を参照してください。


## 新規プロジェクトの開始

このテンプレートからリポジトリを作成したら、次の順で初期化します。

1. `README.md` と `README.ja.md` のプロジェクト名・説明を置き換える。
2. `AGENTS.md` に実際のセットアップ・検証コマンドを記載する。
3. [`templates/`](templates/) から使用言語に必要な差分だけを適用する。
4. `.gitignore` は実際に生成される成果物だけを追加する。
5. CI / Workflow はプロジェクト固有として各リポジトリで管理する。
6. GitHubの自動Release Notesを使う前に、`.github/release.yml` と実際のラベル体系が一致しているか確認する。

Issue / Pull Request の共通デフォルトは [`yuru-sha/.github`](https://github.com/yuru-sha/.github) で管理します。
