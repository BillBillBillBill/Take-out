<script>
  export default {
  	name: "Orderdetail",
  	data: function() {
  		return {
  			grade: 0,
  			isShow: false,
  			orders: [
        	{bussiness: 'aaa',
         	picture: 'images/flower.jpg',
         	address: 'qwertyu',
        	tel: '12345678900',
         	orderid: "order1",
         	total: 10,
         	date: '2016-03-24',
         	order_list: [
         	{food_name: 'a',
          	amount: 3,
          	picture: 'images/flower.jpg',
          	count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          	star: 3,
          	price: 5
          	},
         	{food_name: 'b',
         	picture: 'images/flower.jpg',
          	amount: 3,
          	star:2,
          	price: 5
          },
         {food_name: 'c',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 4,
          price: 5
          },
         {food_name: 'd',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 3,
          price: 5
          },
         {food_name: 'e',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 5,
          price: 5
          }],
         status: '未处理'
         },
         {bussiness: 'bbb',
         picture: 'images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order2",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 2,
          price: 5
          },
         {food_name: 'b',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star:1,
          price: 5
          },
         {food_name: 'c',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star:4,
          price: 5
          },
         {food_name: 'd',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 5,
          price: 5
          },
         {food_name: 'e',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 3,
          price: 5
          }],
         status: '已完成'
         },
         {bussiness: 'ccc',
         picture: 'images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order3",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 4,
          price: 5
          },
         {food_name: 'b',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 2,
          price: 5
          },
         {food_name: 'c',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 4,
          price: 5
          },
         {food_name: 'd',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 1,
          price: 5
          },
         {food_name: 'e',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 5,
          price: 5
          }],
         status: '配送中'
         },
         {bussiness: 'ddd',
         picture: 'images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order4",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 4,
          price: 5
          },
         {food_name: 'b',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 2,
          price: 5
          },
         {food_name: 'c',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 3,
          price: 5
          },
         {food_name: 'd',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 3,
          price: 5
          },
         {food_name: 'e',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 4,
          price: 5
          }],
         status: '已接单'
         },
         {bussiness: 'eee',
         picture: 'images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order5",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 2,
          price: 5
          },
         {food_name: 'b',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 5,
          price: 5
          },
         {food_name: 'c',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 4,
          price: 5
          },
         {food_name: 'd',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 3,
          price: 5
          },
         {food_name: 'e',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 2,
          price: 5
          }],
         status: '已取消'
         },
         {bussiness: 'fff',
         picture: 'images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order6",
         date: '2016-03-24',
         total: 10,
         order_list: [
         {food_name: 'a',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 4,
          price: 5
          },
         {food_name: 'b',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 3,
          price: 5
          },
         {food_name: 'c',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 5,
          price: 5
          },
         {food_name: 'd',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 2,
          price: 5
          },
         {food_name: 'e',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 1,
          price: 5
          }],
         status: '未处理'
        },
        {bussiness: 'ggg',
         picture: 'images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order7",
         date: '2016-03-24',
         total: 10,
         order_list: [
         {food_name: 'a',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 4,
          price: 5
          },
         {food_name: 'b',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 3,
          price: 5
          },
         {food_name: 'c',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 2,
          price: 5
          },
         {food_name: 'd',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 5,
          price: 5
          },
         {food_name: 'e',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 4,
          price: 5
          }],
         status: '配送中'
         },
         {bussiness: 'hhh',
         picture: 'images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order8",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 3,
          price: 5
          },
         {food_name: 'b',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 2,
          price: 5
          },
         {food_name: 'c',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 1,
          price: 5
          },
         {food_name: 'd',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 5,
          price: 5
          },
         {food_name: 'e',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 4,
          price: 5
          }],
         status: '已完成'
         },
         {bussiness: 'iii',
         picture: 'images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order9",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 3,
          price: 5
          },
         {food_name: 'b',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 2,
          price: 5
          },
         {food_name: 'c',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 1,
          price: 5
          },
         {food_name: 'd',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 4,
          price: 5
          },
         {food_name: 'e',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 5,
          price: 5
          }],
         status: '未处理'
         },
         {bussiness: 'jjj',
         picture: 'images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order10",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 1,
          price: 5
          },
         {food_name: 'b',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 2,
          price: 5
          },
         {food_name: 'c',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 3,
          price: 5
          },
         {food_name: 'd',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 4,
          price: 5
          },
         {food_name: 'e',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 5,
          price: 5
          }],
         status: '已取消'
         },
         {bussiness: 'kkk',
         picture: 'images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order11",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 5,
          price: 5
          },
         {food_name: 'b',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 4,
          price: 5
          },
         {food_name: 'c',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 3,
          price: 5
          },
         {food_name: 'd',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 3,
          price: 5
          },
         {food_name: 'e',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 2,
          price: 5
          }],
         status: '已完成'
         },
         {bussiness: 'lll',
         picture: 'images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order12",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 1,
          price: 5
          },
         {food_name: 'b',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 2,
          price: 5
          },
         {food_name: 'c',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 3,
          price: 5
          },
         {food_name: 'd',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 4,
          price: 5
          },
         {food_name: 'e',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 5,
          price: 5
          }],
         status: '未处理'
        },
        {bussiness: 'nnn',
         picture: 'images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order13",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 5,
          price: 5
          },
         {food_name: 'b',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 4,
          price: 5
          },
         {food_name: 'c',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 3,
          price: 5
          },
         {food_name: 'd',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 2,
          price: 5
          },
         {food_name: 'e',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 1,
          price: 5
          }],
         status: '配送中'
         },
         {bussiness: 'mmm',
         picture: 'images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order14",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 1,
          price: 5
          },
         {food_name: 'b',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 2,
          price: 5
          },
         {food_name: 'c',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 3,
          price: 5
          },
         {food_name: 'd',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 4,
          price: 5
          },
         {food_name: 'e',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 5,
          price: 5
          }],
         status: '已完成'
         },
         {bussiness: 'ooo',
         picture: 'images/flower.jpg',
         address: 'qwertyu',
         tel: '12345678900',
         orderid: "order15",
         total: 10,
         date: '2016-03-24',
         order_list: [
         {food_name: 'a',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 5,
          price: 5
          },
         {food_name: 'b',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 4,
          price: 5
          },
         {food_name: 'c',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 3,
          price: 5
          },
         {food_name: 'd',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 2,
          price: 5
          },
         {food_name: 'e',
         picture: 'images/flower.jpg',
          amount: 3,
          count: 543,
             comments: [
              {user: '123*****678',
              date: '2016-02-14',
              star: 4,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-05-03',
              star: 3,
              description: "良心商家~"},
              {user: '123*****678',
              date: '2015-12-14',
              star: 5,
              description: "好吃好吃好好吃！"},
              {user: '123*****678',
              date: '2016-04-07',
              star: 2,
              description: "一般般"}
             ],
          star: 1,
          price: 5
          }],
         status: '已完成'
        }],
        currentOrderId: this.$route.params.orderId,
        bussiness_name: "zzzzz",
        star: 3,
        address: "新天地三楼",
        tel: "12345678976",
        count: 97}
  	},
  	methods: {
  		cancelOrder: function(orderid) {
  			alert("成功取消订单");
  		},
  		completeOrder: function(orderid) {
  			alert("成功确认收货");
  		},
  		openComment: function() {
  			this.isShow = true;
  		},
  		submitComments: function(food_name) {
  			this.isShow = false;
  		},
  		resetIsShow: function() {
  			this.isShow = false;
  		},
  		hoverGrade: function(index) {
        this.changeStarsGrade(index);
      },
      getGrade: function(index) {
        this.changeStarsGrade(index);
      },
      resetStars: function() {
        var stars = $(".grade-star");
        for (var i = 0; i < stars.length; i++) {
          $(stars[i]).removeClass("gold").addClass("gray");
        }
      },
      changeStarsGrade: function(index) {
        var stars = $(".grade-star");
        this.resetStars();
        for (var i = 0; i <= index; i++) {
          $(stars[i]).removeClass("gray").addClass("gold");
        }
        this.grade = index + 1;
      }
  	},
    ready: function() {
      $(document).foundation();
    }
  }
</script>

<template>
  <div class="row orderdetail small-up-1 medium-up-2">
  <template v-for="item in orders">
  <template v-if="item.orderid == currentOrderId">
    <div class="column">
      <div class="row">
      	<div class="column">
  	  	  <img class="thumbnail" src="../images/flower.jpg" />
      	</div>
      	<div class="column align-middle ">
      	  <h4>{{bussiness_name}}</h4>
          <div>
            <i v-for="n in star" class="fi-star gold"></i><i v-for="n in (5-star)" class="fi-star gray"></i>
          </div>
          <div>月销售量{{count}}单</div>
          <div><i class="fi-telephone"></i>{{tel}}</div>
          <div><i class="fi-marker"></i> {{address}}</div>
      	</div>
      </div>
      <div class="row">
      	<div class="column medium-6">
      	  <div class="callout small">
      	    <div>收货地址：{{item.address}}</div>
      	  </div>
      	</div>
      </div>
      <div class="row">
        <div class="column medium-6">
          <div class="callout small">
      	    <div>收货人电话：{{item.tel}}</div>
      	  </div>
        </div>
      </div>
      <div class="row">
        <div class="column medium-6">
          <div class="callout small">
      	    <div>总计：<i class="fi-yen"></i>{{item.total}}</div>
      	  </div>
        </div>
      </div>
      <div class="row">
        <div class="column medium-6">
          <div class="callout small">
      	    <div>状态：{{item.status}}</div>
      	  </div>
        </div>
      </div>
      <div class="row">
        <div class="column">
          <!-- v-link="{name: 'comment', params: {orderId: item.orderid}}"-->
          <div v-if="item.status == '已完成'" class="button comment" data-open="comment">评价</div>
          <!-- v-link="{name: 'comment', params: {orderId: item.orderid}}"-->
          <div v-if="item.status == '已取消' || item.status == '已完成'" class="button complain" data-open="complain">投诉</div>
          <!-- v-link="{name: 'comment', params: {orderId: item.orderid}}"-->
          <div v-if="item.status == '未处理'" class="button cancel" data-open="cancel">取消订单</div>
          <div v-if="item.status == '配送中'" class="button complete" data-open="complete">完成订单</div>
        </div>
      </div>
  	</div>
  	<div class="column">
  	<template v-for="order in item.order_list" >
  	  <div class="callout small">
  	  <a :data-open="order.food_name">
  	    <div class="row">
          <div class="column align-middle"><img :src="order.picture" /></div>
  	      <div class="column align-middle ">{{order.food_name}}</div>
  	      <div class="column align-middle ">{{order.amount}}份</div>
  	      <div class="column align-middle "><i class="fi-yen"></i> {{order.price}}/份</div>
        </div>
      </a>
      </div>
      <div class="reveal" :id="order.food_name" data-reveal>
      	<h2>{{order.food_name}}</h2>
        <img :src="order.picture" />
        <div class="row food_detail_">
          <div class="column">{{order.food_name}}</div>
          <div class="column-6">
            <i v-for="n in order.star" class="fi-star gold"></i><i v-for="n in (5-order.star)" class="fi-star gray"></i>
          </div>
          <div class="column price"><i class="fi-yen"></i> {{order.price}}</div>
          <div class="column count_detail">剩余<span class="item_count">{{order.count}}</span>份</div>
        </div>
        <div class="button" v-if="item.status == '已完成'" data-open="order_again" v-on:click="openComment">评价该食物</div>
        <form method="post" action="./" v-if="isShow">
          <div>
            您的评分是：{{grade}} 分
            <template v-for="n in 5">
              <i class="fi-star gray grade-star" v-bind:class="n+''" :id="'star-'+n" v-on:click="getGrade(n)" v-on:mouseover="hoverGrade(n)"></i>
            </template>
          </div>
    	  <textarea id="comment_text" name="comment" placeholder="Enter your comments on this order"></textarea>
    	  <input class="button expanded" id="comment_button" type="submit" value="提交评价" v-on:click="submitComments(order.food_name)"></input>
        </form>
        <button class="close-button" data-close aria-label="Close modal" type="button" v-on:click="resetIsShow">
          <span aria-hidden="true">&times;</span>
        </button>
        <ul class="show_comments accordion" data-accordion data-multi-expand="true">
          <li v-for="comment in order.comments" v-bind:class="[$index==0 ? 'is-active':'']" class="accordion-item" data-accordion-item>
            <a class="accordion-title">
              <span>{{comment.user}}</span>
              <i v-for="n in comment.star" class="fi-star gold"></i><i v-for="n in (5-comment.star)" class="fi-star gray"></i>
              <span>{{comment.date}}</span>
            </a>
            <div class="description accordion-content" data-tab-content>{{comment.description}}</div>
          </li>
        </ul>
      </div>
      </template>
    </div>

    <div class="reveal" id="comment" data-reveal>
      <form method="post" action="./">
        <div>
          您的评分是：{{grade}} 分
          <template v-for="n in 5">
            <i class="fi-star gray grade-star" v-bind:class="n+''" :id="'star-'+n" v-on:click="getGrade(n)" v-on:mouseover="hoverGrade(n)"></i>
          </template>
        </div>
        <textarea id="comment_text" name="comment" placeholder="Enter your comments on this order"></textarea>
        <input class="button expanded" id="comment_button" type="submit" value="提交评价"></input>
      </form>
      <button class="close-button" data-close aria-label="Close modal" type="button">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    <div class="reveal" id="complain" data-reveal>
      <form method="post" action="./">
      	<label>投诉原因：
      	  <textarea id="complain_text" name="complain" placeholder="Enter your complain reasons here."></textarea>
      	</label>
      	<input class="button expanded" id="complain_button" type="submit" value="提交投诉"></input>
      </form>
      <button class="close-button" data-close aria-label="Close modal" type="button">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    <div class="reveal" id="cancel" data-reveal>
      <div class="button expanded" id="cancel_button" v-on:click="cancelOrder(currentOrderId)">确认取消</div>
      <div class="button expanded" data-close>不取消了</div>
    </div>
    <div class="reveal" id="complete" data-reveal>
      <div class="button expanded" id="complete_button" v-on:click="completeOrder(currentOrderId)">确认收货</div>
      <div class="button expanded" data-close>手滑点错了</div>
    </div>
  </template>
  </template>	
  </div>
</template>

<style lang="sass">
  // Import
  @import "../variables.scss";

  // Style
  * {
    box-sizing:border-box;
    -moz-box-sizing:border-box; /* Firefox */
    -webkit-box-sizing:border-box; /* Safari */
  }

  .orderdetail {
    margin-top: 20px;
  }
</style>