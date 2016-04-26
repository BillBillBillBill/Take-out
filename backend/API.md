API接口说明

# 登陆
URL:/api-token-auth/account_type
Method:POST
Require:username,password
Optional:
Token Require: No
Return:{"data": {"token": "Your token"}}

curl example
curl -d '{"username": "test", "password": "test"}' -X POST http://127.0.0.1:8000/api-token-auth/bussiness


# 注册
URL:/seller
Method:POST
Require:username,password,nickname,account_type
Optional:
Token Require: No
Return:{"data": {"token": "Your token"}}

curl example
curl -d '{"username": "test3", "password": "test", "nickname": "fuck", "account_type": "P"}' -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/seller


# 获取卖家列表
URL:/seller
Method:GET
Require:
Optional:
Token Require: No
Return:{"data": {"seller_list": [{seller_infor}]}}

curl example
curl http://127.0.0.1:8000/seller


# 获取单个卖家信息
URL:/seller/seller_id
Method:GET
Require:
Optional:
Token Require: No
Return:{"data": {"seller": seller_infor}}

curl example
curl http://127.0.0.1:8000/seller/1


# 修改卖家信息
URL:/seller/seller_id
Method:PUT
Require:
Optional:password,nickname
Token Require: Yes
Return:{status_code: 200, data: {}}

curl example
curl -d '{"token": "asdasdasd", "password": "test", "nickname": "fuck"}' -X PUT -H "Content-Type:application/json"  http://127.0.0.1:8000/seller/1
