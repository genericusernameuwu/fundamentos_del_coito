output "frontend_website_url" {
  value = format("http://%s", aws_s3_bucket_website_configuration.frontend.website_endpoint)
}

output "api_base_url" {
  value = trimsuffix(aws_apigatewayv2_stage.api_stage.invoke_url, "/")
}

output "rds_endpoint" {
  value = aws_db_instance.mysql.address
}
