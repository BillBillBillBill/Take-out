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


# 卖家注册
URL:/seller
Method:POST
Require:username,password,nickname,account_type
Optional:
Token Require: No
Return:{"data": {"id": "seller id"}}

curl example
curl -d '{"username": "test", "password": "test", "nickname": "fuck", "account_type": "P"}' -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/seller


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


# 获取商店列表
URL:/store
Method:GET
Require:
Optional:
Token Require: No
Return:{"data": {"seller_list": [{seller_infor}]}}

curl example
curl http://127.0.0.1:8000/store

# 创建商店
URL:/store
Method:POST
Require:name,address,announcement,description,phone
Optional:
Token Require: Yes
Return:{"data": {"id": "store id"}}

curl example
curl -d '{"token": "20160428011519$bussiness$2$e7c1ad7a$8e0212c482a6ea99ee93c2a5a20f5dbde377c01cd10768accb7524c9d9a76a2a", "name": "testname", "address": "testaddress", "announcement": "testannouncement", "description": "testdescription", "phone": "12345678901"}' -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/store

# 修改商店信息
URL:/store/store_id
Method:PUT
Require:
Optional:name,address,announcement,description,phone
Token Require: Yes
Return:{status_code: 200, data: {}}

curl example
curl -d '{"token": "20160428011519$bussiness$2$e7c1ad7a$8e0212c482a6ea99ee93c2a5a20f5dbde377c01cd10768accb7524c9d9a76a2a", "name": "name", "address": "fuck"}' -X PUT -H "Content-Type:application/json"  http://127.0.0.1:8000/store/1
