package config

import (
    "github.com/sirupsen/logrus"
    "github.com/spf13/viper"
)

type Config struct {
    Database struct {
        DSN          string `mapstructure:"dsn"`
        MaxOpenConns int    `mapstructure:"max_open_conns"`
        MaxIdleConns int    `mapstructure:"max_idle_conns"`
    }
    Server struct {
        Port string `mapstructure:"port"`
    }
    Log struct {
        Level string `mapstructure:"level"`
    }
}

func LoadConfig() Config {
    viper.SetConfigFile("configs/config.yml")
    viper.SetConfigType("yaml")
    if err := viper.ReadInConfig(); err != nil {
        logrus.Fatalf("Error reading config: %v", err)
    }
    var cfg Config
    if err := viper.Unmarshal(&cfg); err != nil {
        logrus.Fatalf("Error unmarshaling config: %v", err)
    }
    return cfg
}