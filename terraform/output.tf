output "public_ip" {
  value = module.instances.public_ip
}

output "public_dns" {
  value = module.instances.public_dns
}

output "db_address" {
  value = module.rds.address
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







