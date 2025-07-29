terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.90.0"
    }
  }
}

provider "azurerm" {
  features {}

  subscription_id = "8b6001cd-a329-4999-8dbb-3b3261bb100a"
}

