output "application_url" { value = "http://${aws_lb.this.dns_name}" }
output "asg_name" { value = aws_autoscaling_group.web.name }
output "target_group_arn" { value = aws_lb_target_group.web.arn }
