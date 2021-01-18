output "public_ip" {
  value = module.instances.public_ip
}

output "db_endpoint" {
  value = module.rds.endpoint
}

output "db_name" {
  value = module.rds.name
}

output "db_username" {
  value = module.rds.username
}

output "db_password" {
  value = module.rds.password
}

output "db_port" {
  value = module.rds.port
}







