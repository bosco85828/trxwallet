# TRXwallet

## 使用方式

* 創建地址

請求方式: "GET"
uri: /createAccount

響應範例:
```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 451
Server: Werkzeug/2.0.3 Python/3.9.13
Date: Sat, 25 Mar 2023 10:25:36 GMT

{
  "data": {
    "base58check_address": "TPJ8LJxWiUb6GCYRXnt1EAehfuwhQVWBA5", 
    "hex_address": "41922da4498907f47c2a3b17ff8312fedf05eb41b3", 
    "private_key": "", 
    "public_key": ""
  }, 
  "meta": {
    "message": "", 
    "status": "success"
  }
}
```

* 查詢餘額

請求方式: "POST"
uri: /getbalance
請求參數:
    {
        "address":youraddres
    }

響應範例:
```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 53
Server: Werkzeug/2.0.3 Python/3.9.13
Date: Sat, 25 Mar 2023 10:17:33 GMT

{
  "data": {
    "Balance": 3670754.345048,
    "Symbol": "USDT"
  },
  "meta": {
    "message": "",
    "status": "success"
  }
}
```