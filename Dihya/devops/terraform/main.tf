# Terraform configuration pour déployer l'infrastructure Dihya Coding
# Respecte sécurité, bonnes pratiques, extensibilité cloud-agnostique

terraform {
  required_version = ">= 1.5.0"
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

# Réseau Docker pour l'app
resource "docker_network" "dihya_net" {
  name = "dihya_network"
}

# Backend Flask
resource "docker_image" "backend" {
  name         = "dihya/backend:latest"
  build {
    context    = "${path.module}/../../docker"
    dockerfile = "Dockerfile.backend"
  }
}

resource "docker_container" "backend" {
  name  = "dihya-backend"
  image = docker_image.backend.latest
  networks_advanced {
    name = docker_network.dihya_net.name
  }
  env = [
    "SECRET_KEY=${var.secret_key}",
    "JWT_SECRET_KEY=${var.jwt_secret_key}",
    "MAIL_SERVER=${var.mail_server}",
    "MAIL_PORT=${var.mail_port}",
    "MAIL_USERNAME=${var.mail_username}",
    "MAIL_PASSWORD=${var.mail_password}",
    "MAIL_DEFAULT_SENDER=${var.mail_default_sender}",
    "BASE_URL=${var.base_url}"
  ]
  ports {
    internal = 5000
    external = 5000
  }
}

# Frontend React
resource "docker_image" "frontend" {
  name         = "dihya/frontend:latest"
  build {
    context    = "${path.module}/../../docker"
    dockerfile = "Dockerfile.frontend"
  }
}

resource "docker_container" "frontend" {
  name  = "dihya-frontend"
  image = docker_image.frontend.latest
  networks_advanced {
    name = docker_network.dihya_net.name
  }
  ports {
    internal = 80
    external = 8080
  }
}

# Variables d'environnement sécurisées
variable "secret_key" {}
variable "jwt_secret_key" {}
variable "mail_server" {}
variable "mail_port" {}
variable "mail_username" {}
variable "mail_password" {}
variable "mail_default_sender" {}
variable "base_url" {}

# Outputs utiles
output "backend_url" {
  value = "http://localhost:5000"
}
output "frontend_url" {
  value = "http://localhost:8080"
}