package config

import (
    "github.com/spf13/viper"
    "log"
)

type Config struct {
    Database struct {
        DSN string
    }
    Server struct {
        Port string
    }
    Log struct {
        Level string
    }
}

func LoadConfig() Config {
    viper.SetConfigFile("config.yml")
    if err := viper.ReadInConfig(); err != nil {
        log.Fatalf("Error reading config: %v", err)
    }
    var cfg Config
    if err := viper.Unmarshal(&cfg); err != nil {
        log.Fatalf("Error unmarshaling config: %v", err)
    }
    return cfg
}