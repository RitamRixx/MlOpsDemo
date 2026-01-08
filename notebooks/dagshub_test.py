import mlflow
import dagshub


mlflow.set_tracking_uri("https://dagshub.com/RitamRixx/MlOpsDemo.mlflow")

dagshub.init(repo_owner='RitamRixx', repo_name='MlOpsDemo', mlflow=True)

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)