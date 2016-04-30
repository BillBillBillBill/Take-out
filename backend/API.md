API接口说明

请求成功格式：
{"status_code": 200, "data": xxx}

请求失败格式：
{"status_code": 4xx, "message": xxx}


# 文件(图片)上传
URL:/upload
Method:POST
Require:
Optional:
Token Require: Yes
Return:{"data": {"id": file_id}}

curl example
curl -H 'Authorization-Token: 20160428011519$bussiness$2$e7c1ad7a$8e0212c482a6ea99ee93c2a5a20f5dbde377c01cd10768accb7524c9d9a76a2a' -F 'image=@/home/bill/Desktop/files/头像.jpg' http://127.0.0.1:8000/upload

# 登陆
URL:/api-token-auth/account_type
Method:POST
Require:username,password
Optional:
Token Require: No
Return:{"data": {"token": "Your token"}}

curl example
curl -d '{"username": "test", "password": "test"}' -X POST http://127.0.0.1:8000/api-token-auth/bussiness

==============================================================================
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
Return:{"data": {}}

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
Optional:image_ids
Token Require: Yes
Return:{"data": {"id": "store id"}}

curl example
curl -d '{"token": "20160428011519$bussiness$2$e7c1ad7a$8e0212c482a6ea99ee93c2a5a20f5dbde377c01cd10768accb7524c9d9a76a2a", "name": "testname", "address": "testaddress", "announcement": "testannouncement", "description": "testdescription", "phone": "12345678901", "image_ids": "1,3"}' -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/store

# 获取单个商店信息
URL:/store/store_id
Method:GET
Require:
Optional:
Token Require: No
Return:{"data": {"store": store_infor}}

curl example
curl http://127.0.0.1:8000/store/1

# 修改商店信息
URL:/store/store_id
Method:PUT
Require:
Optional:name,address,announcement,description,phone
Token Require: Yes
Return:{"data": {}}

curl example
curl -d '{"token": "20160428011519$bussiness$2$e7c1ad7a$8e0212c482a6ea99ee93c2a5a20f5dbde377c01cd10768accb7524c9d9a76a2a", "name": "name", "address": "fuck"}' -X PUT -H "Content-Type:application/json"  http://127.0.0.1:8000/store/1



# 获取食物列表
URL:/food
Method:GET
Require:store_id
Optional:
Token Require: No
Return:{"data": {"food_list": [{food_infor}]}}

curl example
curl -X GET -d '{"store_id": 1}' http://127.0.0.1:8000/food

# 创建食物
URL:/food
Method:POST
Require:name, description, price, stock
Optional:image_ids
Token Require: Yes
Return:{"data": {"id": "food id"}}

curl example
curl -d '{"token": "20160428011519$bussiness$2$e7c1ad7a$8e0212c482a6ea99ee93c2a5a20f5dbde377c01cd10768accb7524c9d9a76a2a", "name": "foodname", "description": "gggggg", "price": 12.34, "stock": 100, "image_ids": "1,3"}' -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/food

# 获取单个食物信息
URL:/food/food_id
Method:GET
Require:
Optional:
Token Require: No
Return:{"data": {"food": food_infor}}

curl example
curl http://127.0.0.1:8000/food/1

# 修改食物信息
URL:/food/food_id
Method:PUT
Require:
Optional:name, description, price, stock
Token Require: Yes
Return:{"data": {}}

curl example
curl -d '{"token": "20160428011519$bussiness$2$e7c1ad7a$8e0212c482a6ea99ee93c2a5a20f5dbde377c01cd10768accb7524c9d9a76a2a", "name": "name", "description": "asddddddddd"}' -X PUT -H "Content-Type:application/json"  http://127.0.0.1:8000/food/1

# 删除食物
URL:/food/food_id
Method:DELETE
Require:
Optional:
Token Require: Yes
Return:{"data": {}}

curl example
curl -d '{"token": "20160428011519$bussiness$2$e7c1ad7a$8e0212c482a6ea99ee93c2a5a20f5dbde377c01cd10768accb7524c9d9a76a2a"}' -X DELETE -H "Content-Type:application/json"  http://127.0.0.1:8000/food/1

==============================================================================


==============================================================================