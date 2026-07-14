output "api_url" { value = "${aws_apigatewayv2_stage.default.invoke_url}/hello" }
output "function_name" { value = aws_lambda_function.hello.function_name }
output "execution_role_arn" { value = aws_iam_role.lambda.arn }
output "log_group_name" { value = aws_cloudwatch_log_group.lambda.name }
