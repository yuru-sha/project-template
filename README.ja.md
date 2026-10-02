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


## 1コマンドでのプロジェクト作成

新規リポジトリは、GitHub画面から手動で作成するより、次のラッパーを使う運用を推奨します。

```sh
bash scripts/create-project.sh yuru-sha/my-project
```

Privateリポジトリの場合:

```sh
bash scripts/create-project.sh yuru-sha/my-project --private
```

このスクリプトは以下を自動で行います。

1. `yuru-sha/project-template` からリポジトリを作成
2. GitHub規定ラベルはそのまま維持
3. 共通追加ラベルを作成・更新
4. `orca:*` ライフサイクルラベルを作成・更新

必要環境は、認証済みの GitHub CLI (`gh`) と Python 3 です。

ラベル定義の正本は [`yuru-sha/project-template/.github/labels.json`](.github/labels.json) のみに置きます。同期処理は冪等なので、既存リポジトリにも適用できます。

```sh
python3 scripts/sync-labels.py --repo yuru-sha/existing-project
```

同梱のGitHub Actions Workflowは毎日 `yuru-sha/project-template` の正本ラベル定義を取得して同期し、手動実行も可能です。これにより各リポジトリ側でラベル定義を個別管理する必要はありません。
