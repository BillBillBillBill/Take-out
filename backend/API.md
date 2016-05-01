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
# 顾客注册
URL:/customer
Method:POST
Require:username,password,nickname,account_type
Optional:
Token Require: No
Return:{"data": {"id": "customer id"}}

curl example
curl -d '{"username": "test", "password": "test", "nickname": "fuck", "account_type": "P"}' -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/customer


# 获取顾客列表
URL:/customer
Method:GET
Require:
Optional:
Token Require: No
Return:{"data": {"customer_list": [{customer_infor}]}}

curl example
curl http://127.0.0.1:8000/customer


# 获取单个顾客信息
URL:/customer/customer_id
Method:GET
Require:
Optional:
Token Require: No
Return:{"data": {"customer": customer_infor}}

curl example
curl http://127.0.0.1:8000/customer/1


# 修改顾客信息
URL:/customer/customer_id
Method:PUT
Require:
Optional:password,nickname
Token Require: Yes
Return:{"data": {}}

curl example
curl -d '{"token": "20160430153325$customer$1$a34d6487$c751839117e735773971fb38f1c60823b9d97e352bf439367221e26fb8616b04", "password": "edit", "nickname": "edit"}' -X PUT -H "Content-Type:application/json"  http://127.0.0.1:8000/customer/1



# 获取收货信息列表
URL:/delivery_information
Method:GET
Require:
Optional:
Token Require: Yes
Return:{"data": {"delivery_information_list": [{delivery_information_infor}]}}

curl example
curl -X GET -d '{"token": "20160501014629$customer$1$5d33a5bb$50d6cdd6ddf4a3ec78a10424a67fada17a0f9098b697b652523fb3093aac03e1"}'  http://127.0.0.1:8000/delivery_information

# 添加收货信息
URL:/delivery_information
Method:POST
Require:address, phone, receiver
Optional:
Token Require: Yes
Return:{"data": {"id": "delivery_information id"}}

curl example
curl -d '{"token": "20160501014629$customer$1$5d33a5bb$50d6cdd6ddf4a3ec78a10424a67fada17a0f9098b697b652523fb3093aac03e1", "address": "addressasdasd", "phone": "18888888888", "receiver": "黄先生"}' -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/delivery_information

# 获取单个收货信息
URL:/delivery_information/delivery_information_id
Method:GET
Require:
Optional:
Token Require: No
Return:{"data": {"delivery_information": delivery_information_infor}}

curl example
curl http://127.0.0.1:8000/delivery_information/1

# 修改收货信息
URL:/delivery_information/delivery_information_id
Method:PUT
Require:
Optional:address, phone, receiver
Token Require: Yes
Return:{"data": {}}

curl example
curl -d '{"token": "20160501014629$customer$1$5d33a5bb$50d6cdd6ddf4a3ec78a10424a67fada17a0f9098b697b652523fb3093aac03e1", "receiver": "黄小姐"}' -X PUT -H "Content-Type:application/json"  http://127.0.0.1:8000/delivery_information/1

# 删除收货信息
URL:/delivery_information/delivery_information_id
Method:DELETE
Require:
Optional:
Token Require: Yes
Return:{"data": {}}

curl example
curl -d '{"token": "20160501014629$customer$1$5d33a5bb$50d6cdd6ddf4a3ec78a10424a67fada17a0f9098b697b652523fb3093aac03e1"}' -X DELETE -H "Content-Type:application/json"  http://127.0.0.1:8000/delivery_information/1



# 获取投诉列表(发出)
URL:/complaint
Method:GET
Require:
Optional:
Token Require: Yes
Return:{"data": {"complaint_list": [{complaint_infor}]}}

curl example
curl -X GET -d '{"token": "20160501014629$customer$1$5d33a5bb$50d6cdd6ddf4a3ec78a10424a67fada17a0f9098b697b652523fb3093aac03e1"}' http://127.0.0.1:8000/complaint

# 添加投诉信息
URL:/complaint
Method:POST
Require:content, store_id
Optional:
Token Require: Yes
Return:{"data": {"id": "complaint id"}}

curl example
curl -d '{"token": "20160501014629$customer$1$5d33a5bb$50d6cdd6ddf4a3ec78a10424a67fada17a0f9098b697b652523fb3093aac03e1", "content": "asdasdasd", "store_id": "1"}' -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/complaint

# 获取单个投诉信息
URL:/complaint/complaint_id
Method:GET
Require:
Optional:
Token Require: No
Return:{"data": {"complaint": complaint_infor}}

curl example
curl http://127.0.0.1:8000/complaint/1

# 修改投诉信息
URL:/complaint/complaint_id
Method:PUT
Require:
Optional:status
Token Require: Yes
Return:{"data": {}}

curl example
curl -d '{"token": "20160501014629$customer$1$5d33a5bb$50d6cdd6ddf4a3ec78a10424a67fada17a0f9098b697b652523fb3093aac03e1", "status": "R"}' -X PUT -H "Content-Type:application/json"  http://127.0.0.1:8000/complaint/1



# 获取订单列表
URL:/order
Method:GET
Require:
Optional:
Token Require: Yes
Return:{"data": {"order_list": [{order_infor}]}}

curl example
curl -X GET -d '{"token": "20160501014629$customer$1$5d33a5bb$50d6cdd6ddf4a3ec78a10424a67fada17a0f9098b697b652523fb3093aac03e1"}' http://127.0.0.1:8000/order

# 添加订单信息
URL:/order
Method:POST
Require:food_list, delivery_information_id, store_id
Optional:note
Token Require: Yes
Return:{"data": {"id": "order id"}}

curl example
curl -d '{"token": "20160501014629$customer$1$5d33a5bb$50d6cdd6ddf4a3ec78a10424a67fada17a0f9098b697b652523fb3093aac03e1", "food_list": [{"food_id": "1", "count": "2"}, {"food_id": "2", "count": "3"}], "delivery_information_id": "1", "store_id": "1"}' -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/order

# 获取单个订单信息
URL:/order/order_id
Method:GET
Require:
Optional:
Token Require: No
Return:{"data": {"order": order_infor}}

curl example
curl http://127.0.0.1:8000/order/1

# 修改订单信息
URL:/order/order_id
Method:PUT
Require:
Optional:status
Token Require: Yes
Return:{"data": {}}

curl example
curl -d '{"token": "20160501014629$customer$1$5d33a5bb$50d6cdd6ddf4a3ec78a10424a67fada17a0f9098b697b652523fb3093aac03e1", "status": "5"}' -X PUT -H "Content-Type:application/json"  http://127.0.0.1:8000/order/1
==============================================================================
# 管理员注册
URL:/admin
Method:POST
Require:username,password,nickname,account_type
Optional:
Token Require: No
Return:{"data": {"id": "admin id"}}

curl example
curl -d '{"username": "test", "password": "test", "nickname": "fuck", "account_type": "P"}' -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/admin


# 获取管理员列表
URL:/admin
Method:GET
Require:
Optional:
Token Require: No
Return:{"data": {"admin_list": [{admin_infor}]}}

curl example
curl http://127.0.0.1:8000/admin


# 获取单个管理员信息
URL:/admin/admin_id
Method:GET
Require:
Optional:
Token Require: No
Return:{"data": {"admin": admin_infor}}

curl example
curl http://127.0.0.1:8000/admin/1


# 修改管理员信息
URL:/admin/admin_id
Method:PUT
Require:
Optional:password,nickname
Token Require: Yes
Return:{"data": {}}

curl example
curl -d '{"token": "", "password": "edit", "nickname": "edit"}' -X PUT -H "Content-Type:application/json"  http://127.0.0.1:8000/admin/1
