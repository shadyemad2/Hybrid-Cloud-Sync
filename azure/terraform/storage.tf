
resource "azurerm_storage_account" "storage" {
  name                     = "hybridsyncstorage1"
  resource_group_name      = "learn-e181f92c-658e-4d60-887e-7bcdff2894cc"
  location                 = "West US"
  account_tier             = "Standard"
  account_replication_type = "LRS"
  is_hns_enabled           = false
  access_tier              = "Hot"
  enable_https_traffic_only = true

  blob_properties {
    delete_retention_policy {
      days = 7
    }
  }
}

resource "azurerm_storage_container" "container" {
  name                  = "sync-container"
  storage_account_name  = azurerm_storage_account.storage.name
  container_access_type = "private"
}

