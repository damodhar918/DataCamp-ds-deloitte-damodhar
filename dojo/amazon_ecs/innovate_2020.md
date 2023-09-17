---
title: 実践的 AWS コンテナ運用ガイド -モニタリング、ロギング、デプロイ、スケーリングの実現方法
tags: amazon-ec2-container-service
url: -
---

# イントロダクション
## アプリケーションをコンテナ化する背景
- Run Anywhere
    - 複数環境に渡る一貫した実現可能性
    - Portability
    - 可搬性の高さ
    - コンテナイメージの作成 (build)、レジストリ、アップロード (push)、ダウン
- ロード (pull) に代表される、可搬性の高さをささえるエコシステム
    - Isolated processes
    - コンテナによるプロセスレベルのリソースアイソレーション、それによる
- CPU やメモリに代表されるリソースの柔軟な割り当て、高速な起動と停止

## ECS 上にデプロイされた、あるアプリケーションのシナリオ
- EC2 上で動いていた WEB アプリケーションをデリバリ速度の向上を目指し、コンテナ化
- コンテナを使ったアプリケーションの運用は初めて
- Application Load Balancer、Amazon ECS/Fargate、Amazon RDS というアーキテクチャ
- マネージメントコンソールから ECS にデプロイし動作することまでは確認済み

# コンテナ化アプリケーションの運用における課題とその解決方法
## 課題1: より詳細なモニタリング
- 負荷テストの結果、 ECS上のサービスが想定されたパフォーマンスを出していない
- CloudWatch のデフォルトのメトリクスではタスク、コンテナ単位のメトリクスが取れず、リソースの配分が難しい

**解決**
- Amazon Cloud Watch Container Insights を使って適切なリソース配分を見極める
    - Container Insights はコンテナ単位のリソースモニタリングが可能
    - 適切なリソース配分により、効率的かつ安全に運用できるリソースを割り当てる
    - Container Insights のダッシュボードを起点により詳細な分析が可能
	    1. ECS TasksからContainer performanceを確認
		2. ECSタスク定義にてタスク内のコンテナリソース配分を変更する
		3. Container Insightsからリソース使用状況を確認

## 課題2: ログの柔軟なルーティング
- Nginx のアクセスログは現状の運⽤通り、S3 に格納したいがCloudWatch Logs 経由でのログの転送となっている
- ログの種類に応じて、格納先に タスクから柔軟に転送してCloudWatch Logs のコスト最適化をしたい

**解決**
- Amazon ECS の FireLens をログドライバーとして利用する
- Fluentd または Fluent Bit のログルーターコンテナがサイドカーとして実行され、カスタム設定により柔軟なログの保存が可能
    - ECS のコンテナの標準出力/標準エラー出力を、 Fluentd またはFluent Bit に簡単にルーティングできる機能
    - AWS サービスまたは Third Party 製ツールの宛先にログをルーティング可能
    - Fluent bit は C言語で実装されている。 Fluentd の方が機能は豊富だが、軽量でコンテナのサイドカーに最適

## 課題3: ECS へのデプロイの自動化について
- ソースコードとコンテナイメージのアップロード、Serviceの更新をそれぞれ手動でおこなっており、デプロイに疲弊している
- 手作業でのデプロイの結果オペレーションミスによるトラブルが頻発している

**解決**
- 手動セットアップ、手動デプロイ
    - 増え続ける負担による開発速度の低下
    - 秘伝のタレ化されたデプロイ手動により、人依存が進み組織の拡大を遮る
- 可能な限りすべてを自動化
    - 自動化されたデプロイにより開発速度の向上
    - すべてのプロセスが自動化されることにより、人依存ではなくコードに依存したデプロイで組織の拡大が容易になる

## 課題4: タスク数のオートスケーリング の設定
- アプリケーションの特性上、日によってアクセスがばらつきがあり、ECS サービスの Auto Scaling を設定することになった
- ステップスケーリングポリシーでの Auto Scaling を設定しているが、スケールアウト・インの設定が複雑

**解決**
- Target Tracking を利用したサービスのスケーリングをおこなう
- メトリクスに対してターゲットとなる値を設定するだけ (e.g. CPU 仕様率 50%)
- 指定値に近づくようにApplication Auto Scaling が自動的にサービスの DesiredCount を調整
- 以下のメトリクスを設定可能
    - ECSServiceAverageCPUUtilization
    - ECSServiceAverageMemoryUtilization
    - ALBRequestCountPerTarget

# Reference
- https://pages.awscloud.com/rs/112-TZM-766/images/%5BS-12%5DAWSInnovate_Online_Conference_2020_Spring_Container_Operation_ans.pdf
