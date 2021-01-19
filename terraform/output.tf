output "public_ip" {
  value = module.instances.public_ip
}

output "db_endpoint" {
  value = module.rds.endpoint
  sensitive = true
}

output "db_name" {
  value = module.rds.name
  sensitive = true
}

output "db_username" {
  value = module.rds.username
  sensitive = true
}

output "db_password" {
  value = module.rds.password
  sensitive = true
}

output "db_port" {
  value = module.rds.port
  sensitive = true
}







