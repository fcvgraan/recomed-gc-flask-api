gcloud projects create recomed-gc-python-api-v1 --name=recomed-gc-python-api --set-as-default

BILLING_ACCOUNT=$(gcloud beta billing accounts list --format 'value(name)' --filter=open=true)
gcloud beta billing projects link create recomed-gc-python-api-v1 --billing-account $BILLING_ACCOUNT

gcloud services enable cloudfunctions.googleapis.com
gcloud services enable cloudbuild.googleapis.com  

gcloud functions deploy calculate-business-seconds --entry-point http_trigger --region europe-west1 --runtime python37 --trigger-http --allow-unauthenticated