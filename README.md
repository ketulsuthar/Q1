# Q1
Assessment


# Step for Deploying on GCP

- Create Project on GCP
- docker build -t gcr.io/[Project_ID]/[App_Name]:v1 .
- gcloud auth configure-docker
- docker push gcr.io/[Project_ID]/[App_Name]:v1
- gcloud builds submit --tag gcr.io/[Project_ID]/[App_Name]
- gcloud run deploy --image gcr.io/[Project_ID]/[App_Name]  --platform managed
