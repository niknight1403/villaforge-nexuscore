// main.go
package main

import (
    "net/http"
    "github.com/dgrijalva/jwt-go"
    "github.com/gin-gonic/gin"
)

var jwtKey = []byte("your_secret_key")

func AuthMiddleware() gin.HandlerFunc {
    return func(c *gin.Context) {
        tokenString := c.GetHeader("Authorization")
        if tokenString == "" {
            c.JSON(http.StatusUnauthorized, gin.H{"error": "Missing auth token"})
            c.Abort()
            return
        }
        _, err := jwt.Parse(tokenString, func(token *jwt.Token) (interface{}, error) {
            return jwtKey, nil
        })
        if err != nil {
            c.JSON(http.StatusUnauthorized, gin.H{"error": "Invalid auth token"})
            c.Abort()
            return
        }
        c.Next()
    }
}

func main() {
    r := gin.Default()
    r.Use(AuthMiddleware())
    r.GET("/api", func(c *gin.Context) {
        c.JSON(http.StatusOK, gin.H{"message": "API is accessible"})
    })
    r.Run() // listen and serve on 0.0.0.0:8080
}