# lab-iac-web

Laboratorio de Infrastructure as Code para AWS con Terraform, basado en el enunciado del taller. La arquitectura implementada es:

S3 static website -> API Gateway HTTP API -> Lambda -> RDS MySQL

## Arquitectura general

- Amazon S3 aloja el frontend estatico.
- API Gateway expone la ruta `GET /items`.
- Lambda ejecuta la logica en Python.
- RDS MySQL persiste los datos.
- Lambda y RDS viven dentro de una VPC con dos subredes privadas.

## Estructura

```text
lab-iac-web/
|-- main.tf
|-- variables.tf
|-- terraform.tfvars
|-- outputs.tf
|-- providers.tf
|-- network.tf
|-- s3.tf
|-- iam.tf
|-- lambda.tf
|-- apigateway.tf
|-- rds.tf
|-- lambda_src/
|   `-- app.py
`-- README.md
```

## Prerequisitos

- Terraform 1.5.0 o superior
- Credenciales AWS configuradas localmente
- Python y `pip`

Paso previo importante para incluir la dependencia de MySQL dentro del paquete de Lambda:

```bash
pip install pymysql -t lambda_src/
```

## Comandos de trabajo

Desde la carpeta `lab-iac-web/`:

```bash
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
```

## Como validar

1. Abrir la URL entregada por `frontend_website_url` en el navegador.
2. Presionar el boton `Consultar API`.
3. Verificar que se muestre un JSON con el mensaje de conexion y la cantidad de registros.
4. Probar la API directamente:

```bash
curl "$(terraform output -raw api_base_url)/items"
```

## Advertencias

- Este laboratorio crea recursos con costo, especialmente RDS.
- Al terminar la actividad, destruir los recursos para evitar cargos:

```bash
terraform destroy
```
