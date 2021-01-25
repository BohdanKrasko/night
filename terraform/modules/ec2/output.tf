output "public_ip" {
  value = aws_instance.ec2[0].public_ip
}

output "public_dns" {
  value = aws_instance.ec2[0].public_dns
}
