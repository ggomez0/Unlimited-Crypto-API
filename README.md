# Unlimited Crypto API Documentation

The **Unlimited Crypto API** provides endpoints to retrieve cryptocurrency prices and market information for top coins. This document covers the available API endpoints, their response formats, error handling, and usage examples.

---

## Base URL
https://apicrypto.ggomez.tech

---

## Endpoints

### 1. `GET /api/price/{name_coin}`

This endpoint retrieves the current price of a specific cryptocurrency based on the provided coin name.

| Parameter  | Type   | Description                                       |
|------------|--------|---------------------------------------------------|
| name_coin  | string | The name of the cryptocurrency (e.g., bitcoin, ethereum) |

#### Response

The response will include the name of the cryptocurrency and its current price.

### Example 

```http
GET /api/price/eth
```


```json
{
  "coin": "ethereum",
  "price": "$2,395.23"
}
```

---

### 2. `GET /api/top/{limit}`

This endpoint retrieves the top cryptocurrencies based on their market value. You can limit the number of coins returned by specifying the `limit` parameter.

| Parameter | Type    | Description                       |
|-----------|---------|-----------------------------------|
| limit     | integer | The maximum number of coins to return |

#### Response

The response is an array of top coins, including the coin's image, name, price, and symbol.

#### Example Request

```http
GET /api/top/2
```

### Example

```json
[
  {
    "name": "Bitcoin",
    "price": "$62,656.79",
    "symbol": "BTC"
  },
  {
    "name": "Ethereum",
    "price": "$2,390.53",
    "symbol": "ETH"
  }
]
```

### 3. `GET /api/ath/{name_coin}`

This endpoint retrieves the ATH (all time high) price of a specific cryptocurrency based on the provided coin name.

#### Response

The response will include the name of the cryptocurrency, his ATH and when its happened.

### Example 

```http
GET /api/ath/eth
```


```json
{
  "ath": 4864.91,
  "ath_date": 1635984000000,
  "symbol": "ETH"
}
```
## Error Responses

For both endpoints, the API may return error responses in the following format:

#### Error Example

```json
{
  "error": "Coin not found"
}
```

| HTTP Status Code | Description                                  |
|------------------|----------------------------------------------|
| 404 Not Found    | The requested coin or resource does not exist |
| 400 Bad Request  | Invalid input or parameters provided          |


## Deploying the API Yourself

To deploy the **Unlimited Crypto API** on your own, follow these steps:

1. **Fork the Repository**: Click the "Fork" button at the top right of the repository page to create your own copy of the repository.

1. **Sign Up / Log In to Vercel**: Go to [Vercel](https://vercel.com/) 

2. **Import Project**: Click on the "New Project" button. Select "Import Git Repository" and choose the forked repository.

3. **Access Your API**: After deployment, you will get a unique URL where your API is hosted. You can use this URL to access your API endpoints.
