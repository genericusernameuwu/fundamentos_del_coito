variable "aws_region" {
  description = "Region de AWS"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Nombre base del proyecto"
  type        = string
  default     = "lab-iac-web"

  validation {
    condition = (
      can(regex("^[a-z0-9-]+$", var.project_name)) &&
      !startswith(var.project_name, "-") &&
      !endswith(var.project_name, "-") &&
      length(var.project_name) <= 41
    )
    error_message = "project_name debe usar solo letras minusculas, numeros y guiones, no puede comenzar o terminar con '-', y debe tener como maximo 41 caracteres para mantener valido el nombre del bucket S3."
  }
}

variable "db_name" {
  description = "Nombre de la base de datos"
  type        = string
  default     = "appdb"
}

variable "db_username" {
  description = "Usuario administrador de MySQL"
  type        = string
  default     = "admin"
}

variable "db_password" {
  description = "Password administrador de MySQL"
  type        = string
  sensitive   = true
}
