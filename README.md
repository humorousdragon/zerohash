# ZeroHash Spot Price Application
This is simple application which fetches spot prices for BTC for various currencies e.g USD, EUR, GBP, JPY etc. by hitting coinbase api and provides output in json format on exposed endpoints e.g.\
[USD spot price](https://spot.zerohash.online/USD)  
This application is developed using python programming language and with flask framework and it runs on port **8080**.

## Please access UI for current setup using following links:

- Root endpoint is exposed here [Spot price root url](https://spot.zerohash.online/), UI page can be developed using html, css, js if needed. You can pass currency code (e.g. USD, GBP, EUR etc.) at the end of url like \<endpoint url\>/\<currency> to get the spot price. Health endpoint is also exposed on [health url](https://spot.zerohash.online/health).
- Kubernetes cluster dashboard can be accessed here [Kubernetes Dashboard](https://spot.zerohash.online:444), token for login can be found in dash-token file. On this dashboard you can check all kubernetes resources running on the cluster and within all namespaces.  

### Information about directories/files in this repo:
This repo contains code files, pipeline file, dockerfile, helm charts, terraform code, test files etc.
- Code is written in *app.py* file. There is file for unit tests *test_app.py*. There is requirements.txt file which is used to install libraries/packages required by the application to run.
- It contains *Dockerfile* which is used to create docker image of the application.
- *Helm* folder contains helm charts, files for creating kubernetes resources such as deployment and service.
- *tf-deploy* folder contains terraform file(s) to deploy resources on the kubernetes cluster.
- *.gihub/workflow* directory has pipeline file (deploy.yml) which run various jobs with github actions.  

**Note:** As of now helm charts are being used to deploy application on the cluster, terraform is deploying nginx on cluster in *zerohash* namespace and have been created just for testing purposes.  

## To deploy application on EKS Cluster using CI/CD:
First we would need an EKS cluster. If it is setup then get credentials e.g. kubeconfig file so that request to deploy on cluster can be authorized. Get base64 of kubeconfig file by running `cat kubeconfig | base64` and store the output on repository as secret with key name as `KUBECONFIG`.

1. `git clone` this repo to your computer.
2. Write your code or make changes to code file which is *app.py*.
3. Make changes to Dockerfile if needed.
4. Add changes by runnig `git add` and specifying files.
5. Commit your changes by running `git commit -m "Description"`
6. Push the code to the repo by running `git push -u origin master` after committing the changes.
7. This will trigger the CI/CD workflow pipeline, with github actions, as pipeline file (.github/workflows/deploy.yml) has been added to the repo. This pipeline will run few jobs as explained below.  
Once this job completes we should see deployment on the kubernetes cluster.  

## Explaination about Pipeline:
**Github actions** is being used to run CI/CD pipeline, which automates the process of testing, building docker image and deploying it on the kubernetes cluster. This pipeline is triggered on push to the master branch event. These jobs are configured in `.github/workflows/deploy.yml` file and are as follows:
1. First job will do basic unit testing of the code using `pytest`.
2. Second job is to build docker images and push this image to ECR.
3. Third job is to deploy resources on kubernetes cluster using helm charts.
4. Fourth job is to perform api testing of the application running on the cluster which we deployed in 3rd job.
5. Fifth job is to test deployment of resources on cluster using terraform.

I hope to keep working on this and improve it wherever possible.