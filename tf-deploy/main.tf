terraform {
  required_version = ">= 0.12"
}

terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = ">= 2.0.0"
    }
  }
}

terraform {
  cloud {
    organization = "ankjnn"

    workspaces {
      name = "gh-actions-eks-deploy"
    }
  }
}

provider "kubernetes" {
  config_path = "./eks-config"
}
resource "kubernetes_namespace" "zerohash" {
  metadata {
    name = "zerohash"
  }
}
resource "kubernetes_deployment" "zerohash" {
  metadata {
    name      = "nginx"
    namespace = kubernetes_namespace.test.metadata.0.name
  }
  spec {
    replicas = 1
    selector {
      match_labels = {
        app = "MyTestApp"
      }
    }
    template {
      metadata {
        labels = {
          app = "MyTestApp"
        }
      }
      spec {
        container {
          image = "nginx:latest"
          name  = "nginx-container"
          port {
            container_port = 80
          }
        }
      }
    }
  }
}
resource "kubernetes_service" "test" {
  metadata {
    name      = "nginx"
    namespace = kubernetes_namespace.test.metadata.0.name
  }
  spec {
    selector = {
      app = kubernetes_deployment.test.spec.0.template.0.metadata.0.labels.app
    }
    type = "NodePort"
    port {
      node_port   = 31111
      port        = 80
      target_port = 80
    }
  }
}
